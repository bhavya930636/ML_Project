import networkx as nx
import matplotlib.pyplot as plt
import os

# Define the folder containing the data files
data_folder = 'data'

# Load labels
with open(os.path.join(data_folder, '1500_labels.txt'), 'r') as f:
    labels = f.read().splitlines()

# Load sentences
with open(os.path.join(data_folder, '1500_sentences_clean.txt'), 'r') as f:
    sentences = f.read().splitlines()

# Load vocabulary
with open(os.path.join(data_folder, '1500_vocab.txt'), 'r') as f:
    vocab = f.read().splitlines()

# Initialize the graph
G = nx.Graph()

# Add nodes for documents (with prefix 'doc_') and words (with prefix 'word_')
doc_nodes = [f'doc_{i}' for i in range(len(sentences))]
word_nodes = [f'word_{word}' for word in vocab]
G.add_nodes_from(doc_nodes, type='document')
G.add_nodes_from(word_nodes, type='word')

# Build edges based on word occurrences in each document
for doc_index, sentence in enumerate(sentences):
    words = sentence.split()
    for word in words:
        if word in vocab:
            G.add_edge(f'doc_{doc_index}', f'word_{word}')

# Visualize the graph
plt.figure(figsize=(12, 12))

# Define colors for documents and words
node_colors = []
node_sizes = []
for node in G.nodes():
    if G.nodes[node]['type'] == 'document':
        node_colors.append('skyblue')  # Documents in sky blue
        node_sizes.append(50)  # Smaller size for document nodes
    else:
        node_colors.append('lightcoral')  # Words in light coral
        node_sizes.append(10)  # Smaller size for word nodes

# Positioning and drawing
pos = nx.spring_layout(G, seed=42, k=0.1)  # Use spring layout for better spacing
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, alpha=0.7)
nx.draw_networkx_edges(G, pos, width=0.2, alpha=0.5)

# Hide axis and show the plot
plt.axis('off')
plt.show()

