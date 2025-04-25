from DBMSEvaluatorRouter import DBMSEvaluator
from MySQLList import MySQLList
from PostgresList import PostgresList
from Neo4jList import Neo4jList
from MySQLCol import MySQLCol
from PostgresCol import PostgresCol
from Neo4jCol import Neo4jCol
from perun import monitor

class Evaluator:
    def __init__(self):
        pass

    #@monitor()
    def eval_neo4j_col(self,i):
        print("Evaluate Neo4j (all features and labels in columns)")
        neo4j_col_evaluator = DBMSEvaluator(Neo4jCol)
        neo4j_col_evaluator.evaluate(i)
    
    #@monitor()
    def eval_neo4j_list(self,i):
        print("Evaluate Neo4j (all features and labels in lists)")
        neo4j_list_evaluator = DBMSEvaluator(Neo4jList)
        neo4j_list_evaluator.evaluate(i)

    #@monitor()
    def eval_mysql_col(self,i):
        print("Evaluate MySQL (all features and labels in columns)")
        mysql_col_evaluator = DBMSEvaluator(MySQLCol)
        mysql_col_evaluator.evaluate(i)

    #@monitor()
    def eval_mysql_list(self,i):
        print("Evaluate MySQL (all features and labels in lists)")
        mysql_list_evaluator = DBMSEvaluator(MySQLList)
        mysql_list_evaluator.evaluate(i)

    #@monitor()
    def eval_postgres_col(self,i):
        print("Evaluate Postgres (all features and labels in columns)")
        postgres_col_evaluator = DBMSEvaluator(PostgresCol)
        postgres_col_evaluator.evaluate(i)

    #@monitor()
    def eval_postgres_list(self,i):
        print("Evaluate Postgres (all features and labels in lists)")
        postgres_list_evaluator = DBMSEvaluator(PostgresList)
        postgres_list_evaluator.evaluate(i)

    def evaluate(self):
        num_iterations = 30
        off_set = 0
        for i in range(off_set, num_iterations + off_set):
            self.eval_neo4j_col(i)
            self.eval_neo4j_list(i)
            
            self.eval_postgres_col(i)
            self.eval_postgres_list(i)
    
            self.eval_mysql_col(i)
            self.eval_mysql_list(i)
        

        

        
        
        