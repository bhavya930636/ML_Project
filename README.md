##How to access the data
Run the Loading_data file

A folder called dataset will be loaded into your local system
Graph will be loaded and you can see the features,nodes,edges,labels(40)
Number of nodes: 169343
Number of edges: 1166243

Go to dataset/openarxiv/mapping/nodeidx2paperid.csv.gz and extract it

Go to mappings.ipynb and run it

There we will find node to paper index mapping
node ID to paper ID

Run the titleabs.ipynb for seeing the title,abstract of papers 
these are indexed with the paper ID found in mappings.ipynb

We have to now make a graph for textgcn using the title and abstracts 
https://github.com/yao8839836/text_gcn
Link to code for textgcn
Then we run textgcn on it to find the "text" embeddings for each doc

Then we run GNN on citation graph loaded in loading_data file
https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/arxiv
Code to run GNN on arxiv graph
This will give us the "citation_network" embedding

Then we will predict the class using these embeddings by concatenating them or by using Neural network on them or by using ensemble learning maybe 
if we want to do ensemble then both have to be trained on classification task 

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


