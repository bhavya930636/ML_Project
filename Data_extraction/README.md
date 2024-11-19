
# Data Extraction and Preparation

## **1. Data Extraction**
**Script**: `Data_extraction/loading_data.py`

### **Steps:**

### **Dataset Download & Loading:**
1. Install the required packages:
   ```bash
   # Install dependencies
   pip install ogb
   pip install torch torchvision torchaudio
   pip install torch-scatter torch-sparse torch-cluster torch-spline-conv torch-geometric
   
2. Load the **ogbn-arxiv** dataset:
   - Represents computer science papers as graph nodes with features, edges, and 40-class labels.
   - The dataset is split into **train**, **validation**, and **test** sets.

3. Save the dataset:
   - Creates a `dataset` folder containing the `ogbn-arxiv` data.
   - Loads and displays graph data, including nodes, features, edges, and labels.

---

### **Metadata Enrichment:**
- **Files Used:**
  - `nodeidx2paperid.csv`
  - `new_titles_abstracts.tsv`
- Merge these files to map node IDs to paper IDs and enrich the dataset with metadata:
  - **Columns**:
    - `paper id`
    - `title`
    - `abstract`
- Example:
  | paper id | title                                     | abstract                                                                 |
  |----------|-------------------------------------------|-------------------------------------------------------------------------|
  | 200971   | ontology as a source for rule generation | This paper discloses the potential of OWL (Web Ontology Language)...   |
  | 549074   | a novel methodology for thermal analysis  | The semiconductor industry is reaching a fascinating...               |
  | ...      | ...                                       | ...                                                                   |

- Node ID mapping example:
  | node idx | paper id  |
  |----------|-----------|
  | 0        | 9657784   |
  | 1        | 39886162  |
  | ...      | ...       |

---

## **2. Creating DataFrames**
**Purpose**: Organize data into meaningful structures.

### **DataFrames Created**:
1. **`df_traintest`**:
   - Contains `node ID` and their respective **train/valid/test** split labels.
2. **`df_labels`**:
   - Contains `node ID` and their respective **class labels**.

---

## **3. Preparing Sentences & Files**
- Titles and abstracts of papers are concatenated into full sentences.
- Metadata written to:
  - **`data/all_labels.txt`**: Contains `node ID`, split, and class label.
  - **`data/corpus/all_corpus.txt`**: Raw text corpus aligned with the labels.

---

# Data Cleaning

## **Notebook**: `Data_extraction/cleaning_text.ipynb`

### **Purpose**:
- Clean and process text data (titles and abstracts) for 1500 nodes.

### **Outputs**:
1. **Cleaned Data**:
   - Saved as `Data_extraction/data/clean_1500.txt`.
   - Uses the text corpus from `data/corpus/all_corpus.txt`.

2. **Vocabulary Generation**:
   - Copy node indices from this notebook.
   - Paste into `data/graph.ipynb`.
   - Creates `data/corpus/vocab_1500.txt` by combining all words from the cleaned text corpus.

---

# Instructions for Running Code:
1. Run `Data_extraction/loading_data.py` to download, merge, and process metadata.
2. Run `Data_extraction/cleaning_text.ipynb` to clean and process text data.
3. In `data/graph.ipynb`, run the cells up to the point where `vocab_1500.txt` is created.
```
