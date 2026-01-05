import sqlite3
import os

class SQLiteConnector:
    """
    Handles the connection to a SQLite database.
    """
    def __init__(self):
        self.conn = None

    def connect(self, db_name="sqlite.db"):
        """
        Connect to the SQLite database server.
        If the database does not exist, it will be created.

        Args:
            db_name (str): The name of the database file.

        Returns:
            sqlite3.Connection: The connection object.
        """
        try:
            # The directory for the database is created if it doesn't exist.
            db_dir = os.path.dirname(db_name)
            if db_dir and not os.path.exists(db_dir):
                os.makedirs(db_dir)

            conn = sqlite3.connect(db_name)
            print(f"Connection to {db_name} successful.")
            return conn
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def close_connection(self):
        """Closes the current database connection if it is open."""
        if self.conn:
            self.conn.close()
            self.conn = None
            print("Connection closed.")

