import psycopg2
from psycopg2 import sql
import numpy as np
import pandas as pd
from tqdm.notebook import tqdm
import time
import torch
from torch_geometric.utils import sort_edge_index
import os

def extract_execution_time(explain_output):
    """
    Extracts the total execution time from the given query plan.

    The function parses the query plan to find the execution time, which is typically
    represented in the format 'Execution Time: X ms'. It returns the execution time
    in seconds.

    Parameters:
    query_plan (list): A list of strings representing the lines of the query plan output.

    Returns:
    float: The total execution time in ms. If the execution time cannot be found,
           returns None.
    """

    execution_time = 0.0
    pattern = re.compile(r"Execution Time: (\d+\.\d+) ms")
    for row in explain_output:
        match = pattern.search(row[0])
        if match:
            execution_time += float(match.group(1))
    return execution_time
    
def connect_to_postgres(dbname = "postgres"):
    """Connect to the PostgreSQL database server."""
    try:
        conn = psycopg2.connect(
            dbname=dbname,  # Connect to default db to create new db
            user='postgres',
            password='password',
            host='localhost'
        )
        print("Connection successful.")
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        raise

def create_database(conn, new_db_name):
    """Create a new database."""
    try:
        conn.autocommit = True
        with conn.cursor() as cursor:
            cursor.execute(sql.SQL("CREATE DATABASE {};").format(sql.Identifier(new_db_name)))
            print(f"Database '{new_db_name}' created successfully.")
    except Exception as e:
        print(f"Error creating database: {e}")
        raise
    finally:
        conn.autocommit = False

def create_schema(conn, schema_sql):
    """Create the database schema."""
    try:
        with conn.cursor() as cursor:
            cursor.execute(schema_sql)
            conn.commit()
            print("Schema created successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Error creating schema: {e}")
        raise

def upload_csv_to_table(conn, csv_file_path, table_name):
    """Upload a CSV file to a table using the COPY command."""
    try:
        with conn.cursor() as cursor:
            with open(csv_file_path, 'r') as f:
                cursor.copy_expert(
                    sql.SQL("""
                        COPY {} FROM STDIN WITH (FORMAT CSV, HEADER TRUE, DELIMITER ',');
                    """).format(sql.Identifier(table_name)), f
                )
            conn.commit()
            print(f"Data from '{csv_file_path}' uploaded to table '{table_name}' successfully using COPY.")
    except Exception as e:
        conn.rollback()
        print(f"Error uploading CSV data using COPY: {e}")
        raise

def create_index(conn, table_name, column_name):
    """Create an index on a specific column."""
    try:
        with conn.cursor() as cursor:
            index_name = f"{table_name}_{column_name}_idx"
            cursor.execute(sql.SQL("CREATE INDEX {} ON {} ({});").format(
                sql.Identifier(index_name),
                sql.Identifier(table_name),
                sql.Identifier(column_name)
            ))
            conn.commit()
            print(f"Index '{index_name}' created successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Error creating index: {e}")
        raise

def read_data(conn, query):
    """Read data from the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
            print("Data read successfully.")
            return results
    except Exception as e:
        print(f"Error reading data: {e}")
        raise

def update_data(conn, query, params):
    """Update data in the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            conn.commit()
            print("Data updated successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Error updating data: {e}")
        raise

def delete_database(conn, db_name):
    """Delete the specified database including all its schemas, tables, and indexes."""
    try:
        conn.autocommit = True
        with conn.cursor() as cursor:
            cursor.execute(sql.SQL("DROP DATABASE IF EXISTS {};").format(sql.Identifier(db_name)))
            print(f"Database '{db_name}' deleted successfully.")
    except Exception as e:
        print(f"Error deleting database: {e}")
        raise
    finally:
        conn.autocommit = False

def create_edges_table(conn):
    """Create an edges table with foreign key constraints to the main table."""
    edges_schema = """
    CREATE TABLE edges (
        source_id INTEGER NOT NULL,
        target_id INTEGER NOT NULL,
        FOREIGN KEY (source_id) REFERENCES nodes(id) ON DELETE CASCADE,
        FOREIGN KEY (target_id) REFERENCES nodes(id) ON DELETE CASCADE
    );
    """
    try:
        with conn.cursor() as cursor:
            cursor.execute(edges_schema)
            conn.commit()
            print("Edges table created successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Error creating edges table: {e}")
        raise

def upload_edges_csv_to_table(conn, csv_file_path):
    """Upload a CSV file to the edges table using the COPY command."""
    try:
        with conn.cursor() as cursor:
            with open(csv_file_path, 'r') as f:
                cursor.copy_expert(
                    sql.SQL("""
                        COPY edges (source_id, target_id) FROM STDIN WITH (FORMAT CSV, HEADER TRUE, DELIMITER ',');
                    """), f
                )
            conn.commit()
            print(f"Edges data from '{csv_file_path}' uploaded successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Error uploading edges CSV data: {e}")
        raise

def recurse_edge_index_iterative(source_nodes, edge_index, max_depth):
    """
    Optimized function to compute the subgraph around the source nodes up to a given depth.
    Uses an iterative approach instead of recursion.
    """
    visited_nodes = set(source_nodes)
    current_frontier = np.array(source_nodes)
    
    subgraph_edges = []

    for _ in range(max_depth):
        # Find edges where the target node is in the current frontier
        target_mask = np.isin(edge_index[1], current_frontier)
        subgraph_edge_index = edge_index[:, target_mask]
        subgraph_edges.append(subgraph_edge_index)

        # Update the current frontier with the source nodes of these edges
        current_frontier = np.setdiff1d(subgraph_edge_index[0], list(visited_nodes))
        visited_nodes.update(current_frontier)
        
        if len(current_frontier) == 0:
            break

    # Combine edges from all hops
    return np.concatenate(subgraph_edges, axis=1) if subgraph_edges else np.empty((2, 0), dtype=edge_index.dtype)


def get_subgraph_from_in_mem_graph_optimized(X, y, i, edge_index, hops):
    """
    Optimized version of subgraph extraction.
    """
    subgraph_edge_index = recurse_edge_index_iterative([i], edge_index, hops)
    unique_node_ids, remapping = np.unique(subgraph_edge_index, return_inverse=True)
    
    # Extract features and labels
    features = X.iloc[unique_node_ids, :].values
    labels = y.iloc[unique_node_ids, :].values.squeeze()

    # Remap edge indices
    remapped_edge_index = remapping.reshape(2, -1)
    return remapped_edge_index, features, labels, unique_node_ids

def create_db(node_file_name):
    # Create a new database
    conn = connect_to_postgres(dbname = "postgres")
    new_db_name = node_file_name.split(".")[0]
    create_database(conn, new_db_name)
    conn.close()
    conn = connect_to_postgres(new_db_name)
    return conn, new_db_name

def create(conn, node_file_name, edge_file_name, X_and_y):
    column_types = ["id SERIAL PRIMARY KEY"]
    for col in X_and_y.columns:
        if "y" in col:
            column_types.append(f"{col} INTEGER")
            continue
        column_types.append(f"{col} REAL")
        
    node_schema = f"""
    CREATE TABLE nodes (
        {",".join(column_types)}
    );
    """
    start = time.time()
    create_schema(conn, node_schema)
    create_edges_table(conn)
    
    csv_file_path = f"syn_data/{node_file_name}"  # Replace with your CSV file path
    upload_csv_to_table(conn, csv_file_path, "nodes")
    create_index(conn, "nodes", "id")
    upload_edges_csv_to_table(conn, f"syn_data/{edge_file_name}")
    create_index(conn, "edges", "target_id")
    creation_time = time.time() - start
    return creation_time

def read(conn, hops, X_and_y, X, y, edge_index, random_sample_size = 1_000):
    np.random.seed(42)
    seed_node_ids = np.random.choice(np.arange(X_and_y.shape[0]), size = random_sample_size, replace = False)
    
    with conn.cursor() as cursor:
        complete_time = 0
        complete_test_time = 0
        feature_columns = list(filter(lambda col: "f" in col, X_and_y.columns))
        label_columns = list(filter(lambda col: "y" in col, X_and_y.columns))
        for seed_node_id in tqdm(seed_node_ids):
            try:
                start = time.time()
                cursor.execute(f"""
        WITH RECURSIVE NestedTargets AS (
            SELECT 0 AS depth, source_id, target_id
            FROM edges
            WHERE target_id = {seed_node_id}
            
            UNION ALL
            
            SELECT nt.depth + 1, e.source_id, e.target_id
            FROM edges e
            JOIN NestedTargets nt ON e.target_id = nt.source_id
            WHERE nt.depth < {hops - 1}
        ),
        
        node_ids AS (
            SELECT DISTINCT id FROM (
                SELECT source_id AS id FROM NestedTargets
                UNION
                SELECT target_id AS id FROM NestedTargets
            ) AS combined_ids
        ),
        
        node_data AS (
            SELECT 
                id, 
                {", ".join(X_and_y.columns)}
            FROM nodes
            WHERE id IN (SELECT id FROM node_ids)
            ORDER BY id
        )
        
        SELECT
            (SELECT array_agg(array[{", ".join(feature_columns)}]) FROM node_data) AS node_table,
            (SELECT array_agg(array[{", ".join(label_columns)}]) FROM node_data) AS label_table,
            (SELECT array_agg(array[source_id, target_id])
             FROM (SELECT DISTINCT source_id, target_id FROM NestedTargets) AS edges) AS edge_table,
             (SELECT array_agg(id) FROM node_data) AS node_ids;
    """)
                results = cursor.fetchall()[0]
                labels = np.array(results[1])
                subgraph_node_features = np.array(results[0])
                if results[0] is None:
                    continue
                
                subgraph_edges = np.array(results[2]).transpose()
                
                node_ids = np.array(results[-1]) #subgraph_node_features[:, 0]
                cols_source = np.searchsorted(node_ids, subgraph_edges[0])
                cols_target = np.searchsorted(node_ids, subgraph_edges[1])
                
                remapped_edge_index = np.concatenate([np.expand_dims(cols_source, axis = 0), np.expand_dims(cols_target, axis = 0)], axis = 0)
                features = subgraph_node_features #[:, 1:]
                overall_run_time = time.time() - start 
                
                complete_time += overall_run_time
                # Testing
                test_time = time.time()
                remapped_edge_index_test, features_test, labels_test, unique_node_ids = get_subgraph_from_in_mem_graph_optimized(X, y, seed_node_id, edge_index, hops)                    
                complete_test_time += time.time() - test_time
                assert (sort_edge_index(torch.from_numpy(remapped_edge_index_test)) == sort_edge_index(torch.from_numpy(remapped_edge_index))).sum() / (remapped_edge_index_test.shape[-1] * remapped_edge_index_test.shape[0]), "Edges doesnt match"
                assert np.allclose(node_ids, unique_node_ids)
                assert np.max(np.abs(features_test - features)) < 1e-3, "features does not match"
                # assert np.allclose(labels_test.shape, labels.shape), "Labels does not match"
                # print(f"Fetched {remapped_edge_index.shape} edges, {labels.shape} labels, {features.shape} features in ({overall_run_time} s)")
            except Exception as e:
                conn.rollback()
                print(f"Error reading data: {e}")
                raise   
    return (complete_time, complete_test_time)

def update_nodes(conn, X_and_y, random_sample_size = 1000):
    feature_columns = list(filter(lambda col: "f" in col, X_and_y.columns))
    label_columns = list(filter(lambda col: "y" in col, X_and_y.columns))
    with conn.cursor() as cursor:
        np.random.seed(42)
        node_ids = np.random.choice(np.arange(X_and_y.shape[0]), size = random_sample_size, replace = False).tolist()
        start = time.time()
        for node_id in tqdm(node_ids):
            np.random.seed(42)
            features = np.random.rand(len(feature_columns)).tolist()  # Random values between 0 and 1
            labels = np.random.randint(0, 2, size=len(label_columns)).tolist()  # Adjust label range as needed            
            sql_query = f"""
            UPDATE nodes 
            SET {",".join([f'{col} = %s' for col in feature_columns])}, {",".join([f'{col} = %s' for col in label_columns])}
            WHERE id = %s;
            """
            values = (*features, *labels, node_id)
            cursor.execute(sql_query, values)
        return time.time() - start

def update_edges(conn, edge_index, X_and_y, random_sample_size = 1000):
    with conn.cursor() as cursor:
        np.random.seed(42)
        edge_ids = np.random.choice(np.arange(edge_index.shape[-1]), size = random_sample_size, replace = False).tolist()
        selected_edges = edge_index[:, edge_ids].transpose(-1, 0 )
        start = time.time()
        for selected_edge in tqdm(selected_edges):
            source_id, target_id = selected_edge
            np.random.seed(42)
            new_target_id = int(np.random.randint(0, X_and_y.shape[0]))
            sql_query = "UPDATE edges SET target_id = %s WHERE source_id = %s AND target_id = %s;"
            values = (new_target_id, int(source_id), int(target_id))
            cursor.execute(sql_query, values)
        return time.time() - start

def delete(conn, new_db_name):
    start = time.time()
    conn.close()
    conn = connect_to_postgres()
    delete_database(conn, new_db_name)
    conn.close()
    return time.time() - start

def eval_ppi(output_df):
    edge_file_name = "ppi_edge_index.csv"
    node_file_name = "ppi.csv"
    X = pd.read_csv(f"data/ppi_x.csv")
    y = pd.read_csv(f"data/ppi_y.csv")
    y.columns = [f"y_{col}" for col in y.columns]
    y = y.astype(np.int8)
    edges = pd.read_csv("data/" + edge_file_name)
    edges.columns = ["source_id", "target_id"]
    X_and_y = X.copy()
    X_and_y.columns = list(map(lambda col: f"f_{col}", X_and_y.columns))
    X_and_y = pd.concat((X_and_y, y), axis = 1)
    
    node_file_name = "X_y_ppi__postgres_columns.csv"
    X_and_y.to_csv(f"syn_data/{node_file_name}", sep = ",", index = True)
    edges.to_csv(f"syn_data/{edge_file_name}", sep = ",", index = False)
    edge_index = edges.values.transpose(-1, 0)
    
    conn, db_name = create_db(node_file_name)
    create_time = create(conn, node_file_name, edge_file_name, X_and_y)
    read_times, read_times_mem = dict(), dict()
    for hops in range(1,4):
        read_time, read_time_mem = read(conn, hops, X_and_y, X, y, edge_index, random_sample_size = 1_000)
        read_times[hops] = read_time
        read_times_mem[hops] = read_time_mem
        
    update_time_nodes = update_nodes(conn, X_and_y, 1_000)
    update_time_edges = update_edges(conn, edge_index, X_and_y, 1_000)
    delete_time= delete(conn,db_name )
    new_row_dict = {"name": "ppi", "create": create_time, "update_nodes": update_time_nodes, "update_edges": update_time_edges, "delete": delete_time}
    for hops in read_times:
        new_row_dict[f"read_{hops}"] = read_times[hops]
        new_row_dict[f"read_in_mem_{hops}"] = read_times_mem[hops]
    new_row = pd.DataFrame([new_row_dict])
    output_df = pd.concat((output_df, new_row), ignore_index=True)
    return output_df

def eval_synth(output_df):
    for num_nodes in tqdm([1_000, 10_000, 100_000, 1_000_000]):
        for num_edges in tqdm(["5_edges", "10_edges", "20_edges", "scale_free"]):
            if num_nodes == 1_000_000 and (num_edges == "10_edges" or num_edges == "20_edges"): continue
            feature_file_name = f"X_{str(num_nodes)}_nodes_{num_edges}.csv"
            label_file_name = f"y_{str(num_nodes)}_nodes_{num_edges}.csv"
            edge_file_name = f"edge_index_{str(num_nodes)}_nodes_{num_edges}.csv"
            assert os.path.exists(f"syn_data/{feature_file_name}"), "Feature file does not exist"
            assert os.path.exists(f"syn_data/{label_file_name}"), "Label file does not exist"
            assert os.path.exists(f"syn_data/{edge_file_name}"), "Edge file does not exist"
            
            X = pd.read_csv(f"syn_data/{feature_file_name}")
            y = pd.read_csv(f"syn_data/{label_file_name}")
            y.columns = [f"y_{col}" for col in y.columns]
            y = y.astype(np.int8)
            edges = pd.read_csv(f"syn_data/{edge_file_name}")
            edges.columns = ["source_id", "target_id"]
            edge_index = edges.values.transpose(-1, 0)
            node_file_name = f"X_and_y_{str(num_nodes)}_nodes_{num_edges}_postgres_columns.csv"
            if not os.path.exists(f"syn_data/{node_file_name}"):
                X_and_y = X.copy()
                X_and_y.columns = list(map(lambda col: f"f_{col}", X_and_y.columns))
                X_and_y = pd.concat((X_and_y, y), axis = 1)
                X_and_y.to_csv(f"syn_data/{node_file_name}", sep = ",", index = True)
            else:
                X_and_y = pd.read_csv(f"syn_data/{node_file_name}", sep = ",", index_col = 0)
            conn, new_db_name = create_db(node_file_name)
            create_time = create(conn, node_file_name, edge_file_name, X_and_y)
            read_times = dict()
            read_times_mem = dict()
            for hops in tqdm(range(1, 4)):
                read_time, read_time_mem = read(conn, hops, X_and_y, X, y, edge_index, 1_000)
                read_times[hops] = read_time
                read_times_mem[hops] = read_time_mem
            update_time_nodes = update_nodes(conn, X_and_y, 1000)
            update_time_edges = update_edges(conn, edge_index, X_and_y, 1000)
            delete_time = delete(conn, new_db_name)
            new_row_dict = {"name": f"{str(num_nodes)}_nodes_{num_edges}", "create": create_time, "update_nodes": update_time_nodes, "update_edges": update_time_edges, "delete": delete_time}
            for hops in read_times:
                new_row_dict[f"read_{hops}"] = read_times[hops]
                new_row_dict[f"read_in_mem_{hops}"] = read_times_mem[hops]
            new_row = pd.DataFrame([new_row_dict])
            output_df = pd.concat((output_df, new_row), ignore_index=True)
    return output_df

num_iterations = 10
off_set = 0
for i in tqdm(range(off_set, num_iterations + off_set)):
    print(f"Iteration {i}")
    output_df = pd.DataFrame(columns = ["name", "create", "update_nodes", "update_edges", "delete"])
    output_df = eval_ppi(output_df)
    output_df = eval_synth(output_df)
    output_df.to_csv(f"postgres_col_{i}.csv")
