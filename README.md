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

## Docu
[![Alt text](images/[example.png](https://github.com/danielwalke/DatabaseGraphEvaluation/blob/main/docu/Documentation-MainDocu.drawio.png))](https://github.com/danielwalke/DatabaseGraphEvaluation/blob/main/docu/Documentation-MainDocu.drawio.png)
