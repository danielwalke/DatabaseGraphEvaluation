import MySQLdb
import numpy as np
import pandas as pd
from tqdm.notebook import tqdm
import time
import torch
from torch_geometric.datasets import PPI
from torch_geometric.loader import DataLoader
from torch_geometric.utils import sort_edge_index
import os
import json

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
    
def connect_to_mysql(database=None):
    """Connect to MySQL database using mysqlclient"""
    if database is None:
        return MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='password',
        local_infile=True# Enable LOAD DATA LOCAL INFILE
    )
    return MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='password',
        db=database,
        local_infile=True# Enable LOAD DATA LOCAL INFILE
    )

def create_database_with_conn(conn, db_name):
    with conn.cursor() as cursor:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        conn.commit()
    return connect_to_mysql(database=db_name)

def create_database(node_file_name):
    conn = connect_to_mysql()
    new_db_name = node_file_name.split(".")[0]
    create_database_with_conn(conn, new_db_name)
    conn.close()
    conn = connect_to_mysql(new_db_name)
    return conn, new_db_name

def create_index(conn, table_name, column_name):
    """Create an index on a specific column."""
    try:
        with conn.cursor() as cursor:
            index_name = f"{table_name}_{column_name}_idx"
            cursor.execute(f"CREATE INDEX {index_name} ON {table_name} ({column_name});")
            conn.commit()
            print(f"Index '{index_name}' created successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Error creating index: {e}")
        raise

def create(conn, node_file_name, edge_file_name, X_and_y):
    # For each column, we'll store arrays as TEXT with comma-separated values
    column_types = ["id INTEGER PRIMARY KEY"] ## AUTO INCREMENT
    for col in X_and_y.columns:
        column_types.append(f"{col} JSON")
    
    node_schema = f"""
    CREATE TABLE IF NOT EXISTS nodes (
        {",".join(column_types)}
    );
    """
    
    start = time.time()
    with conn.cursor() as cursor:
        cursor.execute(node_schema)
        
        # Create edges table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS edges (
            source_id INTEGER,
            target_id INTEGER
        )
        """)
        conn.commit()
    
    csv_file_path = f"syn_data/{node_file_name}"
    
    # For the nodes table, we need to preprocess the CSV to convert arrays to strings
    with conn.cursor() as cursor:
        # MySQLdb requires slightly different syntax for LOAD DATA LOCAL INFILE
        load_data_sql = f"""
        LOAD DATA LOCAL INFILE %s
        INTO TABLE nodes
        FIELDS TERMINATED BY ';'
        LINES TERMINATED BY '\\n'
        IGNORE 1 LINES
        """
        
        cursor.execute(load_data_sql, (csv_file_path,))#
        create_index(conn, "nodes", "id")
        
        # Load edges
        cursor.execute(
            "LOAD DATA LOCAL INFILE %s INTO TABLE edges FIELDS TERMINATED BY ',' LINES TERMINATED BY '\\n' IGNORE 1 LINES",
            (f"syn_data/{edge_file_name}",)
        )
        create_index(conn, "edges", "target_id")
        conn.commit()
    
    creation_time = time.time() - start
    return creation_time

def read(conn, hops, X_and_y, X, y, edge_index, random_sample_size = 1_000):
    np.random.seed(42)
    seed_node_ids = np.random.choice(np.arange(X_and_y.shape[0]), size = random_sample_size, replace = False)
    
    with conn.cursor() as cursor:
        cursor.execute("SET SESSION group_concat_max_len = 86777215;")
        cursor.execute("SET GLOBAL max_allowed_packet = 8073741824;")  # 1GB

        complete_time = 0
        complete_test_time = 0
        
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
            INNER JOIN NestedTargets nt ON e.target_id = nt.source_id
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
        )
        
        SELECT
        (SELECT JSON_ARRAYAGG(X) FROM node_data) AS node_table,
        (SELECT JSON_ARRAYAGG(y) FROM node_data) AS label_table,
        (SELECT JSON_ARRAYAGG(JSON_ARRAY(source_id, target_id))
         FROM (SELECT DISTINCT source_id, target_id FROM NestedTargets) AS edges) AS edge_table,
         (SELECT JSON_ARRAYAGG(id) FROM node_data) AS node_ids;
    """)
                results = cursor.fetchall()[0]
                if None in results:
                    continue
                labels = np.array(json.loads(results[1]))
                subgraph_node_features = np.array(json.loads(results[0]))
                if results[0] is None:
                    continue
                
                subgraph_edges = np.array(json.loads(results[2])).transpose()
                
                node_ids = np.array(json.loads(results[-1]))
                ##TODO change in other files
                id_sort_idx = np.argsort(node_ids)
                node_ids = node_ids[id_sort_idx]
                features = subgraph_node_features[id_sort_idx]
                labels = labels[id_sort_idx]
                # _, cols_source = np.nonzero((subgraph_edges[0] == node_ids[:, None]).transpose())
                # _, cols_target = np.nonzero((subgraph_edges[1] == node_ids[:, None]).transpose())
                ##TODO change in other files
                cols_source = np.searchsorted(node_ids, subgraph_edges[0])
                cols_target = np.searchsorted(node_ids, subgraph_edges[1])
                remapped_edge_index = np.concatenate([np.expand_dims(cols_source, axis = 0), np.expand_dims(cols_target, axis = 0)], axis = 0)
                overall_run_time = time.time() - start 
                
                complete_time += overall_run_time
                # Testing
                test_time = time.time()
                remapped_edge_index_test, features_test, labels_test, unique_node_ids = get_subgraph_from_in_mem_graph_optimized(X, y, seed_node_id, edge_index, hops)                    
                complete_test_time += time.time() - test_time

                assert (sort_edge_index(torch.from_numpy(remapped_edge_index_test)) == sort_edge_index(torch.from_numpy(remapped_edge_index))).sum() / (remapped_edge_index_test.shape[-1] * remapped_edge_index_test.shape[0]), "Edges doesnt match"
                assert np.allclose(node_ids, unique_node_ids), "Node ids does not match"
                assert np.allclose(features.shape, features_test.shape), "features does not match"
                assert np.allclose(features, features_test), "features does not match"
                # assert np.allclose(labels_test, labels), "Labels does not match"
                # print(f"Fetched {remapped_edge_index.shape} edges, {labels.shape} labels, {features.shape} features in ({overall_run_time} s)")
            except Exception as e:
                conn.rollback()
                print(f"Error reading data: {e}")
                raise   
    return (complete_time, complete_test_time)

def update_nodes(conn, X_and_y, X, y, random_sample_size = 1000):
    with conn.cursor() as cursor:
        np.random.seed(42)
        node_ids = np.random.choice(np.arange(X_and_y.shape[0]), size = random_sample_size, replace = False).tolist()
        start = time.time()
        for node_id in tqdm(node_ids):
            np.random.seed(42)
            features = np.random.rand(X.shape[-1]).tolist()  # Random values between 0 and 1
            labels = np.random.randint(0, 2, size=y.shape[-1]).tolist() 
            sql_query = f"""
            UPDATE nodes 
            SET X = '%s', y = '%s'
            WHERE id = %s;
            """
            values = (features, labels, node_id)
            cursor.execute(sql_query % values)
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

def delete_database(conn, db_name):
    """Delete the specified database including all its schemas, tables, and indexes."""
    try:
        conn.autocommit = True
        with conn.cursor() as cursor:
            cursor.execute(f"DROP DATABASE IF EXISTS {db_name};")
            print(f"Database '{db_name}' deleted successfully.")
    except Exception as e:
        print(f"Error deleting database: {e}")
        raise
    finally:
        conn.autocommit = False


def delete(conn, new_db_name):
    start = time.time()
    if conn is not None:
        conn.close()
    conn = connect_to_mysql()
    delete_database(conn, new_db_name)
    conn.close()
    return time.time() - start

def eval_ppi(output_df):
    edge_file_name = "ppi_edge_index.csv"
    node_file_name = "ppi.csv"
    X = pd.read_csv(f"data/ppi_x.csv")
    y = pd.read_csv(f"data/ppi_y.csv")
    edges = pd.read_csv("data/" + edge_file_name)
    edges.columns = ["source_id", "target_id"]
    
    X_and_y = pd.DataFrame()
    X_and_y["y"] = y.apply(lambda row: [int(row[column]) for column in y.columns], axis=1)
    X_and_y["X"] = X.apply(lambda row: [row[column] for column in X.columns], axis=1)
    
    node_file_name = "X_y_ppi_mysql_list.csv" ## Can use the same structure for all database when using column wise import
    X_and_y.to_csv(f"syn_data/{node_file_name}", sep = ";", index = True)
    edges.to_csv(f"syn_data/{edge_file_name}", sep = ",", index = False)
    edge_index = edges.values.transpose(-1, 0)
    conn, db_name = create_database(node_file_name)
    create_time = create(conn, node_file_name, edge_file_name, X_and_y)
    read_times =dict()
    read_times_mem =dict()
    for hops in range(1,4):
        read_time, read_time_mem = read(conn, hops, X_and_y, X, y, edge_index, random_sample_size = 1_000)
        read_times_mem[hops] = read_time_mem
        read_times[hops] = read_time
    update_node_time = update_nodes(conn, X_and_y, X, y, 1_000)
    update_edge_time = update_edges(conn, edge_index, X_and_y, 1_000)
    delete_time= delete(conn,db_name )
    
    new_row_dict = {"name": "PPI", "create": create_time, "update_nodes": update_node_time, "update_edges": update_edge_time, "delete": delete_time}
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
            node_file_name = f"X_and_y_{str(num_nodes)}_nodes_{num_edges}_mysql_list.csv"
            if True or not os.path.exists(f"syn_data/{node_file_name}"):
                X_and_y = pd.DataFrame()
                X_and_y["y"] = y.apply(lambda row: [int(row[column]) for column in y.columns], axis=1)
                X_and_y["X"] = X.apply(lambda row: [row[column] for column in X.columns], axis=1)
                X_and_y.to_csv(f"syn_data/{node_file_name}", sep = ";", index = True)
            else:
                X_and_y = pd.read_csv(f"syn_data/{node_file_name}", sep = ";", index_col = 0)
            conn, db_name = create_database(node_file_name)
            create_time = create(conn, node_file_name, edge_file_name, X_and_y)
            read_times = dict()
            read_times_mem = dict()
            for hops in tqdm(range(1, 4)):
                read_time, read_time_mem = read(conn, hops, X_and_y, X, y, edge_index, random_sample_size = 1_000)
                read_times[hops] = read_time
                read_times_mem[hops] = read_time_mem
            update_time_nodes = update_nodes(conn, X_and_y,  X, y, 1_000)
            update_time_edges = update_edges(conn, edge_index, X_and_y, 1_000)
            delete_time = delete(conn, db_name)
            new_row_dict = {"name": f"{str(num_nodes)}_nodes_{num_edges}", "create": create_time, "update_nodes": update_time_nodes, "update_edges": update_time_edges, "delete": delete_time}
            for hops in read_times:
                new_row_dict[f"read_{hops}"] = read_times[hops]
                new_row_dict[f"read_in_mem_{hops}"] = read_times_mem[hops]
            new_row = pd.DataFrame([new_row_dict])
            output_df = pd.concat((output_df, new_row), ignore_index=True)
    return output_df

num_iterations = 10
off_set = 0
for i in range(off_set, num_iterations + off_set):
    print(f"Iteration {i}")
    output_df = pd.DataFrame(columns = ["name", "create", "update_nodes", "update_edges", "delete"])
    output_df = eval_ppi(output_df)
    output_df = eval_synth(output_df)
    output_df.to_csv(f"mysql_list_{i}.csv")