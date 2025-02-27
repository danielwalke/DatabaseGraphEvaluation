from DBMSEvaluator import DBMSEvaluator
from MySQLList import MySQLList
from PostgresList import PostgresList
from Neo4jList import Neo4jList
from MySQLCol import MySQLCol
from PostgresCol import PostgresCol
from Neo4jCol import Neo4jCol

class Evaluator:
    def __init__(self):
        pass

    def evaluate(self):
        # print("Evaluate Neo4j (all features and labels in columns)")
        # neo4j_col_evaluator = DBMSEvaluator(Neo4jCol)
        # neo4j_col_evaluator.evaluate()

        # print("Evaluate Neo4j (all features and labels in lists)")
        # neo4j_list_evaluator = DBMSEvaluator(Neo4jList)
        # neo4j_list_evaluator.evaluate()

        # print("Evaluate Postgres (all features and labels in columns)")
        # postgres_col_evaluator = DBMSEvaluator(PostgresCol)
        # postgres_col_evaluator.evaluate()

        # print("Evaluate Postgres (all features and labels in lists)")
        # postgres_list_evaluator = DBMSEvaluator(PostgresList)
        # postgres_list_evaluator.evaluate()

        print("Evaluate MySQL (all features and labels in columns)")
        mysql_col_evaluator = DBMSEvaluator(MySQLCol)
        mysql_col_evaluator.evaluate()
        
        print("Evaluate MySQL (all features and labels in lists)")
        mysql_list_evaluator = DBMSEvaluator(MySQLList)
        mysql_list_evaluator.evaluate()