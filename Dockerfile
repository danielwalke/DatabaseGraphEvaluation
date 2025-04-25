FROM neo4j:latest

# Install Python
RUN apt-get update && apt-get install -y python3 python3-pip

# Set Python3 as default
RUN ln -s /usr/bin/python3 /usr/bin/python

# Ensure APOC is installed (optional, depending on your needs)
RUN mkdir -p /plugins && \
    curl -L https://github.com/neo4j-contrib/neo4j-apoc-procedures/releases/latest/download/apoc-extended.jar -o /plugins/apoc.jar

# Expose necessary ports
EXPOSE 7474 7473 7687
