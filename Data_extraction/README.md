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
