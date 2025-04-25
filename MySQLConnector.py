import MySQLdb

class MySQLConnector:
    def __init__(self):
        self.conn = None
        pass

    @staticmethod
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

    def connect(self, db_name = None):        
        self.conn = MySQLConnector.connect_to_mysql(db_name)
        return self.conn