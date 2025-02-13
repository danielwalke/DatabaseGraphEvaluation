import psycopg2

class PostgresConnector:
    def __init__(self):
        self.conn = None
        pass

    @staticmethod
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

    def connect(self, db_name = None):        
        self.conn = PostgresConnector.connect_to_postgres(db_name)
        return self.conn