# Research Paper Classification using Graph Networks

## Overview

This project focuses on classifying computer science research papers using a hybrid approach that combines text embeddings from **TextGCN** with embeddings from a **citation network**. The workflow involves loading, cleaning, and preprocessing data, creating graphs, and building models to generate embeddings. Various combinations of embeddings are tested to predict the paper's class, using multiple experiments to achieve optimal results.

---

## Dataset Preparation and Loading
The dataset is present in the `Data_extraction/data` folder which is made for Textgcn and the `Data_extraction/dataset` folder for GNN.
For more details refer to `Data_extraction/README.md`

## Text Embedding using Text-GCN

- **Script**: `Text-GCN-torch/main.py`  
- **Goal**:  
  Generates text-based embeddings for each document using **Text-GCN**.

### Implementations:

- **TensorFlow**: [TensorFlow Text-GCN](https://github.com/yao8839836/text_gcn)
- **PyTorch**: [PyTorch Text-GCN](https://github.com/codeKgu/Text-GCN)

---

## GCN on Citation Network

- **Notebook**: `GNN-citation/gnn.ipynb`  
- **Description**:  
  Applies a **Graph Neural Network (GNN)** to the citation graph produced during data loading, generating "citation network" embeddings.

- **Reference**: [ogbn-arxiv Examples](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/arxiv)

---

## Final Model

- **Folder**: `Final_Model`  
- **Objective**:  
  Combines embeddings from the **TextGCN** and **citation network** using operations like:
  - Concatenation
  - Addition
  - Multiplication

The combined embeddings are fed into an **Artificial Neural Network (ANN)** for classification.

---

## Training Metrics & Visualization

- **Training Panel**: [Comet Training Metrics](https://www.comet.com/kritiarora2003/textgcn/view/new/panels)

The `visualizing_graphs` folder contains all the code for generating graphs for better understanding and analysis. 

![Alt Text](./visualizing_graphs/1.jpeg)
![Alt Text](./visualizing_graphs/2.jpeg)


---

## Classes for Classification

The project classifies papers into **40 distinct classes** based on their area within Computer Science. Examples include:

- **cs.AI** - Artificial Intelligence
- **cs.CV** - Computer Vision and Pattern Recognition
- **cs.LG** - Machine Learning  

Refer to the complete list of classes in the project overview.

---

## References & Additional Resources

- **TextGCN Paper**: *Graph Convolutional Networks for Text Classification*  
- **Combining Text & Citations**: *LEGAL CASE DOCUMENT SIMILARITY: YOU NEED BOTH NETWORK AND TEXT*  

### Useful Links:

- [Metapath2vec Embeddings](https://stellargraph.readthedocs.io/en/stable/demos/embeddings/metapath2vec-embeddings.html)
- [GCN Link Prediction](https://stellargraph.readthedocs.io/en/stable/demos/link-prediction/gcn-link-prediction.html)
- [The Cora Dataset](https://graphsandnetworks.com/the-cora-dataset/)
- [StellarGraph Loading from Pandas](https://stellargraph.readthedocs.io/en/stable/demos/basics/loading-pandas.html)
- [Reference GCN Code](https://colab.research.google.com/drive/1hXwVDXaZNORPKzLGCDuY-rFHdlj1G-ap?usp=sharing)

---

Thank you for exploring this project.

---

Made with ❤️ at **IIT Bhilai**.

