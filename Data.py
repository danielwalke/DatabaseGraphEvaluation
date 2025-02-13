import pandas as pd
import numpy as np

class Data:
    def __init__(self):
        self.X = None
        self.y = None
        self.X_and_y = None
        self.edge_index = None
        self.X_and_y_file_name = None
        self.edge_file_name = None

    def read_features_col(self, feature_file_name):
        self.X = pd.read_csv(f"syn_data/{feature_file_name}")
        self.X.columns = list(map(lambda col: f"f_{col}", self.X.columns))

    def read_labels_col(self, label_file_name):
        self.y = pd.read_csv(f"syn_data/{label_file_name}")
        self.y.columns = list(map(lambda col: f"y_{col}", self.y.columns))
        self.y = self.y.astype(np.int8)

    def read_edges(self, edge_file_name):
        edges = pd.read_csv(f"syn_data/{edge_file_name}")
        edges.columns = ["source_id", "target_id"]
        self.edge_index = edges.values.transpose(-1, 0)
        self.edge_file_name = edge_file_name

    def create_X_and_y_col(self, X_and_y_file_name):
        self.X_and_y = self.X.copy()
        self.X_and_y = pd.concat((self.X_and_y, self.y), axis = 1)
        self.X_and_y.to_csv(f"syn_data/{X_and_y_file_name}", sep = ",", index = True)
        self.X_and_y_file_name = X_and_y_file_name

    def create_X_and_y_list_postgres(self, X_and_y_file_name):
        self.X_and_y = pd.DataFrame()
        self.X_and_y["X"] = self.X.apply(lambda row: [row[column] for column in self.X.columns], axis=1)
        self.X_and_y["y"] = self.y.apply(lambda row: [int(row[column]) for column in self.y.columns], axis=1)
        
        self.X_and_y["X"] = self.X_and_y["X"].apply(lambda x: f"{{{','.join(map(str, x))}}}")
        self.X_and_y["y"] = self.X_and_y["y"].apply(lambda x: f"{{{','.join(map(str, x))}}}")
        self.X_and_y.to_csv(f"syn_data/{X_and_y_file_name}", sep = ",", index = True)
        self.X_and_y_file_name = X_and_y_file_name

    def create_X_and_y_list_neo4j(self, X_and_y_file_name):
        self.X_and_y = pd.DataFrame()
        self.X_and_y["X"] = self.X.apply(lambda row: [row[column] for column in self.X.columns], axis=1)
        self.X_and_y["y"] = self.y.apply(lambda row: [int(row[column]) for column in self.y.columns], axis=1)
        self.X_and_y.to_csv(f"syn_data/{X_and_y_file_name}", sep = ",", index = True)
        self.X_and_y_file_name = X_and_y_file_name

    def create_X_and_y_list_mysql(self, X_and_y_file_name):
        self.X_and_y = pd.DataFrame()
        self.X_and_y["X"] = self.X.apply(lambda row: [row[column] for column in self.X.columns], axis=1)
        self.X_and_y["y"] = self.y.apply(lambda row: [int(row[column]) for column in self.y.columns], axis=1)
        self.X_and_y.to_csv(f"syn_data/{X_and_y_file_name}", sep = ";", index = True)
        self.X_and_y_file_name = X_and_y_file_name

    def read_and_initialize_data(self, feature_file_name, label_file_name, edge_file_name):
        self.read_features_col(feature_file_name)
        self.read_labels_col(label_file_name)
        self.read_edges(edge_file_name)

    def intialize_column_data(self, feature_file_name, label_file_name, edge_file_name, X_and_y_file_name):
        self.read_and_initialize_data(feature_file_name, label_file_name, edge_file_name)
        self.create_X_and_y_col(X_and_y_file_name)

    def intialize_mysql_list_data(self, feature_file_name, label_file_name, edge_file_name, X_and_y_file_name):
        self.read_and_initialize_data(feature_file_name, label_file_name, edge_file_name)
        self.create_X_and_y_list_mysql(X_and_y_file_name)

    def intialize_postgres_list_data(self, feature_file_name, label_file_name, edge_file_name, X_and_y_file_name):
        self.read_and_initialize_data(feature_file_name, label_file_name, edge_file_name)
        self.create_X_and_y_list_postgres(X_and_y_file_name)

    def intialize_neo4j_list_data(self, feature_file_name, label_file_name, edge_file_name, X_and_y_file_name):
        self.read_and_initialize_data(feature_file_name, label_file_name, edge_file_name)
        self.create_X_and_y_list_neo4j(X_and_y_file_name)