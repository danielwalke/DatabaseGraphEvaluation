# Evaluating batch-wise subgraph-querying of large graphs in relational and graph databases for Graph Neural Networks

## 📘 Project Overview

This project evaluates the efficiency of **relational (PostgreSQL, MySQL)** and **graph-based (Neo4j)** databases for **batch-wise subgraph querying** in **Graph Neural Network (GNN)** training. It identifies optimal backends for different GNN depths and CRUD operations, aiming to enhance memory efficiency and reduce training overhead on large-scale graphs.

---

## ✨ Key Features

- 🔍 **Subgraph Query Benchmarking**  
  Performance analysis for 1st to 3rd-order subgraph queries.  

- ⚙️ **Full CRUD Evaluation**  
  Measures Create, Read, Update, and Delete times across databases.  

- 🧪 **Synthetic and Real Datasets**  
  Includes scale-free and PPI graphs with controlled edge/node parameters.  

- 📊 **GNN-Compatible Output**  
  Outputs PyTorch Geometric–ready feature matrices and COO edge indices. 

- 🛠️ **Schema-Aware DB Setup**  
  Benchmarks both flat and list-column feature storage.

---

## 🚀 Getting Started

Clone the repository and set up your Python environment:

```bash
git clone https://github.com/danielwalke/DatabaseGraphEvaluation.git
cd DatabaseGraphEvaluation
# Optional: create virtual env
# python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

## 🛠️ Local Database Setup (Ubuntu)

This section explains how to install and configure **PostgreSQL**, **Neo4j**, and **MySQL** on Ubuntu with a unified credential scheme. Each service uses:

- **Username**: `postgres` / `neo4j` / `root`
- **Password**: `password`
- **Ports** (default):
  - PostgreSQL: `5432`
  - MySQL: `3306`
  - Neo4j: `7474 (HTTP)`, `7687 (Bolt)`

---

### 1️⃣ PostgreSQL Setup

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib -y

# Set password for the 'postgres' user
sudo -u postgres psql -c "ALTER USER postgres WITH PASSWORD 'password';"

# Restart PostgreSQL
sudo systemctl restart postgresql
```

✅ Access with:
```bash
psql -U postgres -h localhost
```

---

### 2️⃣ Neo4j Setup

```bash
# Add repository and key
wget -O - https://debian.neo4j.com/neotechnology.gpg.key | sudo gpg --dearmor -o /usr/share/keyrings/neo4j.gpg
echo "deb [signed-by=/usr/share/keyrings/neo4j.gpg] https://debian.neo4j.com stable 5" | sudo tee /etc/apt/sources.list.d/neo4j.list

# Install and start
sudo apt update
sudo apt install neo4j -y
sudo systemctl enable neo4j
sudo systemctl start neo4j
```

✅ Set password:
- Open [http://localhost:7474](http://localhost:7474)
- Login with:
  - **Username**: `neo4j`
  - **Initial Password**: `neo4j`
- You will be prompted to change it → set to `password`

---

### 3️⃣ MySQL Setup (with Local File Uploads)

```bash
sudo apt update
sudo apt install mysql-server -y

# Secure install (optional)
sudo mysql_secure_installation
```

Set password and enable `local_infile`:

```bash
sudo mysql -u root

-- Inside MySQL shell:
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
SET GLOBAL local_infile = 1;
EXIT;
```

Enable local file import permanently:

```bash
echo "[mysqld]
local_infile=1" | sudo tee -a /etc/mysql/mysql.conf.d/mysqld.cnf

sudo systemctl restart mysql
```

✅ Test with:
```bash
mysql -u root -p --local-infile=1
```

---
All three databases are now configured with consistent credentials and ready for integration with your GNN benchmarking pipeline. 🚀

## Generating synthetic datasets
1) Graphs with a fixed number of input edges:
  ```bash
   python SynthDataGeneration.py
  ```
2) Graphs with various numbers of input edges (scale-free graphs):
  ```bash
   python SynthRealDistGraphs.py
  ```


## Docu

<img src="/docu/Documentation-MainDocu.drawio.png" height="400">

1) First, main.py serves as the entry point.
2) Evaluator is executed, which performs the pre-specified number of iterations for the specified databases
3) DBMSEvaluator is an executor that iterates over all datasets

<img src="/docu/Documentation-DBEval.drawio.png" width="600">

1) DBMSEValuator executes CRUDEvaluator which executes all CRUD operations
2) The connectors represent drivers to connect to the database (A)
3) These are used in the evaluators for each database that are executed in CRUDEvaluators (B)
4) The queries used in the evaluators for all CURD operations are listed in Queries (C)
5) The data reader (E) reads all data from input files
