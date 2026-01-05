from Neo4jConnectorEE import Neo4jConnectorEE

def get_node_count(tx):
    result = tx.run("MATCH (n) RETURN count(n) AS node_count")
    return result.single()["node_count"]
    
conn = Neo4jConnectorEE()
conn.connect()
with conn.driver.session() as session:
    count = session.execute_read(get_node_count)
    print(count)

from Neo4jConnector import Neo4jConnector

def get_node_count(tx):
    result = tx.run("MATCH (n) RETURN count(n) AS node_count")
    return result.single()["node_count"]
    
conn = Neo4jConnector()
conn.connect()
with conn.driver.session() as session:
    count = session.execute_read(get_node_count)
    print(count)