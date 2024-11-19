Here's a more visually engaging version of your markdown for GitHub, complete with emojis for extra appeal:

---

# 🚀 Research Paper Classification using Graph Networks 📚🔗

## 🌟 Overview

This project focuses on classifying computer science research papers using a hybrid approach, combining text embeddings from **TextGCN** and embeddings from the **citation network**. The workflow involves loading, cleaning, and preprocessing data, creating graphs, and building models to generate embeddings. Finally, various combinations of embeddings are tested to predict the paper's class. 🎉

---

## 📂 Dataset Preparation and Loading

### 🔍 Data Extraction

- **📂 Path:** `Data_extraction/loading_data.py`  
- **Description:**  
  This script extracts and loads the **ogbn-arxiv** dataset, a graph dataset representing computer science papers with nodes, features, edges, and 40-class labels. 🧩

1. **Step-by-Step Process**:
   - Creates a `dataset` folder containing `ogbn-arxiv` data.
   - Displays nodes, features, edges, and labels for the graph.
2. **Folder Structure**:
   - `/data/graph_node_labels.txt`: Contains document names, training/test splits, and labels for each document.
   - `/data/corpus/graph_node_corpus.txt`: Raw text of each document, corresponding to the labels.

### 📦 Dataset Loading

- **Library**: `PygNodePropPredDataset`  
- **Splits**: Data is divided into **train**, **validation**, and **test** sets.

### 🗂️ Creating DataFrames

1. **DataFrames Created**:
   - `df_traintest`: Maps node IDs to their corresponding train/valid/test labels.
   - `df_labels`: Maps node IDs to their class labels.

2. **Data Merging**:
   - Merges `nodeidx2paperid.csv` with `new_titles_abstracts.tsv` for additional metadata.

### ✍️ Preparing Sentences & Writing Files

- Concatenates titles and abstracts for each paper.
- Writes metadata to `graph_node_labels.txt`.
- Writes the text corpus to `graph_node_corpus.txt`.

---

## 🧹 Data Cleaning

- **📓 Notebook**: `Data_extraction/cleaning_text.ipynb`  
- **Purpose**:  
  Cleans and processes text data (titles and abstracts) and stores the results in `Data_extraction/data/clean_100.txt`.

---

## 🕸️ Graph Formation

- **📓 Notebook**: `Data_extraction/graph.ipynb`  
- **Functionality**:  
  Builds a graph of words and documents. Outputs are stored in:
  - `Data_extraction/data/`
  - `Data_extraction/data/corpus/`

---

## 🧠 Text Embedding using Text-GCN

- **📜 Script**: `Text-GCN-torch/main.py`  
- **Goal**:  
  Runs **Text-GCN** to generate text-based embeddings for each document. 📄🔗

### ⚙️ Implementations

- **TensorFlow**: [TensorFlow Text-GCN](https://github.com/yao8839836/text_gcn)
- **PyTorch**: [PyTorch Text-GCN](https://github.com/codeKgu/Text-GCN)

---

## 🔗 GCN on Citation Network

- **📓 Notebook**: `GNN-citation/gnn.ipynb`  
- **Description**:  
  Applies a **Graph Neural Network (GNN)** to the citation graph from the data-loading step to produce "citation network" embeddings. 📑🌐

- **Reference**: [ogbn-arxiv Examples](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/arxiv)

---

## 🏆 Final Model

- **📂 Folder**: `Final_Model`  
- **Objective**:  
  Combines embeddings from **TextGCN** and the **citation network** using various operations:
  - 🔗 **Concatenation**
  - ➕ **Addition**
  - ✖️ **Multiplication**

- **Model**: An **Artificial Neural Network (ANN)** is used for final classification. 🤖

---

## 📊 Training Metrics & Visualization

- **Training Panel**: [Comet Training Metrics](https://www.comet.com/kritiarora2003/textgcn/view/new/panels)

---

## 🎓 Classes for Classification

This project classifies papers into **40 distinct classes**. Each class represents a specialized area of Computer Science. Examples include:

- **cs.AI** - Artificial Intelligence 🤖
- **cs.CV** - Computer Vision and Pattern Recognition 📸
- **cs.LG** - Machine Learning 🔍  
*(Refer to the full list [here](#classes))*  

---

## 📚 References & Additional Resources

- **TextGCN Paper**: *Graph Convolutional Networks for Text Classification*  
- **Combining Text & Citations**: *LEGAL CASE DOCUMENT SIMILARITY: YOU NEED BOTH NETWORK AND TEXT*  

### 📖 Useful Links:

- [Metapath2vec Embeddings](https://stellargraph.readthedocs.io/en/stable/demos/embeddings/metapath2vec-embeddings.html)
- [GCN Link Prediction](https://stellargraph.readthedocs.io/en/stable/demos/link-prediction/gcn-link-prediction.html)
- [The Cora Dataset](https://graphsandnetworks.com/the-cora-dataset/)
- [StellarGraph Loading from Pandas](https://stellargraph.readthedocs.io/en/stable/demos/basics/loading-pandas.html)
- [Reference GCN Code](https://colab.research.google.com/drive/1hXwVDXaZNORPKzLGCDuY-rFHdlj1G-ap?usp=sharing)

---

**Thank you for exploring this project!** ✨📈

---


