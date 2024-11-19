# Hybrid Classification: TextGCN & GNN Embeddings  

This project combines embeddings from **TextGCN** and **GNN** models for document classification.  

## Files Overview  

1. **`f_model.ipynb`**: Combines and classifies using TextGCN and GNN embeddings.  
2. **`gnn_train_f.ipynb`**: Generates GNN embeddings, saved as `gnn_embeddings.pt`.  
3. **`second_last_layer_embeddings.zip`**: Contains TextGCN embeddings.  

## Workflow  

1. **GNN Embeddings**:  
   - Extracted from `gnn_embeddings.pt` (generated via `gnn_train_f.ipynb`).  
   - Node indices mapped using `Data_extraction/cleaning_text.ipynb`.  

2. **TextGCN Embeddings**:  
   - Load from `second_last_layer_embeddings.zip`.  
   - Use the first 1500 embeddings for documents (remaining are word embeddings).  

3. **Classification**:  
   - Combine embeddings in `f_model.ipynb` to generate predictions.  

---  
