
import pandas as pd
from CRUD import CRUD_Evaluator
from tqdm import tqdm
import numpy as np
import scipy.stats as stats
import tracemalloc
import os
import time
import csv

MEM_LOG_FILE = "memory_usage_log.csv"
datasets = ["ppi", "1015074_SBC", "1000_5", "1000_10", "1000_20", "1000_SF", "10000_5", "10000_10", "10000_20", "10000_SF", "100000_5", "100000_10", "100000_20", "100000_SF", "1000000_5", "1000000_SF"]
#datasets = ["1000_5", "1000_10"]

def track_peak_ram():
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Start monitoring
            tracemalloc.start()

            # Run the actual function
            result = func(*args, **kwargs)

            # Get memory usage: (current, peak)
            _, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            # Convert to MB
            peak_mb = peak / (1024 * 1024)

            # Log immediately to file
            with open(MEM_LOG_FILE, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([func.__name__, time.time(), peak_mb])

            return result
        return wrapper
    return decorator

def is_stable(data):    
    n = len(data)
    if n < 5: return False
    mean = np.mean(data)
    std_dev = np.std(data, ddof=1)


    stderr = std_dev / np.sqrt(n)
    conf_interval = stderr * stats.t.ppf((1 + 0.95) / 2., n - 1)

    margin_of_error_percent = (conf_interval / mean) * 100
    return margin_of_error_percent < 5.0

class DBMSEvaluator:
    def __init__(self, Dbms_evaluator_class, time_store):
        self.output_df = pd.DataFrame(columns = ["name", "create", "update_nodes", "update_edges", "delete"])
        self.Dbms_evaluator_class = Dbms_evaluator_class
        self.time_store = time_store
        if not os.path.exists(MEM_LOG_FILE):
            with open(MEM_LOG_FILE, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["function_name", "timestamp", "peak_memory_mb"])

    
    @track_peak_ram()
    def neo4jce__col__1015074_SBC__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jce__col__1015074_SBC__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__1015074_SBC__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__1015074_SBC__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__1015074_SBC__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jce__col__1015074_SBC__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jce__col__1015074_SBC__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jce__col__ppi__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jce__col__ppi__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__ppi__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__ppi__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__ppi__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jce__col__ppi__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jce__col__ppi__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jce__col__1000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jce__col__1000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__1000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__1000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__1000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jce__col__1000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jce__col__1000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jce__col__1000_10__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jce__col__1000_10__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__1000_10__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__1000_10__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__1000_10__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jce__col__1000_10__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jce__col__1000_10__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jce__col__1000_20__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jce__col__1000_20__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__1000_20__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__1000_20__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__1000_20__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jce__col__1000_20__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jce__col__1000_20__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jce__col__1000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jce__col__1000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__1000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__1000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__1000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jce__col__1000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jce__col__1000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jce__col__10000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jce__col__10000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__10000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__10000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__10000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jce__col__10000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jce__col__10000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jce__col__10000_10__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jce__col__10000_10__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__10000_10__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__10000_10__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__10000_10__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jce__col__10000_10__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jce__col__10000_10__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jce__col__10000_20__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jce__col__10000_20__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__10000_20__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__10000_20__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__10000_20__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jce__col__10000_20__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jce__col__10000_20__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jce__col__10000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jce__col__10000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__10000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__10000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__10000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jce__col__10000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jce__col__10000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jce__col__100000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jce__col__100000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__100000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__100000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__100000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jce__col__100000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jce__col__100000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jce__col__100000_10__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jce__col__100000_10__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__100000_10__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__100000_10__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__100000_10__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jce__col__100000_10__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jce__col__100000_10__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jce__col__100000_20__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jce__col__100000_20__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__100000_20__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__100000_20__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__100000_20__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jce__col__100000_20__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jce__col__100000_20__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jce__col__100000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jce__col__100000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__100000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__100000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__100000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jce__col__100000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jce__col__100000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jce__col__1000000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jce__col__1000000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__1000000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__1000000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__1000000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jce__col__1000000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jce__col__1000000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jce__col__1000000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jce__col__1000000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__1000000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__1000000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__col__1000000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jce__col__1000000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jce__col__1000000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jce__list__1015074_SBC__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jce__list__1015074_SBC__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__1015074_SBC__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__1015074_SBC__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__1015074_SBC__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jce__list__1015074_SBC__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jce__list__1015074_SBC__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jce__list__ppi__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jce__list__ppi__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__ppi__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__ppi__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__ppi__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jce__list__ppi__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jce__list__ppi__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jce__list__1000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jce__list__1000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__1000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__1000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__1000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jce__list__1000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jce__list__1000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jce__list__1000_10__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jce__list__1000_10__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__1000_10__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__1000_10__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__1000_10__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jce__list__1000_10__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jce__list__1000_10__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jce__list__1000_20__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jce__list__1000_20__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__1000_20__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__1000_20__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__1000_20__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jce__list__1000_20__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jce__list__1000_20__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jce__list__1000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jce__list__1000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__1000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__1000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__1000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jce__list__1000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jce__list__1000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jce__list__10000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jce__list__10000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__10000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__10000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__10000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jce__list__10000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jce__list__10000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jce__list__10000_10__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jce__list__10000_10__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__10000_10__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__10000_10__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__10000_10__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jce__list__10000_10__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jce__list__10000_10__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jce__list__10000_20__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jce__list__10000_20__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__10000_20__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__10000_20__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__10000_20__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jce__list__10000_20__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jce__list__10000_20__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jce__list__10000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jce__list__10000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__10000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__10000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__10000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jce__list__10000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jce__list__10000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jce__list__100000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jce__list__100000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__100000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__100000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__100000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jce__list__100000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jce__list__100000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jce__list__100000_10__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jce__list__100000_10__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__100000_10__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__100000_10__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__100000_10__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jce__list__100000_10__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jce__list__100000_10__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jce__list__100000_20__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jce__list__100000_20__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__100000_20__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__100000_20__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__100000_20__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jce__list__100000_20__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jce__list__100000_20__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jce__list__100000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jce__list__100000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__100000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__100000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__100000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jce__list__100000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jce__list__100000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jce__list__1000000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jce__list__1000000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__1000000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__1000000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__1000000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jce__list__1000000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jce__list__1000000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jce__list__1000000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jce__list__1000000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__1000000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__1000000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jce__list__1000000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jce__list__1000000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jce__list__1000000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jee__col__1015074_SBC__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jee__col__1015074_SBC__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__1015074_SBC__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__1015074_SBC__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__1015074_SBC__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jee__col__1015074_SBC__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jee__col__1015074_SBC__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jee__col__ppi__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jee__col__ppi__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__ppi__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__ppi__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__ppi__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jee__col__ppi__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jee__col__ppi__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jee__col__1000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jee__col__1000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__1000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__1000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__1000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jee__col__1000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jee__col__1000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jee__col__1000_10__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jee__col__1000_10__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__1000_10__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__1000_10__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__1000_10__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jee__col__1000_10__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jee__col__1000_10__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jee__col__1000_20__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jee__col__1000_20__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__1000_20__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__1000_20__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__1000_20__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jee__col__1000_20__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jee__col__1000_20__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jee__col__1000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jee__col__1000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__1000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__1000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__1000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jee__col__1000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jee__col__1000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jee__col__10000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jee__col__10000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__10000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__10000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__10000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jee__col__10000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jee__col__10000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jee__col__10000_10__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jee__col__10000_10__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__10000_10__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__10000_10__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__10000_10__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jee__col__10000_10__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jee__col__10000_10__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jee__col__10000_20__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jee__col__10000_20__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__10000_20__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__10000_20__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__10000_20__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jee__col__10000_20__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jee__col__10000_20__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jee__col__10000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jee__col__10000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__10000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__10000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__10000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jee__col__10000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jee__col__10000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jee__col__100000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jee__col__100000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__100000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__100000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__100000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jee__col__100000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jee__col__100000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jee__col__100000_10__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jee__col__100000_10__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__100000_10__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__100000_10__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__100000_10__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jee__col__100000_10__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jee__col__100000_10__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jee__col__100000_20__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jee__col__100000_20__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__100000_20__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__100000_20__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__100000_20__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jee__col__100000_20__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jee__col__100000_20__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jee__col__100000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jee__col__100000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__100000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__100000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__100000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jee__col__100000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jee__col__100000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jee__col__1000000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jee__col__1000000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__1000000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__1000000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__1000000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jee__col__1000000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jee__col__1000000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jee__col__1000000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jee__col__1000000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__1000000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__1000000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__col__1000000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jee__col__1000000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jee__col__1000000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jee__list__1015074_SBC__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jee__list__1015074_SBC__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__1015074_SBC__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__1015074_SBC__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__1015074_SBC__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jee__list__1015074_SBC__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jee__list__1015074_SBC__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jee__list__ppi__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jee__list__ppi__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__ppi__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__ppi__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__ppi__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jee__list__ppi__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jee__list__ppi__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jee__list__1000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jee__list__1000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__1000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__1000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__1000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jee__list__1000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jee__list__1000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jee__list__1000_10__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jee__list__1000_10__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__1000_10__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__1000_10__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__1000_10__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jee__list__1000_10__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jee__list__1000_10__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jee__list__1000_20__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jee__list__1000_20__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__1000_20__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__1000_20__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__1000_20__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jee__list__1000_20__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jee__list__1000_20__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jee__list__1000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jee__list__1000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__1000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__1000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__1000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jee__list__1000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jee__list__1000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jee__list__10000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jee__list__10000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__10000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__10000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__10000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jee__list__10000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jee__list__10000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jee__list__10000_10__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jee__list__10000_10__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__10000_10__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__10000_10__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__10000_10__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jee__list__10000_10__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jee__list__10000_10__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jee__list__10000_20__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jee__list__10000_20__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__10000_20__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__10000_20__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__10000_20__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jee__list__10000_20__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jee__list__10000_20__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jee__list__10000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jee__list__10000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__10000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__10000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__10000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jee__list__10000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jee__list__10000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jee__list__100000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jee__list__100000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__100000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__100000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__100000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jee__list__100000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jee__list__100000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jee__list__100000_10__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jee__list__100000_10__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__100000_10__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__100000_10__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__100000_10__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jee__list__100000_10__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jee__list__100000_10__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jee__list__100000_20__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jee__list__100000_20__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__100000_20__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__100000_20__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__100000_20__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jee__list__100000_20__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jee__list__100000_20__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jee__list__100000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jee__list__100000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__100000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__100000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__100000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jee__list__100000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jee__list__100000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jee__list__1000000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jee__list__1000000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__1000000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__1000000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__1000000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jee__list__1000000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jee__list__1000000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def neo4jee__list__1000000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def neo4jee__list__1000000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__1000000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__1000000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def neo4jee__list__1000000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def neo4jee__list__1000000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def neo4jee__list__1000000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def mysql__col__1015074_SBC__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def mysql__col__1015074_SBC__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__1015074_SBC__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__1015074_SBC__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__1015074_SBC__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def mysql__col__1015074_SBC__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def mysql__col__1015074_SBC__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def mysql__col__ppi__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def mysql__col__ppi__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__ppi__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__ppi__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__ppi__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def mysql__col__ppi__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def mysql__col__ppi__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def mysql__col__1000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def mysql__col__1000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__1000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__1000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__1000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def mysql__col__1000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def mysql__col__1000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def mysql__col__1000_10__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def mysql__col__1000_10__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__1000_10__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__1000_10__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__1000_10__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def mysql__col__1000_10__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def mysql__col__1000_10__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def mysql__col__1000_20__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def mysql__col__1000_20__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__1000_20__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__1000_20__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__1000_20__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def mysql__col__1000_20__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def mysql__col__1000_20__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def mysql__col__1000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def mysql__col__1000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__1000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__1000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__1000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def mysql__col__1000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def mysql__col__1000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def mysql__col__10000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def mysql__col__10000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__10000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__10000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__10000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def mysql__col__10000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def mysql__col__10000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def mysql__col__10000_10__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def mysql__col__10000_10__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__10000_10__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__10000_10__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__10000_10__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def mysql__col__10000_10__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def mysql__col__10000_10__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def mysql__col__10000_20__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def mysql__col__10000_20__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__10000_20__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__10000_20__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__10000_20__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def mysql__col__10000_20__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def mysql__col__10000_20__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def mysql__col__10000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def mysql__col__10000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__10000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__10000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__10000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def mysql__col__10000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def mysql__col__10000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def mysql__col__100000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def mysql__col__100000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__100000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__100000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__100000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def mysql__col__100000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def mysql__col__100000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def mysql__col__100000_10__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def mysql__col__100000_10__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__100000_10__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__100000_10__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__100000_10__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def mysql__col__100000_10__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def mysql__col__100000_10__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def mysql__col__100000_20__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def mysql__col__100000_20__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__100000_20__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__100000_20__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__100000_20__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def mysql__col__100000_20__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def mysql__col__100000_20__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def mysql__col__100000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def mysql__col__100000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__100000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__100000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__100000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def mysql__col__100000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def mysql__col__100000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def mysql__col__1000000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def mysql__col__1000000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__1000000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__1000000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__1000000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def mysql__col__1000000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def mysql__col__1000000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def mysql__col__1000000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def mysql__col__1000000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__1000000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__1000000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__col__1000000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def mysql__col__1000000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def mysql__col__1000000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def mysql__list__1015074_SBC__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def mysql__list__1015074_SBC__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__1015074_SBC__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__1015074_SBC__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__1015074_SBC__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def mysql__list__1015074_SBC__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def mysql__list__1015074_SBC__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def mysql__list__ppi__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def mysql__list__ppi__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__ppi__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__ppi__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__ppi__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def mysql__list__ppi__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def mysql__list__ppi__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def mysql__list__1000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def mysql__list__1000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__1000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__1000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__1000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def mysql__list__1000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def mysql__list__1000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def mysql__list__1000_10__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def mysql__list__1000_10__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__1000_10__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__1000_10__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__1000_10__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def mysql__list__1000_10__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def mysql__list__1000_10__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def mysql__list__1000_20__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def mysql__list__1000_20__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__1000_20__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__1000_20__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__1000_20__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def mysql__list__1000_20__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def mysql__list__1000_20__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def mysql__list__1000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def mysql__list__1000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__1000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__1000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__1000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def mysql__list__1000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def mysql__list__1000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def mysql__list__10000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def mysql__list__10000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__10000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__10000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__10000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def mysql__list__10000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def mysql__list__10000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def mysql__list__10000_10__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def mysql__list__10000_10__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__10000_10__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__10000_10__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__10000_10__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def mysql__list__10000_10__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def mysql__list__10000_10__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def mysql__list__10000_20__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def mysql__list__10000_20__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__10000_20__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__10000_20__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__10000_20__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def mysql__list__10000_20__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def mysql__list__10000_20__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def mysql__list__10000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def mysql__list__10000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__10000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__10000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__10000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def mysql__list__10000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def mysql__list__10000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def mysql__list__100000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def mysql__list__100000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__100000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__100000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__100000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def mysql__list__100000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def mysql__list__100000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def mysql__list__100000_10__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def mysql__list__100000_10__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__100000_10__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__100000_10__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__100000_10__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def mysql__list__100000_10__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def mysql__list__100000_10__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def mysql__list__100000_20__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def mysql__list__100000_20__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__100000_20__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__100000_20__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__100000_20__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def mysql__list__100000_20__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def mysql__list__100000_20__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def mysql__list__100000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def mysql__list__100000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__100000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__100000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__100000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def mysql__list__100000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def mysql__list__100000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def mysql__list__1000000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def mysql__list__1000000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__1000000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__1000000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__1000000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def mysql__list__1000000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def mysql__list__1000000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def mysql__list__1000000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def mysql__list__1000000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__1000000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__1000000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def mysql__list__1000000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def mysql__list__1000000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def mysql__list__1000000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def postgres__col__1015074_SBC__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def postgres__col__1015074_SBC__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__1015074_SBC__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__1015074_SBC__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__1015074_SBC__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def postgres__col__1015074_SBC__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def postgres__col__1015074_SBC__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def postgres__col__ppi__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def postgres__col__ppi__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__ppi__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__ppi__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__ppi__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def postgres__col__ppi__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def postgres__col__ppi__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def postgres__col__1000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def postgres__col__1000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__1000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__1000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__1000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def postgres__col__1000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def postgres__col__1000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def postgres__col__1000_10__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def postgres__col__1000_10__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__1000_10__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__1000_10__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__1000_10__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def postgres__col__1000_10__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def postgres__col__1000_10__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def postgres__col__1000_20__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def postgres__col__1000_20__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__1000_20__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__1000_20__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__1000_20__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def postgres__col__1000_20__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def postgres__col__1000_20__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def postgres__col__1000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def postgres__col__1000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__1000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__1000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__1000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def postgres__col__1000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def postgres__col__1000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def postgres__col__10000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def postgres__col__10000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__10000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__10000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__10000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def postgres__col__10000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def postgres__col__10000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def postgres__col__10000_10__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def postgres__col__10000_10__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__10000_10__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__10000_10__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__10000_10__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def postgres__col__10000_10__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def postgres__col__10000_10__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def postgres__col__10000_20__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def postgres__col__10000_20__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__10000_20__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__10000_20__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__10000_20__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def postgres__col__10000_20__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def postgres__col__10000_20__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def postgres__col__10000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def postgres__col__10000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__10000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__10000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__10000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def postgres__col__10000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def postgres__col__10000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def postgres__col__100000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def postgres__col__100000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__100000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__100000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__100000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def postgres__col__100000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def postgres__col__100000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def postgres__col__100000_10__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def postgres__col__100000_10__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__100000_10__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__100000_10__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__100000_10__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def postgres__col__100000_10__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def postgres__col__100000_10__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def postgres__col__100000_20__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def postgres__col__100000_20__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__100000_20__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__100000_20__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__100000_20__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def postgres__col__100000_20__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def postgres__col__100000_20__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def postgres__col__100000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def postgres__col__100000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__100000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__100000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__100000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def postgres__col__100000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def postgres__col__100000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def postgres__col__1000000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def postgres__col__1000000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__1000000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__1000000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__1000000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def postgres__col__1000000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def postgres__col__1000000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def postgres__col__1000000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def postgres__col__1000000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__1000000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__1000000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__col__1000000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def postgres__col__1000000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def postgres__col__1000000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def postgres__list__1015074_SBC__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def postgres__list__1015074_SBC__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__1015074_SBC__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__1015074_SBC__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__1015074_SBC__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def postgres__list__1015074_SBC__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def postgres__list__1015074_SBC__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def postgres__list__ppi__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def postgres__list__ppi__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__ppi__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__ppi__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__ppi__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def postgres__list__ppi__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def postgres__list__ppi__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def postgres__list__1000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def postgres__list__1000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__1000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__1000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__1000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def postgres__list__1000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def postgres__list__1000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def postgres__list__1000_10__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def postgres__list__1000_10__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__1000_10__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__1000_10__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__1000_10__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def postgres__list__1000_10__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def postgres__list__1000_10__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def postgres__list__1000_20__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def postgres__list__1000_20__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__1000_20__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__1000_20__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__1000_20__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def postgres__list__1000_20__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def postgres__list__1000_20__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def postgres__list__1000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def postgres__list__1000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__1000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__1000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__1000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def postgres__list__1000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def postgres__list__1000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def postgres__list__10000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def postgres__list__10000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__10000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__10000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__10000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def postgres__list__10000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def postgres__list__10000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def postgres__list__10000_10__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def postgres__list__10000_10__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__10000_10__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__10000_10__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__10000_10__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def postgres__list__10000_10__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def postgres__list__10000_10__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def postgres__list__10000_20__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def postgres__list__10000_20__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__10000_20__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__10000_20__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__10000_20__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def postgres__list__10000_20__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def postgres__list__10000_20__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def postgres__list__10000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def postgres__list__10000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__10000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__10000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__10000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def postgres__list__10000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def postgres__list__10000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def postgres__list__100000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def postgres__list__100000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__100000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__100000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__100000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def postgres__list__100000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def postgres__list__100000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def postgres__list__100000_10__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def postgres__list__100000_10__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__100000_10__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__100000_10__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__100000_10__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def postgres__list__100000_10__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def postgres__list__100000_10__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def postgres__list__100000_20__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def postgres__list__100000_20__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__100000_20__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__100000_20__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__100000_20__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def postgres__list__100000_20__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def postgres__list__100000_20__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def postgres__list__100000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def postgres__list__100000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__100000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__100000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__100000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def postgres__list__100000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def postgres__list__100000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def postgres__list__1000000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def postgres__list__1000000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__1000000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__1000000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__1000000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def postgres__list__1000000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def postgres__list__1000000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def postgres__list__1000000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def postgres__list__1000000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__1000000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__1000000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def postgres__list__1000000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def postgres__list__1000000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def postgres__list__1000000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def sqlite__col__1015074_SBC__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def sqlite__col__1015074_SBC__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__1015074_SBC__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__1015074_SBC__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__1015074_SBC__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def sqlite__col__1015074_SBC__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def sqlite__col__1015074_SBC__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def sqlite__col__ppi__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def sqlite__col__ppi__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__ppi__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__ppi__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__ppi__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def sqlite__col__ppi__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def sqlite__col__ppi__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def sqlite__col__1000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def sqlite__col__1000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__1000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__1000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__1000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def sqlite__col__1000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def sqlite__col__1000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def sqlite__col__1000_10__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def sqlite__col__1000_10__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__1000_10__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__1000_10__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__1000_10__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def sqlite__col__1000_10__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def sqlite__col__1000_10__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def sqlite__col__1000_20__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def sqlite__col__1000_20__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__1000_20__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__1000_20__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__1000_20__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def sqlite__col__1000_20__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def sqlite__col__1000_20__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def sqlite__col__1000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def sqlite__col__1000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__1000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__1000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__1000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def sqlite__col__1000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def sqlite__col__1000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def sqlite__col__10000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def sqlite__col__10000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__10000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__10000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__10000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def sqlite__col__10000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def sqlite__col__10000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def sqlite__col__10000_10__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def sqlite__col__10000_10__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__10000_10__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__10000_10__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__10000_10__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def sqlite__col__10000_10__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def sqlite__col__10000_10__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def sqlite__col__10000_20__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def sqlite__col__10000_20__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__10000_20__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__10000_20__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__10000_20__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def sqlite__col__10000_20__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def sqlite__col__10000_20__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def sqlite__col__10000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def sqlite__col__10000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__10000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__10000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__10000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def sqlite__col__10000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def sqlite__col__10000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def sqlite__col__100000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def sqlite__col__100000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__100000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__100000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__100000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def sqlite__col__100000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def sqlite__col__100000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def sqlite__col__100000_10__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def sqlite__col__100000_10__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__100000_10__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__100000_10__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__100000_10__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def sqlite__col__100000_10__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def sqlite__col__100000_10__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def sqlite__col__100000_20__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def sqlite__col__100000_20__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__100000_20__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__100000_20__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__100000_20__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def sqlite__col__100000_20__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def sqlite__col__100000_20__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def sqlite__col__100000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def sqlite__col__100000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__100000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__100000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__100000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def sqlite__col__100000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def sqlite__col__100000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def sqlite__col__1000000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def sqlite__col__1000000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__1000000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__1000000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__1000000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def sqlite__col__1000000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def sqlite__col__1000000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def sqlite__col__1000000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def sqlite__col__1000000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__1000000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__1000000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__col__1000000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def sqlite__col__1000000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def sqlite__col__1000000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def sqlite__list__1015074_SBC__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def sqlite__list__1015074_SBC__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__1015074_SBC__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__1015074_SBC__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__1015074_SBC__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def sqlite__list__1015074_SBC__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def sqlite__list__1015074_SBC__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def sqlite__list__ppi__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def sqlite__list__ppi__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__ppi__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__ppi__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__ppi__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def sqlite__list__ppi__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def sqlite__list__ppi__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def sqlite__list__1000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def sqlite__list__1000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__1000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__1000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__1000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def sqlite__list__1000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def sqlite__list__1000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def sqlite__list__1000_10__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def sqlite__list__1000_10__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__1000_10__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__1000_10__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__1000_10__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def sqlite__list__1000_10__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def sqlite__list__1000_10__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def sqlite__list__1000_20__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def sqlite__list__1000_20__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__1000_20__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__1000_20__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__1000_20__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def sqlite__list__1000_20__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def sqlite__list__1000_20__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def sqlite__list__1000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def sqlite__list__1000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__1000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__1000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__1000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def sqlite__list__1000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def sqlite__list__1000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def sqlite__list__10000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def sqlite__list__10000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__10000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__10000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__10000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def sqlite__list__10000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def sqlite__list__10000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def sqlite__list__10000_10__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def sqlite__list__10000_10__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__10000_10__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__10000_10__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__10000_10__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def sqlite__list__10000_10__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def sqlite__list__10000_10__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def sqlite__list__10000_20__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def sqlite__list__10000_20__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__10000_20__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__10000_20__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__10000_20__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def sqlite__list__10000_20__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def sqlite__list__10000_20__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def sqlite__list__10000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def sqlite__list__10000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__10000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__10000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__10000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def sqlite__list__10000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def sqlite__list__10000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def sqlite__list__100000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def sqlite__list__100000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__100000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__100000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__100000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def sqlite__list__100000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def sqlite__list__100000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def sqlite__list__100000_10__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def sqlite__list__100000_10__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__100000_10__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__100000_10__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__100000_10__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def sqlite__list__100000_10__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def sqlite__list__100000_10__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def sqlite__list__100000_20__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def sqlite__list__100000_20__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__100000_20__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__100000_20__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__100000_20__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def sqlite__list__100000_20__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def sqlite__list__100000_20__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def sqlite__list__100000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def sqlite__list__100000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__100000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__100000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__100000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def sqlite__list__100000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def sqlite__list__100000_SF__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def sqlite__list__1000000_5__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def sqlite__list__1000000_5__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__1000000_5__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__1000000_5__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__1000000_5__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def sqlite__list__1000000_5__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def sqlite__list__1000000_5__delete(self, crud_evaluator):
        delete_time = crud_evaluator.delete()
        return delete_time

            
    @track_peak_ram()
    def sqlite__list__1000000_SF__create(self, crud_evaluator):
        create_time = crud_evaluator.create()
        return create_time

            
    @track_peak_ram()
    def sqlite__list__1000000_SF__read_1(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__1000000_SF__read_2(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__1000000_SF__read_3(self, crud_evaluator, hops, assert_features_and_labels):
        read_time, test_time = crud_evaluator.read(hops, assert_ids = True ,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
        return read_time, test_time

                
    @track_peak_ram()
    def sqlite__list__1000000_SF__update_nodes(self, crud_evaluator):
        update_node_time = crud_evaluator.update_nodes()
        return update_node_time

            
    @track_peak_ram()
    def sqlite__list__1000000_SF__update_edges(self, crud_evaluator):
        update_edge_time = crud_evaluator.update_edges()
        return update_edge_time

            
    @track_peak_ram()
    def sqlite__list__1000000_SF__delete(self, crud_evaluator):
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
            create_time, update_node_time, update_edge_time, delete_time = None, None, None, None
            read_times, read_times_mem = {}, {}
    
            db_match = "neo4jce" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1015074_SBC" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jce__col__1015074_SBC__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jce__col__1015074_SBC__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jce__col__1015074_SBC__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jce__col__1015074_SBC__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jce__col__1015074_SBC__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jce__col__1015074_SBC__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jce__col__1015074_SBC__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jce" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "ppi" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jce__col__ppi__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jce__col__ppi__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jce__col__ppi__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jce__col__ppi__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jce__col__ppi__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jce__col__ppi__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jce__col__ppi__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jce" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jce__col__1000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jce__col__1000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jce__col__1000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jce__col__1000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jce__col__1000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jce__col__1000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jce__col__1000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jce" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_10" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jce__col__1000_10__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jce__col__1000_10__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jce__col__1000_10__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jce__col__1000_10__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jce__col__1000_10__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jce__col__1000_10__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jce__col__1000_10__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jce" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_20" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jce__col__1000_20__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jce__col__1000_20__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jce__col__1000_20__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jce__col__1000_20__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jce__col__1000_20__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jce__col__1000_20__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jce__col__1000_20__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jce" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jce__col__1000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jce__col__1000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jce__col__1000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jce__col__1000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jce__col__1000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jce__col__1000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jce__col__1000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jce" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jce__col__10000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jce__col__10000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jce__col__10000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jce__col__10000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jce__col__10000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jce__col__10000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jce__col__10000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jce" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_10" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jce__col__10000_10__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jce__col__10000_10__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jce__col__10000_10__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jce__col__10000_10__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jce__col__10000_10__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jce__col__10000_10__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jce__col__10000_10__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jce" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_20" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jce__col__10000_20__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jce__col__10000_20__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jce__col__10000_20__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jce__col__10000_20__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jce__col__10000_20__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jce__col__10000_20__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jce__col__10000_20__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jce" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jce__col__10000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jce__col__10000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jce__col__10000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jce__col__10000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jce__col__10000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jce__col__10000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jce__col__10000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jce" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jce__col__100000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jce__col__100000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jce__col__100000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jce__col__100000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jce__col__100000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jce__col__100000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jce__col__100000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jce" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_10" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jce__col__100000_10__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jce__col__100000_10__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jce__col__100000_10__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jce__col__100000_10__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jce__col__100000_10__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jce__col__100000_10__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jce__col__100000_10__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jce" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_20" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jce__col__100000_20__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jce__col__100000_20__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jce__col__100000_20__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jce__col__100000_20__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jce__col__100000_20__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jce__col__100000_20__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jce__col__100000_20__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jce" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jce__col__100000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jce__col__100000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jce__col__100000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jce__col__100000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jce__col__100000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jce__col__100000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jce__col__100000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jce" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jce__col__1000000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jce__col__1000000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jce__col__1000000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jce__col__1000000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jce__col__1000000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jce__col__1000000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jce__col__1000000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jce" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jce__col__1000000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jce__col__1000000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jce__col__1000000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jce__col__1000000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jce__col__1000000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jce__col__1000000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jce__col__1000000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jce" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1015074_SBC" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jce__list__1015074_SBC__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jce__list__1015074_SBC__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jce__list__1015074_SBC__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jce__list__1015074_SBC__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jce__list__1015074_SBC__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jce__list__1015074_SBC__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jce__list__1015074_SBC__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jce" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "ppi" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jce__list__ppi__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jce__list__ppi__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jce__list__ppi__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jce__list__ppi__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jce__list__ppi__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jce__list__ppi__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jce__list__ppi__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jce" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jce__list__1000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jce__list__1000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jce__list__1000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jce__list__1000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jce__list__1000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jce__list__1000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jce__list__1000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jce" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_10" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jce__list__1000_10__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jce__list__1000_10__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jce__list__1000_10__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jce__list__1000_10__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jce__list__1000_10__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jce__list__1000_10__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jce__list__1000_10__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jce" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_20" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jce__list__1000_20__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jce__list__1000_20__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jce__list__1000_20__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jce__list__1000_20__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jce__list__1000_20__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jce__list__1000_20__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jce__list__1000_20__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jce" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jce__list__1000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jce__list__1000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jce__list__1000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jce__list__1000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jce__list__1000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jce__list__1000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jce__list__1000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jce" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jce__list__10000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jce__list__10000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jce__list__10000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jce__list__10000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jce__list__10000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jce__list__10000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jce__list__10000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jce" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_10" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jce__list__10000_10__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jce__list__10000_10__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jce__list__10000_10__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jce__list__10000_10__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jce__list__10000_10__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jce__list__10000_10__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jce__list__10000_10__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jce" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_20" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jce__list__10000_20__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jce__list__10000_20__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jce__list__10000_20__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jce__list__10000_20__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jce__list__10000_20__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jce__list__10000_20__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jce__list__10000_20__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jce" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jce__list__10000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jce__list__10000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jce__list__10000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jce__list__10000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jce__list__10000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jce__list__10000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jce__list__10000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jce" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jce__list__100000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jce__list__100000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jce__list__100000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jce__list__100000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jce__list__100000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jce__list__100000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jce__list__100000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jce" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_10" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jce__list__100000_10__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jce__list__100000_10__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jce__list__100000_10__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jce__list__100000_10__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jce__list__100000_10__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jce__list__100000_10__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jce__list__100000_10__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jce" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_20" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jce__list__100000_20__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jce__list__100000_20__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jce__list__100000_20__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jce__list__100000_20__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jce__list__100000_20__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jce__list__100000_20__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jce__list__100000_20__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jce" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jce__list__100000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jce__list__100000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jce__list__100000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jce__list__100000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jce__list__100000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jce__list__100000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jce__list__100000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jce" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jce__list__1000000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jce__list__1000000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jce__list__1000000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jce__list__1000000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jce__list__1000000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jce__list__1000000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jce__list__1000000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jce" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jce__list__1000000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jce__list__1000000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jce__list__1000000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jce__list__1000000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jce__list__1000000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jce__list__1000000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jce__list__1000000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jee" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1015074_SBC" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jee__col__1015074_SBC__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jee__col__1015074_SBC__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jee__col__1015074_SBC__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jee__col__1015074_SBC__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jee__col__1015074_SBC__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jee__col__1015074_SBC__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jee__col__1015074_SBC__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jee" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "ppi" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jee__col__ppi__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jee__col__ppi__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jee__col__ppi__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jee__col__ppi__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jee__col__ppi__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jee__col__ppi__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jee__col__ppi__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jee" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jee__col__1000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jee__col__1000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jee__col__1000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jee__col__1000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jee__col__1000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jee__col__1000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jee__col__1000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jee" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_10" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jee__col__1000_10__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jee__col__1000_10__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jee__col__1000_10__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jee__col__1000_10__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jee__col__1000_10__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jee__col__1000_10__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jee__col__1000_10__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jee" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_20" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jee__col__1000_20__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jee__col__1000_20__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jee__col__1000_20__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jee__col__1000_20__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jee__col__1000_20__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jee__col__1000_20__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jee__col__1000_20__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jee" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jee__col__1000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jee__col__1000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jee__col__1000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jee__col__1000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jee__col__1000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jee__col__1000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jee__col__1000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jee" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jee__col__10000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jee__col__10000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jee__col__10000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jee__col__10000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jee__col__10000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jee__col__10000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jee__col__10000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jee" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_10" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jee__col__10000_10__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jee__col__10000_10__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jee__col__10000_10__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jee__col__10000_10__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jee__col__10000_10__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jee__col__10000_10__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jee__col__10000_10__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jee" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_20" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jee__col__10000_20__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jee__col__10000_20__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jee__col__10000_20__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jee__col__10000_20__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jee__col__10000_20__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jee__col__10000_20__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jee__col__10000_20__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jee" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jee__col__10000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jee__col__10000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jee__col__10000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jee__col__10000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jee__col__10000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jee__col__10000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jee__col__10000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jee" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jee__col__100000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jee__col__100000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jee__col__100000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jee__col__100000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jee__col__100000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jee__col__100000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jee__col__100000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jee" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_10" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jee__col__100000_10__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jee__col__100000_10__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jee__col__100000_10__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jee__col__100000_10__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jee__col__100000_10__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jee__col__100000_10__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jee__col__100000_10__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jee" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_20" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jee__col__100000_20__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jee__col__100000_20__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jee__col__100000_20__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jee__col__100000_20__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jee__col__100000_20__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jee__col__100000_20__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jee__col__100000_20__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jee" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jee__col__100000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jee__col__100000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jee__col__100000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jee__col__100000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jee__col__100000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jee__col__100000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jee__col__100000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jee" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jee__col__1000000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jee__col__1000000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jee__col__1000000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jee__col__1000000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jee__col__1000000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jee__col__1000000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jee__col__1000000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jee" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jee__col__1000000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jee__col__1000000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jee__col__1000000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jee__col__1000000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jee__col__1000000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jee__col__1000000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jee__col__1000000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jee" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1015074_SBC" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jee__list__1015074_SBC__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jee__list__1015074_SBC__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jee__list__1015074_SBC__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jee__list__1015074_SBC__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jee__list__1015074_SBC__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jee__list__1015074_SBC__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jee__list__1015074_SBC__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jee" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "ppi" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jee__list__ppi__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jee__list__ppi__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jee__list__ppi__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jee__list__ppi__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jee__list__ppi__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jee__list__ppi__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jee__list__ppi__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jee" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jee__list__1000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jee__list__1000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jee__list__1000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jee__list__1000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jee__list__1000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jee__list__1000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jee__list__1000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jee" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_10" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jee__list__1000_10__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jee__list__1000_10__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jee__list__1000_10__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jee__list__1000_10__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jee__list__1000_10__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jee__list__1000_10__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jee__list__1000_10__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jee" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_20" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jee__list__1000_20__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jee__list__1000_20__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jee__list__1000_20__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jee__list__1000_20__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jee__list__1000_20__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jee__list__1000_20__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jee__list__1000_20__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jee" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jee__list__1000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jee__list__1000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jee__list__1000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jee__list__1000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jee__list__1000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jee__list__1000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jee__list__1000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jee" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jee__list__10000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jee__list__10000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jee__list__10000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jee__list__10000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jee__list__10000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jee__list__10000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jee__list__10000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jee" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_10" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jee__list__10000_10__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jee__list__10000_10__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jee__list__10000_10__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jee__list__10000_10__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jee__list__10000_10__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jee__list__10000_10__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jee__list__10000_10__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jee" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_20" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jee__list__10000_20__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jee__list__10000_20__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jee__list__10000_20__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jee__list__10000_20__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jee__list__10000_20__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jee__list__10000_20__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jee__list__10000_20__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jee" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jee__list__10000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jee__list__10000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jee__list__10000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jee__list__10000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jee__list__10000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jee__list__10000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jee__list__10000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jee" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jee__list__100000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jee__list__100000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jee__list__100000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jee__list__100000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jee__list__100000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jee__list__100000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jee__list__100000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jee" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_10" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jee__list__100000_10__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jee__list__100000_10__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jee__list__100000_10__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jee__list__100000_10__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jee__list__100000_10__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jee__list__100000_10__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jee__list__100000_10__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jee" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_20" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jee__list__100000_20__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jee__list__100000_20__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jee__list__100000_20__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jee__list__100000_20__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jee__list__100000_20__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jee__list__100000_20__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jee__list__100000_20__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jee" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jee__list__100000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jee__list__100000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jee__list__100000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jee__list__100000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jee__list__100000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jee__list__100000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jee__list__100000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jee" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jee__list__1000000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jee__list__1000000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jee__list__1000000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jee__list__1000000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jee__list__1000000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jee__list__1000000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jee__list__1000000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "neo4jee" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.neo4jee__list__1000000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.neo4jee__list__1000000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.neo4jee__list__1000000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.neo4jee__list__1000000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.neo4jee__list__1000000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.neo4jee__list__1000000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.neo4jee__list__1000000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "mysql" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1015074_SBC" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.mysql__col__1015074_SBC__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.mysql__col__1015074_SBC__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.mysql__col__1015074_SBC__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.mysql__col__1015074_SBC__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.mysql__col__1015074_SBC__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.mysql__col__1015074_SBC__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.mysql__col__1015074_SBC__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "mysql" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "ppi" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.mysql__col__ppi__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.mysql__col__ppi__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.mysql__col__ppi__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.mysql__col__ppi__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.mysql__col__ppi__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.mysql__col__ppi__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.mysql__col__ppi__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "mysql" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.mysql__col__1000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.mysql__col__1000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.mysql__col__1000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.mysql__col__1000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.mysql__col__1000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.mysql__col__1000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.mysql__col__1000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "mysql" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_10" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.mysql__col__1000_10__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.mysql__col__1000_10__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.mysql__col__1000_10__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.mysql__col__1000_10__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.mysql__col__1000_10__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.mysql__col__1000_10__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.mysql__col__1000_10__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "mysql" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_20" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.mysql__col__1000_20__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.mysql__col__1000_20__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.mysql__col__1000_20__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.mysql__col__1000_20__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.mysql__col__1000_20__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.mysql__col__1000_20__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.mysql__col__1000_20__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "mysql" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.mysql__col__1000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.mysql__col__1000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.mysql__col__1000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.mysql__col__1000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.mysql__col__1000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.mysql__col__1000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.mysql__col__1000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "mysql" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.mysql__col__10000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.mysql__col__10000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.mysql__col__10000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.mysql__col__10000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.mysql__col__10000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.mysql__col__10000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.mysql__col__10000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "mysql" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_10" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.mysql__col__10000_10__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.mysql__col__10000_10__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.mysql__col__10000_10__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.mysql__col__10000_10__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.mysql__col__10000_10__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.mysql__col__10000_10__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.mysql__col__10000_10__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "mysql" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_20" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.mysql__col__10000_20__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.mysql__col__10000_20__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.mysql__col__10000_20__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.mysql__col__10000_20__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.mysql__col__10000_20__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.mysql__col__10000_20__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.mysql__col__10000_20__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "mysql" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.mysql__col__10000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.mysql__col__10000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.mysql__col__10000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.mysql__col__10000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.mysql__col__10000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.mysql__col__10000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.mysql__col__10000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "mysql" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.mysql__col__100000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.mysql__col__100000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.mysql__col__100000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.mysql__col__100000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.mysql__col__100000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.mysql__col__100000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.mysql__col__100000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "mysql" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_10" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.mysql__col__100000_10__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.mysql__col__100000_10__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.mysql__col__100000_10__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.mysql__col__100000_10__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.mysql__col__100000_10__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.mysql__col__100000_10__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.mysql__col__100000_10__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "mysql" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_20" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.mysql__col__100000_20__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.mysql__col__100000_20__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.mysql__col__100000_20__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.mysql__col__100000_20__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.mysql__col__100000_20__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.mysql__col__100000_20__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.mysql__col__100000_20__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "mysql" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.mysql__col__100000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.mysql__col__100000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.mysql__col__100000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.mysql__col__100000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.mysql__col__100000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.mysql__col__100000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.mysql__col__100000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "mysql" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.mysql__col__1000000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.mysql__col__1000000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.mysql__col__1000000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.mysql__col__1000000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.mysql__col__1000000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.mysql__col__1000000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.mysql__col__1000000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "mysql" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.mysql__col__1000000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.mysql__col__1000000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.mysql__col__1000000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.mysql__col__1000000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.mysql__col__1000000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.mysql__col__1000000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.mysql__col__1000000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "mysql" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1015074_SBC" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.mysql__list__1015074_SBC__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.mysql__list__1015074_SBC__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.mysql__list__1015074_SBC__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.mysql__list__1015074_SBC__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.mysql__list__1015074_SBC__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.mysql__list__1015074_SBC__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.mysql__list__1015074_SBC__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "mysql" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "ppi" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.mysql__list__ppi__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.mysql__list__ppi__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.mysql__list__ppi__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.mysql__list__ppi__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.mysql__list__ppi__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.mysql__list__ppi__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.mysql__list__ppi__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "mysql" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.mysql__list__1000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.mysql__list__1000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.mysql__list__1000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.mysql__list__1000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.mysql__list__1000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.mysql__list__1000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.mysql__list__1000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "mysql" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_10" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.mysql__list__1000_10__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.mysql__list__1000_10__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.mysql__list__1000_10__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.mysql__list__1000_10__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.mysql__list__1000_10__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.mysql__list__1000_10__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.mysql__list__1000_10__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "mysql" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_20" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.mysql__list__1000_20__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.mysql__list__1000_20__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.mysql__list__1000_20__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.mysql__list__1000_20__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.mysql__list__1000_20__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.mysql__list__1000_20__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.mysql__list__1000_20__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "mysql" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.mysql__list__1000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.mysql__list__1000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.mysql__list__1000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.mysql__list__1000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.mysql__list__1000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.mysql__list__1000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.mysql__list__1000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "mysql" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.mysql__list__10000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.mysql__list__10000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.mysql__list__10000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.mysql__list__10000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.mysql__list__10000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.mysql__list__10000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.mysql__list__10000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "mysql" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_10" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.mysql__list__10000_10__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.mysql__list__10000_10__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.mysql__list__10000_10__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.mysql__list__10000_10__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.mysql__list__10000_10__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.mysql__list__10000_10__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.mysql__list__10000_10__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "mysql" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_20" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.mysql__list__10000_20__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.mysql__list__10000_20__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.mysql__list__10000_20__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.mysql__list__10000_20__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.mysql__list__10000_20__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.mysql__list__10000_20__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.mysql__list__10000_20__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "mysql" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.mysql__list__10000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.mysql__list__10000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.mysql__list__10000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.mysql__list__10000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.mysql__list__10000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.mysql__list__10000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.mysql__list__10000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "mysql" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.mysql__list__100000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.mysql__list__100000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.mysql__list__100000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.mysql__list__100000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.mysql__list__100000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.mysql__list__100000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.mysql__list__100000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "mysql" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_10" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.mysql__list__100000_10__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.mysql__list__100000_10__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.mysql__list__100000_10__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.mysql__list__100000_10__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.mysql__list__100000_10__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.mysql__list__100000_10__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.mysql__list__100000_10__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "mysql" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_20" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.mysql__list__100000_20__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.mysql__list__100000_20__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.mysql__list__100000_20__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.mysql__list__100000_20__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.mysql__list__100000_20__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.mysql__list__100000_20__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.mysql__list__100000_20__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "mysql" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.mysql__list__100000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.mysql__list__100000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.mysql__list__100000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.mysql__list__100000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.mysql__list__100000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.mysql__list__100000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.mysql__list__100000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "mysql" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.mysql__list__1000000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.mysql__list__1000000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.mysql__list__1000000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.mysql__list__1000000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.mysql__list__1000000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.mysql__list__1000000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.mysql__list__1000000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "mysql" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.mysql__list__1000000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.mysql__list__1000000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.mysql__list__1000000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.mysql__list__1000000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.mysql__list__1000000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.mysql__list__1000000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.mysql__list__1000000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "postgres" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1015074_SBC" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.postgres__col__1015074_SBC__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.postgres__col__1015074_SBC__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.postgres__col__1015074_SBC__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.postgres__col__1015074_SBC__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.postgres__col__1015074_SBC__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.postgres__col__1015074_SBC__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.postgres__col__1015074_SBC__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "postgres" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "ppi" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.postgres__col__ppi__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.postgres__col__ppi__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.postgres__col__ppi__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.postgres__col__ppi__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.postgres__col__ppi__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.postgres__col__ppi__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.postgres__col__ppi__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "postgres" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.postgres__col__1000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.postgres__col__1000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.postgres__col__1000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.postgres__col__1000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.postgres__col__1000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.postgres__col__1000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.postgres__col__1000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "postgres" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_10" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.postgres__col__1000_10__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.postgres__col__1000_10__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.postgres__col__1000_10__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.postgres__col__1000_10__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.postgres__col__1000_10__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.postgres__col__1000_10__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.postgres__col__1000_10__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "postgres" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_20" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.postgres__col__1000_20__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.postgres__col__1000_20__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.postgres__col__1000_20__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.postgres__col__1000_20__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.postgres__col__1000_20__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.postgres__col__1000_20__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.postgres__col__1000_20__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "postgres" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.postgres__col__1000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.postgres__col__1000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.postgres__col__1000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.postgres__col__1000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.postgres__col__1000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.postgres__col__1000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.postgres__col__1000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "postgres" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.postgres__col__10000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.postgres__col__10000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.postgres__col__10000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.postgres__col__10000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.postgres__col__10000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.postgres__col__10000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.postgres__col__10000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "postgres" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_10" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.postgres__col__10000_10__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.postgres__col__10000_10__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.postgres__col__10000_10__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.postgres__col__10000_10__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.postgres__col__10000_10__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.postgres__col__10000_10__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.postgres__col__10000_10__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "postgres" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_20" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.postgres__col__10000_20__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.postgres__col__10000_20__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.postgres__col__10000_20__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.postgres__col__10000_20__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.postgres__col__10000_20__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.postgres__col__10000_20__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.postgres__col__10000_20__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "postgres" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.postgres__col__10000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.postgres__col__10000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.postgres__col__10000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.postgres__col__10000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.postgres__col__10000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.postgres__col__10000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.postgres__col__10000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "postgres" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.postgres__col__100000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.postgres__col__100000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.postgres__col__100000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.postgres__col__100000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.postgres__col__100000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.postgres__col__100000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.postgres__col__100000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "postgres" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_10" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.postgres__col__100000_10__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.postgres__col__100000_10__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.postgres__col__100000_10__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.postgres__col__100000_10__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.postgres__col__100000_10__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.postgres__col__100000_10__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.postgres__col__100000_10__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "postgres" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_20" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.postgres__col__100000_20__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.postgres__col__100000_20__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.postgres__col__100000_20__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.postgres__col__100000_20__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.postgres__col__100000_20__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.postgres__col__100000_20__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.postgres__col__100000_20__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "postgres" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.postgres__col__100000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.postgres__col__100000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.postgres__col__100000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.postgres__col__100000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.postgres__col__100000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.postgres__col__100000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.postgres__col__100000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "postgres" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.postgres__col__1000000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.postgres__col__1000000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.postgres__col__1000000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.postgres__col__1000000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.postgres__col__1000000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.postgres__col__1000000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.postgres__col__1000000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "postgres" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.postgres__col__1000000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.postgres__col__1000000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.postgres__col__1000000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.postgres__col__1000000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.postgres__col__1000000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.postgres__col__1000000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.postgres__col__1000000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "postgres" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1015074_SBC" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.postgres__list__1015074_SBC__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.postgres__list__1015074_SBC__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.postgres__list__1015074_SBC__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.postgres__list__1015074_SBC__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.postgres__list__1015074_SBC__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.postgres__list__1015074_SBC__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.postgres__list__1015074_SBC__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "postgres" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "ppi" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.postgres__list__ppi__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.postgres__list__ppi__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.postgres__list__ppi__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.postgres__list__ppi__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.postgres__list__ppi__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.postgres__list__ppi__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.postgres__list__ppi__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "postgres" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.postgres__list__1000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.postgres__list__1000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.postgres__list__1000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.postgres__list__1000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.postgres__list__1000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.postgres__list__1000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.postgres__list__1000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "postgres" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_10" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.postgres__list__1000_10__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.postgres__list__1000_10__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.postgres__list__1000_10__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.postgres__list__1000_10__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.postgres__list__1000_10__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.postgres__list__1000_10__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.postgres__list__1000_10__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "postgres" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_20" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.postgres__list__1000_20__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.postgres__list__1000_20__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.postgres__list__1000_20__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.postgres__list__1000_20__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.postgres__list__1000_20__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.postgres__list__1000_20__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.postgres__list__1000_20__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "postgres" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.postgres__list__1000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.postgres__list__1000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.postgres__list__1000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.postgres__list__1000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.postgres__list__1000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.postgres__list__1000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.postgres__list__1000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "postgres" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.postgres__list__10000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.postgres__list__10000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.postgres__list__10000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.postgres__list__10000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.postgres__list__10000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.postgres__list__10000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.postgres__list__10000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "postgres" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_10" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.postgres__list__10000_10__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.postgres__list__10000_10__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.postgres__list__10000_10__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.postgres__list__10000_10__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.postgres__list__10000_10__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.postgres__list__10000_10__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.postgres__list__10000_10__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "postgres" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_20" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.postgres__list__10000_20__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.postgres__list__10000_20__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.postgres__list__10000_20__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.postgres__list__10000_20__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.postgres__list__10000_20__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.postgres__list__10000_20__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.postgres__list__10000_20__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "postgres" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.postgres__list__10000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.postgres__list__10000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.postgres__list__10000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.postgres__list__10000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.postgres__list__10000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.postgres__list__10000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.postgres__list__10000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "postgres" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.postgres__list__100000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.postgres__list__100000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.postgres__list__100000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.postgres__list__100000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.postgres__list__100000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.postgres__list__100000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.postgres__list__100000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "postgres" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_10" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.postgres__list__100000_10__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.postgres__list__100000_10__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.postgres__list__100000_10__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.postgres__list__100000_10__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.postgres__list__100000_10__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.postgres__list__100000_10__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.postgres__list__100000_10__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "postgres" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_20" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.postgres__list__100000_20__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.postgres__list__100000_20__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.postgres__list__100000_20__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.postgres__list__100000_20__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.postgres__list__100000_20__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.postgres__list__100000_20__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.postgres__list__100000_20__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "postgres" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.postgres__list__100000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.postgres__list__100000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.postgres__list__100000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.postgres__list__100000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.postgres__list__100000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.postgres__list__100000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.postgres__list__100000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "postgres" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.postgres__list__1000000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.postgres__list__1000000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.postgres__list__1000000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.postgres__list__1000000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.postgres__list__1000000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.postgres__list__1000000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.postgres__list__1000000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "postgres" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.postgres__list__1000000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.postgres__list__1000000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.postgres__list__1000000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.postgres__list__1000000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.postgres__list__1000000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.postgres__list__1000000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.postgres__list__1000000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "sqlite" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1015074_SBC" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.sqlite__col__1015074_SBC__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.sqlite__col__1015074_SBC__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.sqlite__col__1015074_SBC__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.sqlite__col__1015074_SBC__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.sqlite__col__1015074_SBC__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.sqlite__col__1015074_SBC__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.sqlite__col__1015074_SBC__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "sqlite" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "ppi" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.sqlite__col__ppi__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.sqlite__col__ppi__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.sqlite__col__ppi__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.sqlite__col__ppi__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.sqlite__col__ppi__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.sqlite__col__ppi__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.sqlite__col__ppi__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "sqlite" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.sqlite__col__1000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.sqlite__col__1000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.sqlite__col__1000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.sqlite__col__1000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.sqlite__col__1000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.sqlite__col__1000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.sqlite__col__1000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "sqlite" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_10" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.sqlite__col__1000_10__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.sqlite__col__1000_10__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.sqlite__col__1000_10__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.sqlite__col__1000_10__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.sqlite__col__1000_10__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.sqlite__col__1000_10__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.sqlite__col__1000_10__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "sqlite" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_20" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.sqlite__col__1000_20__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.sqlite__col__1000_20__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.sqlite__col__1000_20__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.sqlite__col__1000_20__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.sqlite__col__1000_20__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.sqlite__col__1000_20__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.sqlite__col__1000_20__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "sqlite" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.sqlite__col__1000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.sqlite__col__1000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.sqlite__col__1000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.sqlite__col__1000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.sqlite__col__1000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.sqlite__col__1000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.sqlite__col__1000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "sqlite" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.sqlite__col__10000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.sqlite__col__10000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.sqlite__col__10000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.sqlite__col__10000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.sqlite__col__10000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.sqlite__col__10000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.sqlite__col__10000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "sqlite" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_10" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.sqlite__col__10000_10__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.sqlite__col__10000_10__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.sqlite__col__10000_10__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.sqlite__col__10000_10__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.sqlite__col__10000_10__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.sqlite__col__10000_10__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.sqlite__col__10000_10__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "sqlite" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_20" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.sqlite__col__10000_20__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.sqlite__col__10000_20__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.sqlite__col__10000_20__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.sqlite__col__10000_20__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.sqlite__col__10000_20__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.sqlite__col__10000_20__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.sqlite__col__10000_20__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "sqlite" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.sqlite__col__10000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.sqlite__col__10000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.sqlite__col__10000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.sqlite__col__10000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.sqlite__col__10000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.sqlite__col__10000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.sqlite__col__10000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "sqlite" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.sqlite__col__100000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.sqlite__col__100000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.sqlite__col__100000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.sqlite__col__100000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.sqlite__col__100000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.sqlite__col__100000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.sqlite__col__100000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "sqlite" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_10" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.sqlite__col__100000_10__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.sqlite__col__100000_10__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.sqlite__col__100000_10__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.sqlite__col__100000_10__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.sqlite__col__100000_10__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.sqlite__col__100000_10__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.sqlite__col__100000_10__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "sqlite" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_20" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.sqlite__col__100000_20__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.sqlite__col__100000_20__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.sqlite__col__100000_20__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.sqlite__col__100000_20__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.sqlite__col__100000_20__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.sqlite__col__100000_20__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.sqlite__col__100000_20__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "sqlite" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.sqlite__col__100000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.sqlite__col__100000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.sqlite__col__100000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.sqlite__col__100000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.sqlite__col__100000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.sqlite__col__100000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.sqlite__col__100000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "sqlite" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.sqlite__col__1000000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.sqlite__col__1000000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.sqlite__col__1000000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.sqlite__col__1000000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.sqlite__col__1000000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.sqlite__col__1000000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.sqlite__col__1000000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "sqlite" == self.Dbms_evaluator_class.db_name() 

            if "col" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.sqlite__col__1000000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.sqlite__col__1000000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.sqlite__col__1000000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.sqlite__col__1000000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.sqlite__col__1000000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.sqlite__col__1000000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.sqlite__col__1000000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "sqlite" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1015074_SBC" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.sqlite__list__1015074_SBC__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.sqlite__list__1015074_SBC__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.sqlite__list__1015074_SBC__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.sqlite__list__1015074_SBC__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.sqlite__list__1015074_SBC__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.sqlite__list__1015074_SBC__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.sqlite__list__1015074_SBC__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "sqlite" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "ppi" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.sqlite__list__ppi__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.sqlite__list__ppi__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.sqlite__list__ppi__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.sqlite__list__ppi__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.sqlite__list__ppi__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.sqlite__list__ppi__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.sqlite__list__ppi__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "sqlite" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.sqlite__list__1000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.sqlite__list__1000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.sqlite__list__1000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.sqlite__list__1000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.sqlite__list__1000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.sqlite__list__1000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.sqlite__list__1000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "sqlite" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_10" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.sqlite__list__1000_10__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.sqlite__list__1000_10__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.sqlite__list__1000_10__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.sqlite__list__1000_10__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.sqlite__list__1000_10__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.sqlite__list__1000_10__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.sqlite__list__1000_10__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "sqlite" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_20" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.sqlite__list__1000_20__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.sqlite__list__1000_20__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.sqlite__list__1000_20__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.sqlite__list__1000_20__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.sqlite__list__1000_20__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.sqlite__list__1000_20__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.sqlite__list__1000_20__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "sqlite" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.sqlite__list__1000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.sqlite__list__1000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.sqlite__list__1000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.sqlite__list__1000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.sqlite__list__1000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.sqlite__list__1000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.sqlite__list__1000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "sqlite" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.sqlite__list__10000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.sqlite__list__10000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.sqlite__list__10000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.sqlite__list__10000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.sqlite__list__10000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.sqlite__list__10000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.sqlite__list__10000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "sqlite" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_10" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.sqlite__list__10000_10__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.sqlite__list__10000_10__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.sqlite__list__10000_10__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.sqlite__list__10000_10__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.sqlite__list__10000_10__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.sqlite__list__10000_10__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.sqlite__list__10000_10__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "sqlite" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_20" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.sqlite__list__10000_20__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.sqlite__list__10000_20__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.sqlite__list__10000_20__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.sqlite__list__10000_20__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.sqlite__list__10000_20__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.sqlite__list__10000_20__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.sqlite__list__10000_20__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "sqlite" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "10000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.sqlite__list__10000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.sqlite__list__10000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.sqlite__list__10000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.sqlite__list__10000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.sqlite__list__10000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.sqlite__list__10000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.sqlite__list__10000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "sqlite" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.sqlite__list__100000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.sqlite__list__100000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.sqlite__list__100000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.sqlite__list__100000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.sqlite__list__100000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.sqlite__list__100000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.sqlite__list__100000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "sqlite" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_10" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.sqlite__list__100000_10__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.sqlite__list__100000_10__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.sqlite__list__100000_10__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.sqlite__list__100000_10__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.sqlite__list__100000_10__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.sqlite__list__100000_10__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.sqlite__list__100000_10__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "sqlite" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_20" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.sqlite__list__100000_20__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.sqlite__list__100000_20__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.sqlite__list__100000_20__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.sqlite__list__100000_20__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.sqlite__list__100000_20__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.sqlite__list__100000_20__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.sqlite__list__100000_20__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "sqlite" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "100000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.sqlite__list__100000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.sqlite__list__100000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.sqlite__list__100000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.sqlite__list__100000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.sqlite__list__100000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.sqlite__list__100000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.sqlite__list__100000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "sqlite" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000000_5" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.sqlite__list__1000000_5__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.sqlite__list__1000000_5__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.sqlite__list__1000000_5__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.sqlite__list__1000000_5__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.sqlite__list__1000000_5__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.sqlite__list__1000000_5__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.sqlite__list__1000000_5__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            

            db_match = "sqlite" == self.Dbms_evaluator_class.db_name() 

            if "list" == self.Dbms_evaluator_class.file_suffix() and db_match and "1000000_SF" == dataset_name:
                evaluation_dict_key = self.Dbms_evaluator_class.db_name() +  "	" + self.Dbms_evaluator_class.file_suffix()  +  "	" +  X_y_name
                if evaluation_dict_key not in self.time_store:
                    self.time_store[evaluation_dict_key] = {
                        "create": [],
                        "read_1": [],
                        "read_2": [],
                        "read_3": [],
                        "update_nodes": [],
                        "update_edges": [],
                        "delete": [],
                    }
                st_create = is_stable(self.time_store[evaluation_dict_key]["create"])
                st_read = {str(h): is_stable(self.time_store[evaluation_dict_key][f"read_{h}"]) for h in range(1,4)}
                st_up_nodes = is_stable(self.time_store[evaluation_dict_key]["update_nodes"])
                st_up_edges = is_stable(self.time_store[evaluation_dict_key]["update_edges"])
                st_delete = is_stable(self.time_store[evaluation_dict_key]["delete"])

                everything_is_stable = st_create and all(st_read.values()) and st_up_nodes and st_up_edges and st_delete
                create_time = None
                if not everything_is_stable:
                    create_time = self.sqlite__list__1000000_SF__create(crud_evaluator)
                    self.time_store[evaluation_dict_key]["create"].append(create_time)
                assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                read_times, read_times_mem = dict(), dict()
                if not st_read['1']:                    
                    read_time, test_time = self.sqlite__list__1000000_SF__read_1(crud_evaluator, 1, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '1'].append(read_time)
                    read_times['1'] = read_time
                    read_times_mem['1'] = test_time
                else:
                    read_times['1'] = None
                    read_times_mem['1'] = None
                
                if not st_read['2']:                    
                    read_time, test_time = self.sqlite__list__1000000_SF__read_2(crud_evaluator, 2, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '2'].append(read_time)
                    read_times['2'] = read_time
                    read_times_mem['2'] = test_time
                else:
                    read_times['2'] = None
                    read_times_mem['2'] = None
                
                if not st_read['3']:                    
                    read_time, test_time = self.sqlite__list__1000000_SF__read_3(crud_evaluator, 3, assert_features_and_labels)
                    self.time_store[evaluation_dict_key]["read_" + '3'].append(read_time)
                    read_times['3'] = read_time
                    read_times_mem['3'] = test_time
                else:
                    read_times['3'] = None
                    read_times_mem['3'] = None
                
                update_node_time, update_edge_time, delete_time = None, None, None
                if not st_up_nodes:
                    update_node_time = self.sqlite__list__1000000_SF__update_nodes(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_nodes"].append(update_node_time)

                if not st_up_edges:
                    update_edge_time = self.sqlite__list__1000000_SF__update_edges(crud_evaluator)
                    self.time_store[evaluation_dict_key]["update_edges"].append(update_edge_time)

                if not everything_is_stable:
                    delete_time = self.sqlite__list__1000000_SF__delete(crud_evaluator)
                    self.time_store[evaluation_dict_key]["delete"].append(delete_time)
            
            new_row_dict = {"name": dataset_df_row_name, "create": create_time, "update_nodes": update_node_time, "update_edges": update_edge_time, "delete": delete_time}
            for hops in read_times:
                new_row_dict[f"read_{hops}"] = read_times[hops]
                new_row_dict[f"read_in_mem_{hops}"] = read_times_mem[hops]
            new_row = pd.DataFrame([new_row_dict])
            self.output_df = pd.concat((self.output_df, new_row), ignore_index=True)

    def evaluate(self, i):
        self.output_df = pd.DataFrame(columns = ["name", "create", "update_nodes", "update_edges", "delete"])
        print(f"Iteration {i}")
        # self.eval_ppi()
        self.eval()
        self.output_df.to_csv(f"results/{self.Dbms_evaluator_class.db_name()}_{self.Dbms_evaluator_class.file_suffix()}_{i}.csv")
    