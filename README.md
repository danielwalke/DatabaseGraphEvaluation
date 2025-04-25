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

## Docu

<img src="/docu/Documentation-MainDocu.drawio.png" height="400">

1) First, main.py serves as entry point.
2) Evaluator is executed which performs the pre-specified number of iterations for the specified databases
3) DBMSEvaluator is executor that iterates over all datasets

<img src="/docu/Documentation-DBEval.drawio.png" height="600">
1) DBMSEValuator executes CRUDEvaluator which executes all CRUD operations
2) The connectors represent drivers to connect to the database (A)
3) These are used in the evaluators for each database that are executed in CRUDEvaluators (B)
4) The queries used in the evaluators for all CURD operations are listed in Queries (C)
5) The data reader (E) reads all data from input files
