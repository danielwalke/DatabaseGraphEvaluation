import pandas as pd
from CRUD import CRUD_Evaluator
from tqdm import tqdm

class DBMSEvaluator:
    def __init__(self, Dbms_evaluator_class):
        self.output_df = pd.DataFrame(columns = ["name", "create", "update_nodes", "update_edges", "delete"])
        self.Dbms_evaluator_class = Dbms_evaluator_class

    def eval_ppi(self):
        crud_evaluator = CRUD_Evaluator(self.Dbms_evaluator_class, "ppi_x.csv", "ppi_y.csv", "ppi_edge_index.csv", f"X_y_ppi_{self.Dbms_evaluator_class.file_suffix()}.csv")
        create_time = crud_evaluator.create()
        read_times, read_times_mem = dict(), dict()
        for hops in range(1, 4, 1):
            read_time, test_time = crud_evaluator.read(hops, assert_ids = True,assert_edge_index = True)
            read_times[hops] = read_time
            read_times_mem[hops] = test_time
        update_node_time = crud_evaluator.update_nodes()
        update_edge_time = crud_evaluator.update_edges()
        delete_time = crud_evaluator.delete()
        new_row_dict = {"name": "PPI", "create": create_time, "update_nodes": update_node_time, "update_edges": update_edge_time, "delete": delete_time}
        for hops in read_times:
            new_row_dict[f"read_{hops}"] = read_times[hops]
            new_row_dict[f"read_in_mem_{hops}"] = read_times_mem[hops]
        new_row = pd.DataFrame([new_row_dict])
        self.output_df = pd.concat((self.output_df, new_row), ignore_index=True)
	
    def eval_synth(self):
        for num_nodes in tqdm([1_000, 10_000, 100_000, 1_000_000], desc="Evaluating synth. nodes (node size)"):
            for num_edges in tqdm(["5_edges", "10_edges", "20_edges", "scale_free"], desc="Evaluating synth. nodes (number of edges)"):
                if num_nodes != 1000: continue
                if num_edges != "5_edges": continue
                # if num_nodes < 1_000_000 or num_edges != "scale_free": continue
                # print(str(num_nodes) + num_edges)
                if num_nodes == 1_000_000 and (num_edges == "10_edges" or num_edges == "20_edges"): continue
                crud_evaluator = CRUD_Evaluator(self.Dbms_evaluator_class, f"X_{str(num_nodes)}_nodes_{num_edges}.csv", f"y_{str(num_nodes)}_nodes_{num_edges}.csv", f"edge_index_{str(num_nodes)}_nodes_{num_edges}.csv", f"X_and_y_{str(num_nodes)}_nodes_{num_edges}_{self.Dbms_evaluator_class.file_suffix()}.csv")
                create_time = crud_evaluator.create()
                read_times, read_times_mem = dict(), dict()
                for hops in range(1, 4, 1):
                    ## TODO Potentially chunking numpy all close to perform assertion on large datasets
                    assert_features_and_labels = num_nodes <= 10_000 ## Tested separaely but costs too much RAM here
                    read_time, test_time = crud_evaluator.read(hops, assert_ids = True,assert_edge_index = True, assert_features = assert_features_and_labels, assert_labels = assert_features_and_labels)
                    read_times[hops] = read_time
                    read_times_mem[hops] = test_time
                update_node_time = crud_evaluator.update_nodes()
                update_edge_time = crud_evaluator.update_edges()
                delete_time = crud_evaluator.delete()
                new_row_dict = {"name": f"{str(num_nodes)}_nodes_{num_edges}", "create": create_time, "update_nodes": update_node_time, "update_edges": update_edge_time, "delete": delete_time}
                for hops in read_times:
                    new_row_dict[f"read_{hops}"] = read_times[hops]
                    new_row_dict[f"read_in_mem_{hops}"] = read_times_mem[hops]
                new_row = pd.DataFrame([new_row_dict])
                self.output_df = pd.concat((self.output_df, new_row), ignore_index=True)

    def evaluate(self, i):
        self.output_df = pd.DataFrame(columns = ["name", "create", "update_nodes", "update_edges", "delete"])
        print(f"Iteration {i}")
        # self.eval_ppi()
        self.eval_synth()
        self.output_df.to_csv(f"results/{self.Dbms_evaluator_class.db_name()}_{self.Dbms_evaluator_class.file_suffix()}_{i}.csv")