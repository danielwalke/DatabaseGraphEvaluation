import os
import csv

os.makedirs("syn_data", exist_ok=True)

with open("syn_data/X_and_y_1000_nodes_5_edges_sqlite_list.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["col1", "col2"])
    writer.writerow([1, 2])
