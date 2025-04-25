import pandas as pd
from CRUD import CRUD_Evaluator
from tqdm import tqdm
from perun import monitor

datasets = ["ppi", "1000_5", "1000_10", "1000_20", "1000_SF", "10000_5", "10000_10", "10000_20", "10000_SF", "100000_5", "100000_10", "100000_20", "100000_SF", "1000000_5", "1000000_SF"]

# datasets = ["1000_5"]

class DBMSEvaluator:
    def __init__(self, Dbms_evaluator_class):
        self.output_df = pd.DataFrame(columns = ["name", "create", "update_nodes", "update_edges", "delete"])
        self.Dbms_evaluator_class = Dbms_evaluator_class

    @monitor()
    def neo4j_col_ppi_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def neo4j_col_ppi_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_ppi_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_ppi_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_ppi_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def neo4j_col_ppi_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def neo4j_col_ppi_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def neo4j_col_1000_5_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def neo4j_col_1000_5_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_1000_5_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_1000_5_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_1000_5_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def neo4j_col_1000_5_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def neo4j_col_1000_5_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def neo4j_col_1000_10_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def neo4j_col_1000_10_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_1000_10_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_1000_10_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_1000_10_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def neo4j_col_1000_10_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def neo4j_col_1000_10_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def neo4j_col_1000_20_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def neo4j_col_1000_20_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_1000_20_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_1000_20_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_1000_20_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def neo4j_col_1000_20_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def neo4j_col_1000_20_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def neo4j_col_1000_SF_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def neo4j_col_1000_SF_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_1000_SF_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_1000_SF_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_1000_SF_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def neo4j_col_1000_SF_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def neo4j_col_1000_SF_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def neo4j_col_10000_5_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def neo4j_col_10000_5_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_10000_5_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_10000_5_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_10000_5_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def neo4j_col_10000_5_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def neo4j_col_10000_5_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def neo4j_col_10000_10_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def neo4j_col_10000_10_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_10000_10_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_10000_10_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_10000_10_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def neo4j_col_10000_10_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def neo4j_col_10000_10_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def neo4j_col_10000_20_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def neo4j_col_10000_20_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_10000_20_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_10000_20_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_10000_20_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def neo4j_col_10000_20_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def neo4j_col_10000_20_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def neo4j_col_10000_SF_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def neo4j_col_10000_SF_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_10000_SF_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_10000_SF_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_10000_SF_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def neo4j_col_10000_SF_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def neo4j_col_10000_SF_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def neo4j_col_100000_5_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def neo4j_col_100000_5_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_100000_5_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_100000_5_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_100000_5_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def neo4j_col_100000_5_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def neo4j_col_100000_5_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def neo4j_col_100000_10_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def neo4j_col_100000_10_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_100000_10_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_100000_10_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_100000_10_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def neo4j_col_100000_10_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def neo4j_col_100000_10_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def neo4j_col_100000_20_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def neo4j_col_100000_20_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_100000_20_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_100000_20_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_100000_20_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def neo4j_col_100000_20_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def neo4j_col_100000_20_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def neo4j_col_100000_SF_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def neo4j_col_100000_SF_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_100000_SF_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_100000_SF_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_100000_SF_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def neo4j_col_100000_SF_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def neo4j_col_100000_SF_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def neo4j_col_1000000_5_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def neo4j_col_1000000_5_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_1000000_5_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_1000000_5_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_1000000_5_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def neo4j_col_1000000_5_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def neo4j_col_1000000_5_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def neo4j_col_1000000_SF_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def neo4j_col_1000000_SF_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_1000000_SF_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_1000000_SF_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_col_1000000_SF_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def neo4j_col_1000000_SF_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def neo4j_col_1000000_SF_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def neo4j_list_ppi_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def neo4j_list_ppi_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_ppi_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_ppi_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_ppi_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def neo4j_list_ppi_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def neo4j_list_ppi_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def neo4j_list_1000_5_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def neo4j_list_1000_5_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_1000_5_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_1000_5_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_1000_5_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def neo4j_list_1000_5_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def neo4j_list_1000_5_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def neo4j_list_1000_10_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def neo4j_list_1000_10_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_1000_10_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_1000_10_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_1000_10_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def neo4j_list_1000_10_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def neo4j_list_1000_10_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def neo4j_list_1000_20_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def neo4j_list_1000_20_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_1000_20_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_1000_20_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_1000_20_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def neo4j_list_1000_20_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def neo4j_list_1000_20_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def neo4j_list_1000_SF_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def neo4j_list_1000_SF_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_1000_SF_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_1000_SF_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_1000_SF_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def neo4j_list_1000_SF_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def neo4j_list_1000_SF_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def neo4j_list_10000_5_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def neo4j_list_10000_5_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_10000_5_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_10000_5_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_10000_5_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def neo4j_list_10000_5_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def neo4j_list_10000_5_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def neo4j_list_10000_10_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def neo4j_list_10000_10_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_10000_10_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_10000_10_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_10000_10_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def neo4j_list_10000_10_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def neo4j_list_10000_10_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def neo4j_list_10000_20_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def neo4j_list_10000_20_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_10000_20_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_10000_20_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_10000_20_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def neo4j_list_10000_20_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def neo4j_list_10000_20_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def neo4j_list_10000_SF_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def neo4j_list_10000_SF_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_10000_SF_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_10000_SF_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_10000_SF_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def neo4j_list_10000_SF_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def neo4j_list_10000_SF_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def neo4j_list_100000_5_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def neo4j_list_100000_5_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_100000_5_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_100000_5_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_100000_5_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def neo4j_list_100000_5_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def neo4j_list_100000_5_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def neo4j_list_100000_10_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def neo4j_list_100000_10_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_100000_10_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_100000_10_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_100000_10_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def neo4j_list_100000_10_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def neo4j_list_100000_10_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def neo4j_list_100000_20_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def neo4j_list_100000_20_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_100000_20_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_100000_20_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_100000_20_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def neo4j_list_100000_20_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def neo4j_list_100000_20_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def neo4j_list_100000_SF_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def neo4j_list_100000_SF_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_100000_SF_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_100000_SF_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_100000_SF_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def neo4j_list_100000_SF_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def neo4j_list_100000_SF_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def neo4j_list_1000000_5_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def neo4j_list_1000000_5_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_1000000_5_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_1000000_5_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_1000000_5_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def neo4j_list_1000000_5_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def neo4j_list_1000000_5_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def neo4j_list_1000000_SF_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def neo4j_list_1000000_SF_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_1000000_SF_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_1000000_SF_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def neo4j_list_1000000_SF_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def neo4j_list_1000000_SF_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def neo4j_list_1000000_SF_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def mysql_col_ppi_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def mysql_col_ppi_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_ppi_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_ppi_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_ppi_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def mysql_col_ppi_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def mysql_col_ppi_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def mysql_col_1000_5_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def mysql_col_1000_5_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_1000_5_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_1000_5_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_1000_5_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def mysql_col_1000_5_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def mysql_col_1000_5_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def mysql_col_1000_10_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def mysql_col_1000_10_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_1000_10_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_1000_10_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_1000_10_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def mysql_col_1000_10_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def mysql_col_1000_10_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def mysql_col_1000_20_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def mysql_col_1000_20_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_1000_20_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_1000_20_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_1000_20_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def mysql_col_1000_20_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def mysql_col_1000_20_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def mysql_col_1000_SF_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def mysql_col_1000_SF_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_1000_SF_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_1000_SF_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_1000_SF_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def mysql_col_1000_SF_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def mysql_col_1000_SF_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def mysql_col_10000_5_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def mysql_col_10000_5_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_10000_5_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_10000_5_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_10000_5_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def mysql_col_10000_5_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def mysql_col_10000_5_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def mysql_col_10000_10_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def mysql_col_10000_10_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_10000_10_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_10000_10_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_10000_10_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def mysql_col_10000_10_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def mysql_col_10000_10_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def mysql_col_10000_20_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def mysql_col_10000_20_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_10000_20_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_10000_20_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_10000_20_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def mysql_col_10000_20_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def mysql_col_10000_20_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def mysql_col_10000_SF_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def mysql_col_10000_SF_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_10000_SF_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_10000_SF_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_10000_SF_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def mysql_col_10000_SF_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def mysql_col_10000_SF_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def mysql_col_100000_5_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def mysql_col_100000_5_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_100000_5_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_100000_5_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_100000_5_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def mysql_col_100000_5_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def mysql_col_100000_5_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def mysql_col_100000_10_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def mysql_col_100000_10_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_100000_10_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_100000_10_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_100000_10_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def mysql_col_100000_10_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def mysql_col_100000_10_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def mysql_col_100000_20_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def mysql_col_100000_20_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_100000_20_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_100000_20_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_100000_20_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def mysql_col_100000_20_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def mysql_col_100000_20_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def mysql_col_100000_SF_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def mysql_col_100000_SF_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_100000_SF_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_100000_SF_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_100000_SF_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def mysql_col_100000_SF_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def mysql_col_100000_SF_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def mysql_col_1000000_5_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def mysql_col_1000000_5_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_1000000_5_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_1000000_5_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_1000000_5_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def mysql_col_1000000_5_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def mysql_col_1000000_5_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def mysql_col_1000000_SF_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def mysql_col_1000000_SF_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_1000000_SF_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_1000000_SF_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_col_1000000_SF_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def mysql_col_1000000_SF_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def mysql_col_1000000_SF_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def mysql_list_ppi_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def mysql_list_ppi_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_ppi_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_ppi_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_ppi_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def mysql_list_ppi_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def mysql_list_ppi_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def mysql_list_1000_5_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def mysql_list_1000_5_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_1000_5_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_1000_5_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_1000_5_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def mysql_list_1000_5_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def mysql_list_1000_5_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def mysql_list_1000_10_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def mysql_list_1000_10_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_1000_10_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_1000_10_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_1000_10_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def mysql_list_1000_10_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def mysql_list_1000_10_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def mysql_list_1000_20_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def mysql_list_1000_20_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_1000_20_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_1000_20_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_1000_20_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def mysql_list_1000_20_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def mysql_list_1000_20_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def mysql_list_1000_SF_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def mysql_list_1000_SF_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_1000_SF_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_1000_SF_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_1000_SF_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def mysql_list_1000_SF_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def mysql_list_1000_SF_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def mysql_list_10000_5_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def mysql_list_10000_5_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_10000_5_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_10000_5_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_10000_5_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def mysql_list_10000_5_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def mysql_list_10000_5_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def mysql_list_10000_10_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def mysql_list_10000_10_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_10000_10_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_10000_10_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_10000_10_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def mysql_list_10000_10_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def mysql_list_10000_10_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def mysql_list_10000_20_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def mysql_list_10000_20_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_10000_20_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_10000_20_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_10000_20_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def mysql_list_10000_20_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def mysql_list_10000_20_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def mysql_list_10000_SF_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def mysql_list_10000_SF_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_10000_SF_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_10000_SF_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_10000_SF_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def mysql_list_10000_SF_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def mysql_list_10000_SF_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def mysql_list_100000_5_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def mysql_list_100000_5_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_100000_5_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_100000_5_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_100000_5_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def mysql_list_100000_5_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def mysql_list_100000_5_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def mysql_list_100000_10_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def mysql_list_100000_10_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_100000_10_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_100000_10_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_100000_10_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def mysql_list_100000_10_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def mysql_list_100000_10_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def mysql_list_100000_20_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def mysql_list_100000_20_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_100000_20_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_100000_20_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_100000_20_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def mysql_list_100000_20_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def mysql_list_100000_20_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def mysql_list_100000_SF_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def mysql_list_100000_SF_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_100000_SF_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_100000_SF_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_100000_SF_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def mysql_list_100000_SF_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def mysql_list_100000_SF_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def mysql_list_1000000_5_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def mysql_list_1000000_5_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_1000000_5_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_1000000_5_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_1000000_5_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def mysql_list_1000000_5_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def mysql_list_1000000_5_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def mysql_list_1000000_SF_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def mysql_list_1000000_SF_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_1000000_SF_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_1000000_SF_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def mysql_list_1000000_SF_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def mysql_list_1000000_SF_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def mysql_list_1000000_SF_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def postgres_col_ppi_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def postgres_col_ppi_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_ppi_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_ppi_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_ppi_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def postgres_col_ppi_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def postgres_col_ppi_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def postgres_col_1000_5_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def postgres_col_1000_5_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_1000_5_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_1000_5_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_1000_5_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def postgres_col_1000_5_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def postgres_col_1000_5_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def postgres_col_1000_10_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def postgres_col_1000_10_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_1000_10_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_1000_10_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_1000_10_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def postgres_col_1000_10_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def postgres_col_1000_10_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def postgres_col_1000_20_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def postgres_col_1000_20_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_1000_20_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_1000_20_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_1000_20_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def postgres_col_1000_20_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def postgres_col_1000_20_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def postgres_col_1000_SF_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def postgres_col_1000_SF_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_1000_SF_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_1000_SF_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_1000_SF_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def postgres_col_1000_SF_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def postgres_col_1000_SF_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def postgres_col_10000_5_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def postgres_col_10000_5_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_10000_5_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_10000_5_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_10000_5_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def postgres_col_10000_5_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def postgres_col_10000_5_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def postgres_col_10000_10_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def postgres_col_10000_10_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_10000_10_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_10000_10_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_10000_10_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def postgres_col_10000_10_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def postgres_col_10000_10_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def postgres_col_10000_20_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def postgres_col_10000_20_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_10000_20_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_10000_20_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_10000_20_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def postgres_col_10000_20_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def postgres_col_10000_20_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def postgres_col_10000_SF_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def postgres_col_10000_SF_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_10000_SF_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_10000_SF_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_10000_SF_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def postgres_col_10000_SF_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def postgres_col_10000_SF_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def postgres_col_100000_5_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def postgres_col_100000_5_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_100000_5_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_100000_5_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_100000_5_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def postgres_col_100000_5_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def postgres_col_100000_5_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def postgres_col_100000_10_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def postgres_col_100000_10_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_100000_10_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_100000_10_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_100000_10_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def postgres_col_100000_10_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def postgres_col_100000_10_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def postgres_col_100000_20_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def postgres_col_100000_20_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_100000_20_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_100000_20_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_100000_20_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def postgres_col_100000_20_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def postgres_col_100000_20_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def postgres_col_100000_SF_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def postgres_col_100000_SF_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_100000_SF_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_100000_SF_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_100000_SF_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def postgres_col_100000_SF_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def postgres_col_100000_SF_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def postgres_col_1000000_5_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def postgres_col_1000000_5_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_1000000_5_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_1000000_5_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_1000000_5_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def postgres_col_1000000_5_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def postgres_col_1000000_5_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def postgres_col_1000000_SF_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def postgres_col_1000000_SF_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_1000000_SF_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_1000000_SF_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_col_1000000_SF_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def postgres_col_1000000_SF_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def postgres_col_1000000_SF_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def postgres_list_ppi_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def postgres_list_ppi_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_ppi_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_ppi_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_ppi_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def postgres_list_ppi_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def postgres_list_ppi_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def postgres_list_1000_5_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def postgres_list_1000_5_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_1000_5_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_1000_5_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_1000_5_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def postgres_list_1000_5_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def postgres_list_1000_5_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def postgres_list_1000_10_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def postgres_list_1000_10_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_1000_10_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_1000_10_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_1000_10_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def postgres_list_1000_10_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def postgres_list_1000_10_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def postgres_list_1000_20_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def postgres_list_1000_20_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_1000_20_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_1000_20_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_1000_20_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def postgres_list_1000_20_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def postgres_list_1000_20_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def postgres_list_1000_SF_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def postgres_list_1000_SF_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_1000_SF_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_1000_SF_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_1000_SF_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def postgres_list_1000_SF_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def postgres_list_1000_SF_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def postgres_list_10000_5_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def postgres_list_10000_5_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_10000_5_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_10000_5_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_10000_5_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def postgres_list_10000_5_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def postgres_list_10000_5_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def postgres_list_10000_10_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def postgres_list_10000_10_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_10000_10_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_10000_10_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_10000_10_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def postgres_list_10000_10_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def postgres_list_10000_10_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def postgres_list_10000_20_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def postgres_list_10000_20_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_10000_20_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_10000_20_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_10000_20_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def postgres_list_10000_20_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def postgres_list_10000_20_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def postgres_list_10000_SF_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def postgres_list_10000_SF_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_10000_SF_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_10000_SF_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_10000_SF_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def postgres_list_10000_SF_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def postgres_list_10000_SF_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def postgres_list_100000_5_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def postgres_list_100000_5_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_100000_5_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_100000_5_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_100000_5_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def postgres_list_100000_5_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def postgres_list_100000_5_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def postgres_list_100000_10_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def postgres_list_100000_10_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_100000_10_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_100000_10_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_100000_10_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def postgres_list_100000_10_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def postgres_list_100000_10_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def postgres_list_100000_20_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def postgres_list_100000_20_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_100000_20_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_100000_20_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_100000_20_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def postgres_list_100000_20_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def postgres_list_100000_20_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def postgres_list_100000_SF_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def postgres_list_100000_SF_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_100000_SF_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_100000_SF_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_100000_SF_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def postgres_list_100000_SF_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def postgres_list_100000_SF_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def postgres_list_1000000_5_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def postgres_list_1000000_5_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_1000000_5_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_1000000_5_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_1000000_5_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def postgres_list_1000000_5_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def postgres_list_1000000_5_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @monitor()
    def postgres_list_1000000_SF_create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @monitor()
    def postgres_list_1000000_SF_read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_1000000_SF_read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_1000000_SF_read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @monitor()
    def postgres_list_1000000_SF_update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @monitor()
    def postgres_list_1000000_SF_update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @monitor()
    def postgres_list_1000000_SF_delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

    def eval(self):
        for dataset_name in datasets:
            num_nodes = 0 if "_" not in dataset_name else int(dataset_name.split("_")[0])
            num_edges_str = "unknown" if "_" not in dataset_name else dataset_name.split("_")[-1]
            if num_edges_str == "SF":
                num_edges_str = "scale_free"
            else: 
                num_edges_str += "_edges"
            dataset_df_row_name = dataset_name.upper() if "_" not in dataset_name else f"{str(num_nodes)}_nodes_{num_edges_str}"
            X_name =  "ppi_x.csv" if "_" not in dataset_name else f"X_{str(num_nodes)}_nodes_{num_edges_str}.csv"
            y_name =  "ppi_y.csv" if "_" not in dataset_name else f"y_{str(num_nodes)}_nodes_{num_edges_str}.csv"
            edge_index_name =  "ppi_edge_index.csv" if "_" not in dataset_name else f"edge_index_{str(num_nodes)}_nodes_{num_edges_str}.csv"
            X_y_name =  f"X_y_ppi_{self.Dbms_evaluator_class.file_suffix()}.csv" if "_" not in dataset_name else f"X_and_y_{str(num_nodes)}_nodes_{num_edges_str}_{self.Dbms_evaluator_class.file_suffix()}.csv"
            
            crud_evaluator = CRUD_Evaluator(self.Dbms_evaluator_class, X_name, y_name, edge_index_name, X_y_name) 
            create_time, read_times, read_times_mem, update_node_time, update_edge_time, delete_time = None, None, None, None, None, None

            if "col" in self.Dbms_evaluator_class.file_suffix() and "neo4j" in self.Dbms_evaluator_class.db_name() and "ppi" == dataset_name:
                create_time = self.neo4j_col_ppi_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.neo4j_col_ppi_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.neo4j_col_ppi_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.neo4j_col_ppi_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.neo4j_col_ppi_update_nodes(crud_evaluator)
                update_edge_time = self.neo4j_col_ppi_update_edges(crud_evaluator)
                delete_time = self.neo4j_col_ppi_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "neo4j" in self.Dbms_evaluator_class.db_name() and "1000_5" == dataset_name:
                create_time = self.neo4j_col_1000_5_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.neo4j_col_1000_5_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.neo4j_col_1000_5_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.neo4j_col_1000_5_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.neo4j_col_1000_5_update_nodes(crud_evaluator)
                update_edge_time = self.neo4j_col_1000_5_update_edges(crud_evaluator)
                delete_time = self.neo4j_col_1000_5_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "neo4j" in self.Dbms_evaluator_class.db_name() and "1000_10" == dataset_name:
                create_time = self.neo4j_col_1000_10_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.neo4j_col_1000_10_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.neo4j_col_1000_10_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.neo4j_col_1000_10_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.neo4j_col_1000_10_update_nodes(crud_evaluator)
                update_edge_time = self.neo4j_col_1000_10_update_edges(crud_evaluator)
                delete_time = self.neo4j_col_1000_10_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "neo4j" in self.Dbms_evaluator_class.db_name() and "1000_20" == dataset_name:
                create_time = self.neo4j_col_1000_20_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.neo4j_col_1000_20_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.neo4j_col_1000_20_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.neo4j_col_1000_20_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.neo4j_col_1000_20_update_nodes(crud_evaluator)
                update_edge_time = self.neo4j_col_1000_20_update_edges(crud_evaluator)
                delete_time = self.neo4j_col_1000_20_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "neo4j" in self.Dbms_evaluator_class.db_name() and "1000_SF" == dataset_name:
                create_time = self.neo4j_col_1000_SF_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.neo4j_col_1000_SF_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.neo4j_col_1000_SF_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.neo4j_col_1000_SF_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.neo4j_col_1000_SF_update_nodes(crud_evaluator)
                update_edge_time = self.neo4j_col_1000_SF_update_edges(crud_evaluator)
                delete_time = self.neo4j_col_1000_SF_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "neo4j" in self.Dbms_evaluator_class.db_name() and "10000_5" == dataset_name:
                create_time = self.neo4j_col_10000_5_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.neo4j_col_10000_5_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.neo4j_col_10000_5_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.neo4j_col_10000_5_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.neo4j_col_10000_5_update_nodes(crud_evaluator)
                update_edge_time = self.neo4j_col_10000_5_update_edges(crud_evaluator)
                delete_time = self.neo4j_col_10000_5_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "neo4j" in self.Dbms_evaluator_class.db_name() and "10000_10" == dataset_name:
                create_time = self.neo4j_col_10000_10_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.neo4j_col_10000_10_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.neo4j_col_10000_10_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.neo4j_col_10000_10_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.neo4j_col_10000_10_update_nodes(crud_evaluator)
                update_edge_time = self.neo4j_col_10000_10_update_edges(crud_evaluator)
                delete_time = self.neo4j_col_10000_10_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "neo4j" in self.Dbms_evaluator_class.db_name() and "10000_20" == dataset_name:
                create_time = self.neo4j_col_10000_20_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.neo4j_col_10000_20_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.neo4j_col_10000_20_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.neo4j_col_10000_20_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.neo4j_col_10000_20_update_nodes(crud_evaluator)
                update_edge_time = self.neo4j_col_10000_20_update_edges(crud_evaluator)
                delete_time = self.neo4j_col_10000_20_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "neo4j" in self.Dbms_evaluator_class.db_name() and "10000_SF" == dataset_name:
                create_time = self.neo4j_col_10000_SF_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.neo4j_col_10000_SF_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.neo4j_col_10000_SF_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.neo4j_col_10000_SF_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.neo4j_col_10000_SF_update_nodes(crud_evaluator)
                update_edge_time = self.neo4j_col_10000_SF_update_edges(crud_evaluator)
                delete_time = self.neo4j_col_10000_SF_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "neo4j" in self.Dbms_evaluator_class.db_name() and "100000_5" == dataset_name:
                create_time = self.neo4j_col_100000_5_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.neo4j_col_100000_5_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.neo4j_col_100000_5_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.neo4j_col_100000_5_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.neo4j_col_100000_5_update_nodes(crud_evaluator)
                update_edge_time = self.neo4j_col_100000_5_update_edges(crud_evaluator)
                delete_time = self.neo4j_col_100000_5_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "neo4j" in self.Dbms_evaluator_class.db_name() and "100000_10" == dataset_name:
                create_time = self.neo4j_col_100000_10_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.neo4j_col_100000_10_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.neo4j_col_100000_10_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.neo4j_col_100000_10_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.neo4j_col_100000_10_update_nodes(crud_evaluator)
                update_edge_time = self.neo4j_col_100000_10_update_edges(crud_evaluator)
                delete_time = self.neo4j_col_100000_10_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "neo4j" in self.Dbms_evaluator_class.db_name() and "100000_20" == dataset_name:
                create_time = self.neo4j_col_100000_20_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.neo4j_col_100000_20_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.neo4j_col_100000_20_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.neo4j_col_100000_20_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.neo4j_col_100000_20_update_nodes(crud_evaluator)
                update_edge_time = self.neo4j_col_100000_20_update_edges(crud_evaluator)
                delete_time = self.neo4j_col_100000_20_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "neo4j" in self.Dbms_evaluator_class.db_name() and "100000_SF" == dataset_name:
                create_time = self.neo4j_col_100000_SF_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.neo4j_col_100000_SF_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.neo4j_col_100000_SF_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.neo4j_col_100000_SF_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.neo4j_col_100000_SF_update_nodes(crud_evaluator)
                update_edge_time = self.neo4j_col_100000_SF_update_edges(crud_evaluator)
                delete_time = self.neo4j_col_100000_SF_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "neo4j" in self.Dbms_evaluator_class.db_name() and "1000000_5" == dataset_name:
                create_time = self.neo4j_col_1000000_5_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.neo4j_col_1000000_5_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.neo4j_col_1000000_5_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.neo4j_col_1000000_5_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.neo4j_col_1000000_5_update_nodes(crud_evaluator)
                update_edge_time = self.neo4j_col_1000000_5_update_edges(crud_evaluator)
                delete_time = self.neo4j_col_1000000_5_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "neo4j" in self.Dbms_evaluator_class.db_name() and "1000000_SF" == dataset_name:
                create_time = self.neo4j_col_1000000_SF_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.neo4j_col_1000000_SF_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.neo4j_col_1000000_SF_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.neo4j_col_1000000_SF_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.neo4j_col_1000000_SF_update_nodes(crud_evaluator)
                update_edge_time = self.neo4j_col_1000000_SF_update_edges(crud_evaluator)
                delete_time = self.neo4j_col_1000000_SF_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "neo4j" in self.Dbms_evaluator_class.db_name() and "ppi" == dataset_name:
                create_time = self.neo4j_list_ppi_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.neo4j_list_ppi_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.neo4j_list_ppi_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.neo4j_list_ppi_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.neo4j_list_ppi_update_nodes(crud_evaluator)
                update_edge_time = self.neo4j_list_ppi_update_edges(crud_evaluator)
                delete_time = self.neo4j_list_ppi_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "neo4j" in self.Dbms_evaluator_class.db_name() and "1000_5" == dataset_name:
                create_time = self.neo4j_list_1000_5_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.neo4j_list_1000_5_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.neo4j_list_1000_5_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.neo4j_list_1000_5_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.neo4j_list_1000_5_update_nodes(crud_evaluator)
                update_edge_time = self.neo4j_list_1000_5_update_edges(crud_evaluator)
                delete_time = self.neo4j_list_1000_5_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "neo4j" in self.Dbms_evaluator_class.db_name() and "1000_10" == dataset_name:
                create_time = self.neo4j_list_1000_10_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.neo4j_list_1000_10_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.neo4j_list_1000_10_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.neo4j_list_1000_10_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.neo4j_list_1000_10_update_nodes(crud_evaluator)
                update_edge_time = self.neo4j_list_1000_10_update_edges(crud_evaluator)
                delete_time = self.neo4j_list_1000_10_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "neo4j" in self.Dbms_evaluator_class.db_name() and "1000_20" == dataset_name:
                create_time = self.neo4j_list_1000_20_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.neo4j_list_1000_20_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.neo4j_list_1000_20_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.neo4j_list_1000_20_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.neo4j_list_1000_20_update_nodes(crud_evaluator)
                update_edge_time = self.neo4j_list_1000_20_update_edges(crud_evaluator)
                delete_time = self.neo4j_list_1000_20_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "neo4j" in self.Dbms_evaluator_class.db_name() and "1000_SF" == dataset_name:
                create_time = self.neo4j_list_1000_SF_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.neo4j_list_1000_SF_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.neo4j_list_1000_SF_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.neo4j_list_1000_SF_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.neo4j_list_1000_SF_update_nodes(crud_evaluator)
                update_edge_time = self.neo4j_list_1000_SF_update_edges(crud_evaluator)
                delete_time = self.neo4j_list_1000_SF_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "neo4j" in self.Dbms_evaluator_class.db_name() and "10000_5" == dataset_name:
                create_time = self.neo4j_list_10000_5_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.neo4j_list_10000_5_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.neo4j_list_10000_5_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.neo4j_list_10000_5_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.neo4j_list_10000_5_update_nodes(crud_evaluator)
                update_edge_time = self.neo4j_list_10000_5_update_edges(crud_evaluator)
                delete_time = self.neo4j_list_10000_5_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "neo4j" in self.Dbms_evaluator_class.db_name() and "10000_10" == dataset_name:
                create_time = self.neo4j_list_10000_10_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.neo4j_list_10000_10_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.neo4j_list_10000_10_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.neo4j_list_10000_10_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.neo4j_list_10000_10_update_nodes(crud_evaluator)
                update_edge_time = self.neo4j_list_10000_10_update_edges(crud_evaluator)
                delete_time = self.neo4j_list_10000_10_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "neo4j" in self.Dbms_evaluator_class.db_name() and "10000_20" == dataset_name:
                create_time = self.neo4j_list_10000_20_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.neo4j_list_10000_20_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.neo4j_list_10000_20_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.neo4j_list_10000_20_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.neo4j_list_10000_20_update_nodes(crud_evaluator)
                update_edge_time = self.neo4j_list_10000_20_update_edges(crud_evaluator)
                delete_time = self.neo4j_list_10000_20_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "neo4j" in self.Dbms_evaluator_class.db_name() and "10000_SF" == dataset_name:
                create_time = self.neo4j_list_10000_SF_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.neo4j_list_10000_SF_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.neo4j_list_10000_SF_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.neo4j_list_10000_SF_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.neo4j_list_10000_SF_update_nodes(crud_evaluator)
                update_edge_time = self.neo4j_list_10000_SF_update_edges(crud_evaluator)
                delete_time = self.neo4j_list_10000_SF_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "neo4j" in self.Dbms_evaluator_class.db_name() and "100000_5" == dataset_name:
                create_time = self.neo4j_list_100000_5_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.neo4j_list_100000_5_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.neo4j_list_100000_5_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.neo4j_list_100000_5_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.neo4j_list_100000_5_update_nodes(crud_evaluator)
                update_edge_time = self.neo4j_list_100000_5_update_edges(crud_evaluator)
                delete_time = self.neo4j_list_100000_5_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "neo4j" in self.Dbms_evaluator_class.db_name() and "100000_10" == dataset_name:
                create_time = self.neo4j_list_100000_10_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.neo4j_list_100000_10_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.neo4j_list_100000_10_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.neo4j_list_100000_10_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.neo4j_list_100000_10_update_nodes(crud_evaluator)
                update_edge_time = self.neo4j_list_100000_10_update_edges(crud_evaluator)
                delete_time = self.neo4j_list_100000_10_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "neo4j" in self.Dbms_evaluator_class.db_name() and "100000_20" == dataset_name:
                create_time = self.neo4j_list_100000_20_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.neo4j_list_100000_20_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.neo4j_list_100000_20_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.neo4j_list_100000_20_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.neo4j_list_100000_20_update_nodes(crud_evaluator)
                update_edge_time = self.neo4j_list_100000_20_update_edges(crud_evaluator)
                delete_time = self.neo4j_list_100000_20_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "neo4j" in self.Dbms_evaluator_class.db_name() and "100000_SF" == dataset_name:
                create_time = self.neo4j_list_100000_SF_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.neo4j_list_100000_SF_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.neo4j_list_100000_SF_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.neo4j_list_100000_SF_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.neo4j_list_100000_SF_update_nodes(crud_evaluator)
                update_edge_time = self.neo4j_list_100000_SF_update_edges(crud_evaluator)
                delete_time = self.neo4j_list_100000_SF_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "neo4j" in self.Dbms_evaluator_class.db_name() and "1000000_5" == dataset_name:
                create_time = self.neo4j_list_1000000_5_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.neo4j_list_1000000_5_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.neo4j_list_1000000_5_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.neo4j_list_1000000_5_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.neo4j_list_1000000_5_update_nodes(crud_evaluator)
                update_edge_time = self.neo4j_list_1000000_5_update_edges(crud_evaluator)
                delete_time = self.neo4j_list_1000000_5_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "neo4j" in self.Dbms_evaluator_class.db_name() and "1000000_SF" == dataset_name:
                create_time = self.neo4j_list_1000000_SF_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.neo4j_list_1000000_SF_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.neo4j_list_1000000_SF_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.neo4j_list_1000000_SF_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.neo4j_list_1000000_SF_update_nodes(crud_evaluator)
                update_edge_time = self.neo4j_list_1000000_SF_update_edges(crud_evaluator)
                delete_time = self.neo4j_list_1000000_SF_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "mysql" in self.Dbms_evaluator_class.db_name() and "ppi" == dataset_name:
                create_time = self.mysql_col_ppi_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.mysql_col_ppi_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.mysql_col_ppi_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.mysql_col_ppi_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.mysql_col_ppi_update_nodes(crud_evaluator)
                update_edge_time = self.mysql_col_ppi_update_edges(crud_evaluator)
                delete_time = self.mysql_col_ppi_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "mysql" in self.Dbms_evaluator_class.db_name() and "1000_5" == dataset_name:
                create_time = self.mysql_col_1000_5_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.mysql_col_1000_5_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.mysql_col_1000_5_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.mysql_col_1000_5_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.mysql_col_1000_5_update_nodes(crud_evaluator)
                update_edge_time = self.mysql_col_1000_5_update_edges(crud_evaluator)
                delete_time = self.mysql_col_1000_5_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "mysql" in self.Dbms_evaluator_class.db_name() and "1000_10" == dataset_name:
                create_time = self.mysql_col_1000_10_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.mysql_col_1000_10_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.mysql_col_1000_10_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.mysql_col_1000_10_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.mysql_col_1000_10_update_nodes(crud_evaluator)
                update_edge_time = self.mysql_col_1000_10_update_edges(crud_evaluator)
                delete_time = self.mysql_col_1000_10_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "mysql" in self.Dbms_evaluator_class.db_name() and "1000_20" == dataset_name:
                create_time = self.mysql_col_1000_20_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.mysql_col_1000_20_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.mysql_col_1000_20_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.mysql_col_1000_20_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.mysql_col_1000_20_update_nodes(crud_evaluator)
                update_edge_time = self.mysql_col_1000_20_update_edges(crud_evaluator)
                delete_time = self.mysql_col_1000_20_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "mysql" in self.Dbms_evaluator_class.db_name() and "1000_SF" == dataset_name:
                create_time = self.mysql_col_1000_SF_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.mysql_col_1000_SF_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.mysql_col_1000_SF_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.mysql_col_1000_SF_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.mysql_col_1000_SF_update_nodes(crud_evaluator)
                update_edge_time = self.mysql_col_1000_SF_update_edges(crud_evaluator)
                delete_time = self.mysql_col_1000_SF_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "mysql" in self.Dbms_evaluator_class.db_name() and "10000_5" == dataset_name:
                create_time = self.mysql_col_10000_5_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.mysql_col_10000_5_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.mysql_col_10000_5_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.mysql_col_10000_5_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.mysql_col_10000_5_update_nodes(crud_evaluator)
                update_edge_time = self.mysql_col_10000_5_update_edges(crud_evaluator)
                delete_time = self.mysql_col_10000_5_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "mysql" in self.Dbms_evaluator_class.db_name() and "10000_10" == dataset_name:
                create_time = self.mysql_col_10000_10_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.mysql_col_10000_10_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.mysql_col_10000_10_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.mysql_col_10000_10_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.mysql_col_10000_10_update_nodes(crud_evaluator)
                update_edge_time = self.mysql_col_10000_10_update_edges(crud_evaluator)
                delete_time = self.mysql_col_10000_10_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "mysql" in self.Dbms_evaluator_class.db_name() and "10000_20" == dataset_name:
                create_time = self.mysql_col_10000_20_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.mysql_col_10000_20_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.mysql_col_10000_20_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.mysql_col_10000_20_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.mysql_col_10000_20_update_nodes(crud_evaluator)
                update_edge_time = self.mysql_col_10000_20_update_edges(crud_evaluator)
                delete_time = self.mysql_col_10000_20_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "mysql" in self.Dbms_evaluator_class.db_name() and "10000_SF" == dataset_name:
                create_time = self.mysql_col_10000_SF_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.mysql_col_10000_SF_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.mysql_col_10000_SF_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.mysql_col_10000_SF_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.mysql_col_10000_SF_update_nodes(crud_evaluator)
                update_edge_time = self.mysql_col_10000_SF_update_edges(crud_evaluator)
                delete_time = self.mysql_col_10000_SF_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "mysql" in self.Dbms_evaluator_class.db_name() and "100000_5" == dataset_name:
                create_time = self.mysql_col_100000_5_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.mysql_col_100000_5_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.mysql_col_100000_5_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.mysql_col_100000_5_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.mysql_col_100000_5_update_nodes(crud_evaluator)
                update_edge_time = self.mysql_col_100000_5_update_edges(crud_evaluator)
                delete_time = self.mysql_col_100000_5_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "mysql" in self.Dbms_evaluator_class.db_name() and "100000_10" == dataset_name:
                create_time = self.mysql_col_100000_10_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.mysql_col_100000_10_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.mysql_col_100000_10_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.mysql_col_100000_10_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.mysql_col_100000_10_update_nodes(crud_evaluator)
                update_edge_time = self.mysql_col_100000_10_update_edges(crud_evaluator)
                delete_time = self.mysql_col_100000_10_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "mysql" in self.Dbms_evaluator_class.db_name() and "100000_20" == dataset_name:
                create_time = self.mysql_col_100000_20_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.mysql_col_100000_20_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.mysql_col_100000_20_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.mysql_col_100000_20_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.mysql_col_100000_20_update_nodes(crud_evaluator)
                update_edge_time = self.mysql_col_100000_20_update_edges(crud_evaluator)
                delete_time = self.mysql_col_100000_20_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "mysql" in self.Dbms_evaluator_class.db_name() and "100000_SF" == dataset_name:
                create_time = self.mysql_col_100000_SF_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.mysql_col_100000_SF_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.mysql_col_100000_SF_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.mysql_col_100000_SF_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.mysql_col_100000_SF_update_nodes(crud_evaluator)
                update_edge_time = self.mysql_col_100000_SF_update_edges(crud_evaluator)
                delete_time = self.mysql_col_100000_SF_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "mysql" in self.Dbms_evaluator_class.db_name() and "1000000_5" == dataset_name:
                create_time = self.mysql_col_1000000_5_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.mysql_col_1000000_5_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.mysql_col_1000000_5_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.mysql_col_1000000_5_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.mysql_col_1000000_5_update_nodes(crud_evaluator)
                update_edge_time = self.mysql_col_1000000_5_update_edges(crud_evaluator)
                delete_time = self.mysql_col_1000000_5_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "mysql" in self.Dbms_evaluator_class.db_name() and "1000000_SF" == dataset_name:
                create_time = self.mysql_col_1000000_SF_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.mysql_col_1000000_SF_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.mysql_col_1000000_SF_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.mysql_col_1000000_SF_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.mysql_col_1000000_SF_update_nodes(crud_evaluator)
                update_edge_time = self.mysql_col_1000000_SF_update_edges(crud_evaluator)
                delete_time = self.mysql_col_1000000_SF_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "mysql" in self.Dbms_evaluator_class.db_name() and "ppi" == dataset_name:
                create_time = self.mysql_list_ppi_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.mysql_list_ppi_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.mysql_list_ppi_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.mysql_list_ppi_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.mysql_list_ppi_update_nodes(crud_evaluator)
                update_edge_time = self.mysql_list_ppi_update_edges(crud_evaluator)
                delete_time = self.mysql_list_ppi_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "mysql" in self.Dbms_evaluator_class.db_name() and "1000_5" == dataset_name:
                create_time = self.mysql_list_1000_5_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.mysql_list_1000_5_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.mysql_list_1000_5_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.mysql_list_1000_5_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.mysql_list_1000_5_update_nodes(crud_evaluator)
                update_edge_time = self.mysql_list_1000_5_update_edges(crud_evaluator)
                delete_time = self.mysql_list_1000_5_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "mysql" in self.Dbms_evaluator_class.db_name() and "1000_10" == dataset_name:
                create_time = self.mysql_list_1000_10_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.mysql_list_1000_10_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.mysql_list_1000_10_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.mysql_list_1000_10_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.mysql_list_1000_10_update_nodes(crud_evaluator)
                update_edge_time = self.mysql_list_1000_10_update_edges(crud_evaluator)
                delete_time = self.mysql_list_1000_10_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "mysql" in self.Dbms_evaluator_class.db_name() and "1000_20" == dataset_name:
                create_time = self.mysql_list_1000_20_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.mysql_list_1000_20_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.mysql_list_1000_20_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.mysql_list_1000_20_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.mysql_list_1000_20_update_nodes(crud_evaluator)
                update_edge_time = self.mysql_list_1000_20_update_edges(crud_evaluator)
                delete_time = self.mysql_list_1000_20_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "mysql" in self.Dbms_evaluator_class.db_name() and "1000_SF" == dataset_name:
                create_time = self.mysql_list_1000_SF_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.mysql_list_1000_SF_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.mysql_list_1000_SF_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.mysql_list_1000_SF_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.mysql_list_1000_SF_update_nodes(crud_evaluator)
                update_edge_time = self.mysql_list_1000_SF_update_edges(crud_evaluator)
                delete_time = self.mysql_list_1000_SF_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "mysql" in self.Dbms_evaluator_class.db_name() and "10000_5" == dataset_name:
                create_time = self.mysql_list_10000_5_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.mysql_list_10000_5_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.mysql_list_10000_5_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.mysql_list_10000_5_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.mysql_list_10000_5_update_nodes(crud_evaluator)
                update_edge_time = self.mysql_list_10000_5_update_edges(crud_evaluator)
                delete_time = self.mysql_list_10000_5_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "mysql" in self.Dbms_evaluator_class.db_name() and "10000_10" == dataset_name:
                create_time = self.mysql_list_10000_10_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.mysql_list_10000_10_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.mysql_list_10000_10_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.mysql_list_10000_10_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.mysql_list_10000_10_update_nodes(crud_evaluator)
                update_edge_time = self.mysql_list_10000_10_update_edges(crud_evaluator)
                delete_time = self.mysql_list_10000_10_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "mysql" in self.Dbms_evaluator_class.db_name() and "10000_20" == dataset_name:
                create_time = self.mysql_list_10000_20_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.mysql_list_10000_20_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.mysql_list_10000_20_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.mysql_list_10000_20_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.mysql_list_10000_20_update_nodes(crud_evaluator)
                update_edge_time = self.mysql_list_10000_20_update_edges(crud_evaluator)
                delete_time = self.mysql_list_10000_20_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "mysql" in self.Dbms_evaluator_class.db_name() and "10000_SF" == dataset_name:
                create_time = self.mysql_list_10000_SF_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.mysql_list_10000_SF_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.mysql_list_10000_SF_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.mysql_list_10000_SF_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.mysql_list_10000_SF_update_nodes(crud_evaluator)
                update_edge_time = self.mysql_list_10000_SF_update_edges(crud_evaluator)
                delete_time = self.mysql_list_10000_SF_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "mysql" in self.Dbms_evaluator_class.db_name() and "100000_5" == dataset_name:
                create_time = self.mysql_list_100000_5_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.mysql_list_100000_5_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.mysql_list_100000_5_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.mysql_list_100000_5_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.mysql_list_100000_5_update_nodes(crud_evaluator)
                update_edge_time = self.mysql_list_100000_5_update_edges(crud_evaluator)
                delete_time = self.mysql_list_100000_5_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "mysql" in self.Dbms_evaluator_class.db_name() and "100000_10" == dataset_name:
                create_time = self.mysql_list_100000_10_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.mysql_list_100000_10_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.mysql_list_100000_10_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.mysql_list_100000_10_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.mysql_list_100000_10_update_nodes(crud_evaluator)
                update_edge_time = self.mysql_list_100000_10_update_edges(crud_evaluator)
                delete_time = self.mysql_list_100000_10_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "mysql" in self.Dbms_evaluator_class.db_name() and "100000_20" == dataset_name:
                create_time = self.mysql_list_100000_20_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.mysql_list_100000_20_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.mysql_list_100000_20_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.mysql_list_100000_20_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.mysql_list_100000_20_update_nodes(crud_evaluator)
                update_edge_time = self.mysql_list_100000_20_update_edges(crud_evaluator)
                delete_time = self.mysql_list_100000_20_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "mysql" in self.Dbms_evaluator_class.db_name() and "100000_SF" == dataset_name:
                create_time = self.mysql_list_100000_SF_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.mysql_list_100000_SF_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.mysql_list_100000_SF_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.mysql_list_100000_SF_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.mysql_list_100000_SF_update_nodes(crud_evaluator)
                update_edge_time = self.mysql_list_100000_SF_update_edges(crud_evaluator)
                delete_time = self.mysql_list_100000_SF_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "mysql" in self.Dbms_evaluator_class.db_name() and "1000000_5" == dataset_name:
                create_time = self.mysql_list_1000000_5_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.mysql_list_1000000_5_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.mysql_list_1000000_5_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.mysql_list_1000000_5_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.mysql_list_1000000_5_update_nodes(crud_evaluator)
                update_edge_time = self.mysql_list_1000000_5_update_edges(crud_evaluator)
                delete_time = self.mysql_list_1000000_5_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "mysql" in self.Dbms_evaluator_class.db_name() and "1000000_SF" == dataset_name:
                create_time = self.mysql_list_1000000_SF_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.mysql_list_1000000_SF_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.mysql_list_1000000_SF_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.mysql_list_1000000_SF_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.mysql_list_1000000_SF_update_nodes(crud_evaluator)
                update_edge_time = self.mysql_list_1000000_SF_update_edges(crud_evaluator)
                delete_time = self.mysql_list_1000000_SF_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "postgres" in self.Dbms_evaluator_class.db_name() and "ppi" == dataset_name:
                create_time = self.postgres_col_ppi_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.postgres_col_ppi_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.postgres_col_ppi_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.postgres_col_ppi_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.postgres_col_ppi_update_nodes(crud_evaluator)
                update_edge_time = self.postgres_col_ppi_update_edges(crud_evaluator)
                delete_time = self.postgres_col_ppi_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "postgres" in self.Dbms_evaluator_class.db_name() and "1000_5" == dataset_name:
                create_time = self.postgres_col_1000_5_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.postgres_col_1000_5_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.postgres_col_1000_5_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.postgres_col_1000_5_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.postgres_col_1000_5_update_nodes(crud_evaluator)
                update_edge_time = self.postgres_col_1000_5_update_edges(crud_evaluator)
                delete_time = self.postgres_col_1000_5_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "postgres" in self.Dbms_evaluator_class.db_name() and "1000_10" == dataset_name:
                create_time = self.postgres_col_1000_10_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.postgres_col_1000_10_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.postgres_col_1000_10_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.postgres_col_1000_10_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.postgres_col_1000_10_update_nodes(crud_evaluator)
                update_edge_time = self.postgres_col_1000_10_update_edges(crud_evaluator)
                delete_time = self.postgres_col_1000_10_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "postgres" in self.Dbms_evaluator_class.db_name() and "1000_20" == dataset_name:
                create_time = self.postgres_col_1000_20_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.postgres_col_1000_20_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.postgres_col_1000_20_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.postgres_col_1000_20_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.postgres_col_1000_20_update_nodes(crud_evaluator)
                update_edge_time = self.postgres_col_1000_20_update_edges(crud_evaluator)
                delete_time = self.postgres_col_1000_20_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "postgres" in self.Dbms_evaluator_class.db_name() and "1000_SF" == dataset_name:
                create_time = self.postgres_col_1000_SF_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.postgres_col_1000_SF_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.postgres_col_1000_SF_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.postgres_col_1000_SF_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.postgres_col_1000_SF_update_nodes(crud_evaluator)
                update_edge_time = self.postgres_col_1000_SF_update_edges(crud_evaluator)
                delete_time = self.postgres_col_1000_SF_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "postgres" in self.Dbms_evaluator_class.db_name() and "10000_5" == dataset_name:
                create_time = self.postgres_col_10000_5_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.postgres_col_10000_5_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.postgres_col_10000_5_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.postgres_col_10000_5_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.postgres_col_10000_5_update_nodes(crud_evaluator)
                update_edge_time = self.postgres_col_10000_5_update_edges(crud_evaluator)
                delete_time = self.postgres_col_10000_5_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "postgres" in self.Dbms_evaluator_class.db_name() and "10000_10" == dataset_name:
                create_time = self.postgres_col_10000_10_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.postgres_col_10000_10_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.postgres_col_10000_10_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.postgres_col_10000_10_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.postgres_col_10000_10_update_nodes(crud_evaluator)
                update_edge_time = self.postgres_col_10000_10_update_edges(crud_evaluator)
                delete_time = self.postgres_col_10000_10_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "postgres" in self.Dbms_evaluator_class.db_name() and "10000_20" == dataset_name:
                create_time = self.postgres_col_10000_20_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.postgres_col_10000_20_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.postgres_col_10000_20_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.postgres_col_10000_20_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.postgres_col_10000_20_update_nodes(crud_evaluator)
                update_edge_time = self.postgres_col_10000_20_update_edges(crud_evaluator)
                delete_time = self.postgres_col_10000_20_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "postgres" in self.Dbms_evaluator_class.db_name() and "10000_SF" == dataset_name:
                create_time = self.postgres_col_10000_SF_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.postgres_col_10000_SF_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.postgres_col_10000_SF_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.postgres_col_10000_SF_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.postgres_col_10000_SF_update_nodes(crud_evaluator)
                update_edge_time = self.postgres_col_10000_SF_update_edges(crud_evaluator)
                delete_time = self.postgres_col_10000_SF_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "postgres" in self.Dbms_evaluator_class.db_name() and "100000_5" == dataset_name:
                create_time = self.postgres_col_100000_5_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.postgres_col_100000_5_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.postgres_col_100000_5_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.postgres_col_100000_5_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.postgres_col_100000_5_update_nodes(crud_evaluator)
                update_edge_time = self.postgres_col_100000_5_update_edges(crud_evaluator)
                delete_time = self.postgres_col_100000_5_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "postgres" in self.Dbms_evaluator_class.db_name() and "100000_10" == dataset_name:
                create_time = self.postgres_col_100000_10_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.postgres_col_100000_10_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.postgres_col_100000_10_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.postgres_col_100000_10_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.postgres_col_100000_10_update_nodes(crud_evaluator)
                update_edge_time = self.postgres_col_100000_10_update_edges(crud_evaluator)
                delete_time = self.postgres_col_100000_10_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "postgres" in self.Dbms_evaluator_class.db_name() and "100000_20" == dataset_name:
                create_time = self.postgres_col_100000_20_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.postgres_col_100000_20_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.postgres_col_100000_20_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.postgres_col_100000_20_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.postgres_col_100000_20_update_nodes(crud_evaluator)
                update_edge_time = self.postgres_col_100000_20_update_edges(crud_evaluator)
                delete_time = self.postgres_col_100000_20_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "postgres" in self.Dbms_evaluator_class.db_name() and "100000_SF" == dataset_name:
                create_time = self.postgres_col_100000_SF_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.postgres_col_100000_SF_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.postgres_col_100000_SF_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.postgres_col_100000_SF_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.postgres_col_100000_SF_update_nodes(crud_evaluator)
                update_edge_time = self.postgres_col_100000_SF_update_edges(crud_evaluator)
                delete_time = self.postgres_col_100000_SF_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "postgres" in self.Dbms_evaluator_class.db_name() and "1000000_5" == dataset_name:
                create_time = self.postgres_col_1000000_5_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.postgres_col_1000000_5_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.postgres_col_1000000_5_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.postgres_col_1000000_5_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.postgres_col_1000000_5_update_nodes(crud_evaluator)
                update_edge_time = self.postgres_col_1000000_5_update_edges(crud_evaluator)
                delete_time = self.postgres_col_1000000_5_delete(crud_evaluator)
            

            if "col" in self.Dbms_evaluator_class.file_suffix() and "postgres" in self.Dbms_evaluator_class.db_name() and "1000000_SF" == dataset_name:
                create_time = self.postgres_col_1000000_SF_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.postgres_col_1000000_SF_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.postgres_col_1000000_SF_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.postgres_col_1000000_SF_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.postgres_col_1000000_SF_update_nodes(crud_evaluator)
                update_edge_time = self.postgres_col_1000000_SF_update_edges(crud_evaluator)
                delete_time = self.postgres_col_1000000_SF_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "postgres" in self.Dbms_evaluator_class.db_name() and "ppi" == dataset_name:
                create_time = self.postgres_list_ppi_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.postgres_list_ppi_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.postgres_list_ppi_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.postgres_list_ppi_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.postgres_list_ppi_update_nodes(crud_evaluator)
                update_edge_time = self.postgres_list_ppi_update_edges(crud_evaluator)
                delete_time = self.postgres_list_ppi_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "postgres" in self.Dbms_evaluator_class.db_name() and "1000_5" == dataset_name:
                create_time = self.postgres_list_1000_5_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.postgres_list_1000_5_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.postgres_list_1000_5_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.postgres_list_1000_5_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.postgres_list_1000_5_update_nodes(crud_evaluator)
                update_edge_time = self.postgres_list_1000_5_update_edges(crud_evaluator)
                delete_time = self.postgres_list_1000_5_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "postgres" in self.Dbms_evaluator_class.db_name() and "1000_10" == dataset_name:
                create_time = self.postgres_list_1000_10_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.postgres_list_1000_10_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.postgres_list_1000_10_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.postgres_list_1000_10_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.postgres_list_1000_10_update_nodes(crud_evaluator)
                update_edge_time = self.postgres_list_1000_10_update_edges(crud_evaluator)
                delete_time = self.postgres_list_1000_10_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "postgres" in self.Dbms_evaluator_class.db_name() and "1000_20" == dataset_name:
                create_time = self.postgres_list_1000_20_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.postgres_list_1000_20_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.postgres_list_1000_20_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.postgres_list_1000_20_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.postgres_list_1000_20_update_nodes(crud_evaluator)
                update_edge_time = self.postgres_list_1000_20_update_edges(crud_evaluator)
                delete_time = self.postgres_list_1000_20_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "postgres" in self.Dbms_evaluator_class.db_name() and "1000_SF" == dataset_name:
                create_time = self.postgres_list_1000_SF_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.postgres_list_1000_SF_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.postgres_list_1000_SF_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.postgres_list_1000_SF_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.postgres_list_1000_SF_update_nodes(crud_evaluator)
                update_edge_time = self.postgres_list_1000_SF_update_edges(crud_evaluator)
                delete_time = self.postgres_list_1000_SF_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "postgres" in self.Dbms_evaluator_class.db_name() and "10000_5" == dataset_name:
                create_time = self.postgres_list_10000_5_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.postgres_list_10000_5_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.postgres_list_10000_5_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.postgres_list_10000_5_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.postgres_list_10000_5_update_nodes(crud_evaluator)
                update_edge_time = self.postgres_list_10000_5_update_edges(crud_evaluator)
                delete_time = self.postgres_list_10000_5_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "postgres" in self.Dbms_evaluator_class.db_name() and "10000_10" == dataset_name:
                create_time = self.postgres_list_10000_10_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.postgres_list_10000_10_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.postgres_list_10000_10_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.postgres_list_10000_10_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.postgres_list_10000_10_update_nodes(crud_evaluator)
                update_edge_time = self.postgres_list_10000_10_update_edges(crud_evaluator)
                delete_time = self.postgres_list_10000_10_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "postgres" in self.Dbms_evaluator_class.db_name() and "10000_20" == dataset_name:
                create_time = self.postgres_list_10000_20_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.postgres_list_10000_20_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.postgres_list_10000_20_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.postgres_list_10000_20_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.postgres_list_10000_20_update_nodes(crud_evaluator)
                update_edge_time = self.postgres_list_10000_20_update_edges(crud_evaluator)
                delete_time = self.postgres_list_10000_20_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "postgres" in self.Dbms_evaluator_class.db_name() and "10000_SF" == dataset_name:
                create_time = self.postgres_list_10000_SF_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.postgres_list_10000_SF_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.postgres_list_10000_SF_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.postgres_list_10000_SF_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.postgres_list_10000_SF_update_nodes(crud_evaluator)
                update_edge_time = self.postgres_list_10000_SF_update_edges(crud_evaluator)
                delete_time = self.postgres_list_10000_SF_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "postgres" in self.Dbms_evaluator_class.db_name() and "100000_5" == dataset_name:
                create_time = self.postgres_list_100000_5_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.postgres_list_100000_5_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.postgres_list_100000_5_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.postgres_list_100000_5_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.postgres_list_100000_5_update_nodes(crud_evaluator)
                update_edge_time = self.postgres_list_100000_5_update_edges(crud_evaluator)
                delete_time = self.postgres_list_100000_5_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "postgres" in self.Dbms_evaluator_class.db_name() and "100000_10" == dataset_name:
                create_time = self.postgres_list_100000_10_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.postgres_list_100000_10_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.postgres_list_100000_10_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.postgres_list_100000_10_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.postgres_list_100000_10_update_nodes(crud_evaluator)
                update_edge_time = self.postgres_list_100000_10_update_edges(crud_evaluator)
                delete_time = self.postgres_list_100000_10_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "postgres" in self.Dbms_evaluator_class.db_name() and "100000_20" == dataset_name:
                create_time = self.postgres_list_100000_20_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.postgres_list_100000_20_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.postgres_list_100000_20_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.postgres_list_100000_20_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.postgres_list_100000_20_update_nodes(crud_evaluator)
                update_edge_time = self.postgres_list_100000_20_update_edges(crud_evaluator)
                delete_time = self.postgres_list_100000_20_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "postgres" in self.Dbms_evaluator_class.db_name() and "100000_SF" == dataset_name:
                create_time = self.postgres_list_100000_SF_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.postgres_list_100000_SF_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.postgres_list_100000_SF_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.postgres_list_100000_SF_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.postgres_list_100000_SF_update_nodes(crud_evaluator)
                update_edge_time = self.postgres_list_100000_SF_update_edges(crud_evaluator)
                delete_time = self.postgres_list_100000_SF_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "postgres" in self.Dbms_evaluator_class.db_name() and "1000000_5" == dataset_name:
                create_time = self.postgres_list_1000000_5_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.postgres_list_1000000_5_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.postgres_list_1000000_5_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.postgres_list_1000000_5_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.postgres_list_1000000_5_update_nodes(crud_evaluator)
                update_edge_time = self.postgres_list_1000000_5_update_edges(crud_evaluator)
                delete_time = self.postgres_list_1000000_5_delete(crud_evaluator)
            

            if "list" in self.Dbms_evaluator_class.file_suffix() and "postgres" in self.Dbms_evaluator_class.db_name() and "1000000_SF" == dataset_name:
                create_time = self.postgres_list_1000000_SF_create(crud_evaluator)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                read_time, test_time = self.postgres_list_1000000_SF_read_1(crud_evaluator, 1, assert_features_and_labels)
                read_times['1'] = read_time
                read_times_mem['1'] = test_time
                
                read_time, test_time = self.postgres_list_1000000_SF_read_2(crud_evaluator, 2, assert_features_and_labels)
                read_times['2'] = read_time
                read_times_mem['2'] = test_time
                
                read_time, test_time = self.postgres_list_1000000_SF_read_3(crud_evaluator, 3, assert_features_and_labels)
                read_times['3'] = read_time
                read_times_mem['3'] = test_time
                
                update_node_time = self.postgres_list_1000000_SF_update_nodes(crud_evaluator)
                update_edge_time = self.postgres_list_1000000_SF_update_edges(crud_evaluator)
                delete_time = self.postgres_list_1000000_SF_delete(crud_evaluator)
            
            new_row_dict = {"name": dataset_df_row_name, "create": create_time, "update_nodes": update_node_time, "update_edges": update_edge_time, "delete": delete_time}
            for hops in read_times:
                new_row_dict[f"read_{hops}"] = read_times[hops]
                new_row_dict[f"read_in_mem_{hops}"] = read_times_mem[hops]
            new_row = pd.DataFrame([new_row_dict])
            self.output_df = pd.concat((self.output_df, new_row), ignore_index=True)

    def evaluate(self, i):
        self.output_df = pd.DataFrame(columns = ["name", "create", "update_nodes", "update_edges", "delete"])
        print(f"Iteration {i}")
        self.eval()
        self.output_df.to_csv(f"results/{self.Dbms_evaluator_class.db_name()}_{self.Dbms_evaluator_class.file_suffix()}_{i}.csv")