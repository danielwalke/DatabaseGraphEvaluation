from neo4j import GraphDatabase

class Neo4jConnector:
    def __init__(self):
        self.driver = None
        pass

    @staticmethod
    def connect_to_neo4j(uri, user, password):
        """
        Establishes a connection to the Neo4j database.
        
        Args:
            uri (str): The URI of the Neo4j database.
            user (str): The username for authentication.
            password (str): The password for authentication.
        
        Returns:
            GraphDatabase.driver: The Neo4j driver instance for the connection.
        """
        
        return GraphDatabase.driver(uri, auth=(user, password))

    def connect(self):
        uri = f"bolt://localhost:{7687}"
        username = "neo4j"
        password = "password"
        
        self.driver = Neo4jConnector.connect_to_neo4j(uri, username, password)