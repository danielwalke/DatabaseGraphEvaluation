from DBMSEvaluatorRouterSQLite import DBMSEvaluator, is_stable #TODO: Switch RouterSQLite
from MySQLList import MySQLList
from PostgresList import PostgresList
from Neo4jList import Neo4jList
from Neo4jListEE import Neo4jListEE
from MySQLCol import MySQLCol
from PostgresCol import PostgresCol
from SQLiteCol import SQLiteCol
from SQLiteList import SQLiteList
from Neo4jCol import Neo4jCol
from Neo4jColEE import Neo4jColEE
from NeighborLoaderList import NeighborLoaderList
from perun import monitor
import os 
import datetime

import re
import numpy as np
from scipy import stats
from collections import defaultdict

CONF_LEVEL = 0.95
STABILITY_THRESHOLD_PERCENT = 5.0
MIN_SAMPLES = 5

def normalize_dataset_name(raw_key):
    key = raw_key.lower()

    # Database
    if key.startswith("sqlite"):
        db = "SQLite"
    elif key.startswith("neo4j"):
        db = "Neo4j"
    elif key.startswith("postgres"):
        db = "Postgres"
    elif key.startswith("mysql"):
        db = "MySQL"
    else:
        db = "UnknownDB"

    # Storage/layout
    if "list" in key:
        layout = "List"
    elif "col" in key:
        layout = "Col"
    else:
        layout = "UnknownLayout"

    # Extract problem + size
    # Matches: X_and_y_1000_nodes_5
    match = re.search(r"(x_and_y_\d+_nodes_\d+)", key)
    if match:
        problem = match.group(1)
    else:
        problem = "UnknownProblem"

    return f"{db}-{layout}-{problem}"



def margin_of_error_percent(data, conf_level=CONF_LEVEL):
    n = len(data)
    if n < MIN_SAMPLES:
        return None

    mean = np.mean(data)
    std = np.std(data, ddof=1)

    if mean == 0:
        return np.inf

    stderr = std / np.sqrt(n)
    t_val = stats.t.ppf((1 + conf_level) / 2.0, n - 1)
    margin = t_val * stderr

    return (margin / mean) * 100


def database_name_from_key(key):
    return key.split('_')[0]


def generate_markdown(benchmark_data):
    grouped = defaultdict(dict)

    for dataset_key, operations in benchmark_data.items():
        db = database_name_from_key(dataset_key)
        grouped[db][dataset_key] = operations

    md = []

    for db in sorted(grouped.keys()):
        md.append(f"## Database: `{db}`\n")

        for dataset, operations in grouped[db].items():
            pretty_name = normalize_dataset_name(dataset)
            md.append(f"### Dataset: `{pretty_name}`\n")
            md.append("| Operation | n | Mean (s) | Margin of error (%) | Stable |")
            md.append("|----------|---|----------|---------------------|--------|")

            for op, values in operations.items():
                n = len(values)

                if n == 0:
                    mean_str = "—"
                    moe_str = "—"
                    stable = False
                else:
                    mean = np.mean(values)
                    moe = margin_of_error_percent(values)

                    mean_str = f"{mean:.6f}"

                    if moe is None:
                        moe_str = "—"
                    else:
                        moe_str = f"{moe:.2f}"

                    # Stability logic (explicit and honest)
                    stable = (
                        n >= MIN_SAMPLES and
                        moe is not None and
                        moe < STABILITY_THRESHOLD_PERCENT
                    )

                md.append(
                    f"| `{op}` | {n} | {mean_str} | {moe_str} | "
                    f"{'✅' if stable else '❌'} |"
                )

            md.append("")

        md.append("")

    return "\n".join(md)
    

class Evaluator:
    def __init__(self):
        pass

    #@monitor()
    def eval_neo4j_col(self,i, time_store):
        print("Evaluate Neo4j (all features and labels in columns)")
        neo4j_col_evaluator = DBMSEvaluator(Neo4jCol, time_store)
        neo4j_col_evaluator.evaluate(i)
    
    #@monitor()
    def eval_neo4j_list(self,i, time_store):
        print("Evaluate Neo4j (all features and labels in lists)")
        neo4j_list_evaluator = DBMSEvaluator(Neo4jList, time_store)
        neo4j_list_evaluator.evaluate(i)

    #@monitor()
    def eval_neo4j_ee_col(self,i, time_store):
        print("Evaluate Neo4j EE (all features and labels in columns)")
        neo4j_col_evaluator = DBMSEvaluator(Neo4jColEE, time_store)
        neo4j_col_evaluator.evaluate(i)
    
    #@monitor()
    def eval_neo4j_ee_list(self,i, time_store):
        print("Evaluate Neo4j EE (all features and labels in lists)")
        neo4j_list_evaluator = DBMSEvaluator(Neo4jListEE, time_store)
        neo4j_list_evaluator.evaluate(i)

    #@monitor()
    def eval_mysql_col(self,i, time_store):
        print("Evaluate MySQL (all features and labels in columns)")
        mysql_col_evaluator = DBMSEvaluator(MySQLCol, time_store)
        mysql_col_evaluator.evaluate(i)

    #@monitor()
    def eval_mysql_list(self,i, time_store):
        print("Evaluate MySQL (all features and labels in lists)")
        mysql_list_evaluator = DBMSEvaluator(MySQLList, time_store)
        mysql_list_evaluator.evaluate(i)

    #@monitor()
    def eval_postgres_col(self,i, time_store):
        print("Evaluate Postgres (all features and labels in columns)")
        postgres_col_evaluator = DBMSEvaluator(PostgresCol, time_store)
        postgres_col_evaluator.evaluate(i)

    #@monitor()
    def eval_postgres_list(self,i, time_store):
        print("Evaluate Postgres (all features and labels in lists)")
        postgres_list_evaluator = DBMSEvaluator(PostgresList, time_store)
        postgres_list_evaluator.evaluate(i)

    #@monitor()
    def eval_sqlite_col(self,i, time_store):
        print("Evaluate SQLite (all features and labels in columns)")
        sqlite_col_evaluator = DBMSEvaluator(SQLiteCol, time_store)
        sqlite_col_evaluator.evaluate(i)

    #@monitor()
    def eval_sqlite_list(self,i, time_store):
        print("Evaluate SQLite (all features and labels in lists)")
        sqlite_list_evaluator = DBMSEvaluator(SQLiteList, time_store)
        sqlite_list_evaluator.evaluate(i)

    def eval_neighborloader_list(self,i, time_store):
        print("Evaluate Neighborloader (all features and labels in lists)")
        neighborloader_list_evaluator = DBMSEvaluator(NeighborLoaderList, time_store)
        neighborloader_list_evaluator.evaluate(i)

    def evaluate(self):
        time_store = dict()
        num_iterations = 30 #2
        print(os.getcwd())
        files = os.listdir("results")
        files = list(filter(lambda f: ".csv" in f, files))
        file_numbers = list(map(lambda f: int(f.split(".")[0].split("_")[-1]), files))
        off_set = 0 if len(files) == 0 else (max(file_numbers) + 1)
        for i in range(off_set, num_iterations + off_set):
            #self.eval_neighborloader_list(i)
            # self.eval_sqlite_list(i, time_store)
            # self.eval_sqlite_col(i, time_store)
            
            self.eval_neo4j_col(i, time_store)
            self.eval_neo4j_list(i, time_store)

            self.eval_neo4j_ee_col(i, time_store)
            self.eval_neo4j_ee_list(i, time_store)
            
            # self.eval_postgres_col(i, time_store)
            # self.eval_postgres_list(i, time_store)
    
            # self.eval_mysql_col(i, time_store)
            # self.eval_mysql_list(i, time_store)

            print(20*"_")
            print(generate_markdown(time_store))
            print(20*"_")
        now = datetime.datetime.now()
        print(str(now))

            
            
        

        

        
        
        