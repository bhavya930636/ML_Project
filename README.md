## How to access the data
Run the Loading_data file

A folder called dataset will be loaded into your local system
Graph will be loaded and you can see the features,nodes,edges,labels(40)

Form a folder called data and in it a folder corpus
then when you run this file graph_node_labels.txt and graph_node_corpus.txt will be formed

/data/graph_node_labels.txt indicates document names, training/test split, document labels. Each line is for a document.

/data/corpus/graph_node_corpus.txt contains raw text of each document, each line is for the corresponding line in /data/graph_node_labels.txt

Loading the Dataset:

  The ogbn-arxiv dataset is loaded using PygNodePropPredDataset.
    The train, validation, and test splits are obtained.

Creating DataFrames:

  A DataFrame (df_traintest) is created to store node IDs and their respective train/valid/test labels.
    Another DataFrame (df_labels) is created to store node IDs and their labels.

Data Merging:

  The code merges the node ID mapping (nodeidx2paperid.csv) with a DataFrame containing paper titles and abstracts (new_titles_abstracts.tsv) to enrich the dataset with metadata.

Preparing Sentences:

  Sentences are created by concatenating the title and abstract for each paper.
    Labels and train/test indications are prepared for each node.

Writing to Files:

  The metadata is written to graph_node_labels.txt.
    The corpus is written to graph_node_corpus.txt.

## Cleaning the data (preprocessing text)
cleaning_text.ipynb is used to clean the title_abstractand stored in data/clean_100.txt.

## Forming graph
Then graph.ipynb is used to form the graph of words and documents and the corresponding files are stored in data/ and data/corpus/

## Train textGCN
Then we will use train.py now to run textgcn on it to find the "text" embeddings for each doc
https://github.com/yao8839836/text_gcn
https://github.com/codeKgu/Text-GCN
Link to code for textgcn

## Train GCN
gnn.ipynb is used to run GNN on citation graph loaded in loading_data file
https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/arxiv
Code to run GNN on arxiv graph
This will give us the "citation_network" embedding

Then we will predict the class using these embeddings by concatenating them or by using Neural network on them or by using ensemble learning maybe 
if we want to do ensemble then both have to be trained on classification task 

## Classes
These are the 40 classes in which we want to classify the papers
cs.AI - Artificial Intelligence
cs.AR - Hardware Architecture
cs.CC - Computational Complexity
cs.CE - Computational Engineering, Finance, and Science
cs.CG - Computational Geometry
cs.CL - Computation and Language
cs.CR - Cryptography and Security
cs.CV - Computer Vision and Pattern Recognition
cs.CY - Computers and Society
cs.DB - Databases
cs.DC - Distributed, Parallel, and Cluster Computing
cs.DL - Digital Libraries
cs.DM - Discrete Mathematics
cs.DS - Data Structures and Algorithms
cs.ET - Emerging Technologies
cs.FL - Formal Languages and Automata Theory
cs.GL - General Literature
cs.GR - Graphics
cs.GT - Computer Science and Game Theory
cs.HC - Human-Computer Interaction
cs.IR - Information Retrieval
cs.IT - Information Theory
cs.LG - Machine Learning
cs.LO - Logic in Computer Science
cs.MA - Multiagent Systems
cs.MM - Multimedia
cs.MS - Mathematical Software
cs.NA - Numerical Analysis
cs.NE - Neural and Evolutionary Computing
cs.NI - Networking and Internet Architecture
cs.OH - Other Computer Science
cs.OS - Operating Systems
cs.PF - Performance
cs.PL - Programming Languages
cs.RO - Robotics
cs.SC - Symbolic Computation
cs.SD - Sound
cs.SE - Software Engineering
cs.SI - Social and Information Networks
cs.SY - Systems and Control

Dataset taken from this paper
Open Graph Benchmark:
Datasets for Machine Learning on Graphs

paper for textgcn
Graph Convolutional Networks for Text Classification

paper for idea of combining text and citations
LEGAL CASE DOCUMENT SIMILARITY: YOU NEED BOTH
NETWORK AND TEXT ∗

APPENDIX
https://stellargraph.readthedocs.io/en/stable/demos/embeddings/metapath2vec-embeddings.html
Metapath2vec

https://stellargraph.readthedocs.io/en/stable/demos/link-prediction/gcn-link-prediction.html
GCN Link Prediction

https://graphsandnetworks.com/the-cora-dataset/
the cora dataset

https://stellargraph.readthedocs.io/en/stable/demos/basics/loading-pandas.html
loading dataa into stellargraph from pandas

https://colab.research.google.com/drive/1hXwVDXaZNORPKzLGCDuY-rFHdlj1G-ap?usp=sharing
reference gcn code

https://ogb.stanford.edu/docs/nodeprop/
load graph

https://arxiv.org/archive/cs
scrap docs


