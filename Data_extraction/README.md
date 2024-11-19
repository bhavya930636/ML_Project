
### Data Extraction

- **Path:** `Data_extraction/loading_data.py` 
- **Description:** 
  The script extracts and loads the **ogbn-arxiv** dataset, a graph dataset that represents computer science papers through nodes, features, edges, and 40-class labels.

#### Step-by-Step Process:
1. Creates a `dataset` folder containing `ogbn-arxiv` data.
2. Loads the graph data, displaying nodes, features, edges, and labels.
   
#### Folder Structure:
- `/data/graph_node_labels.txt`: Contains document names, training/test splits, and labels for each document.
- `/data/corpus/graph_node_corpus.txt`: Raw text of each document, aligned with the labels.

### Dataset Loading

- **Library**: `PygNodePropPredDataset`  
- The dataset is split into **train**, **validation**, and **test** sets.

### Creating DataFrames

1. **DataFrames Created**:
   - `df_traintest`: Contains node IDs and their respective train/valid/test labels.
   - `df_labels`: Contains node IDs and their corresponding class labels.

2. **Data Merging**:
   - Merges `nodeidx2paperid.csv` with `new_titles_abstracts.tsv` to enrich the dataset with additional metadata.

### Preparing Sentences & Writing Files

- Titles and abstracts for each paper are concatenated into sentences.
- Metadata is written to `graph_node_labels.txt`.
- Text corpus is saved in `graph_node_corpus.txt`.

---

## Data Cleaning

- **Notebook**: `Data_extraction/cleaning_text.ipynb`  
- **Purpose**:  
  This step cleans and processes text data (titles and abstracts) and stores the cleaned data in `Data_extraction/data/clean_100.txt`.

---

## Graph Formation

- **Notebook**: `Data_extraction/graph.ipynb`  
- **Functionality**:  
  Constructs a graph of words and documents, with results saved in:
  - `Data_extraction/data/`
  - `Data_extraction/data/corpus/`

---
