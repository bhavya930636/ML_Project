import torch
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Generate a synthetic adjacency matrix for document nodes (1500 nodes in this case)
# In practice, this would be derived from your dataset, where adjacency matrix[i, j] = 1 if document i is connected to document j
def generate_synthetic_adjacency_matrix(num_nodes=1500):
    # Generate a random adjacency matrix (symmetric)
    adj_matrix = np.random.randint(0, 2, size=(num_nodes, num_nodes))  # 0 or 1 indicating no or connection
    np.fill_diagonal(adj_matrix, 0)  # No self-loops (no document is connected to itself)
    adj_matrix = np.tril(adj_matrix) + np.tril(adj_matrix, -1).T  # Make it symmetric
    return adj_matrix

# Visualize the graph
def visualize_graph(adj_matrix):
    G = nx.from_numpy_array(adj_matrix)  # Convert adjacency matrix to graph (using from_numpy_array)

    # Draw the graph
    plt.figure(figsize=(12, 12))
    pos = nx.spring_layout(G, seed=42)  # Layout for positioning the nodes

    # Draw nodes and edges
    nx.draw_networkx_nodes(G, pos, node_size=50, node_color='blue', alpha=0.7)  # Document nodes in blue
    nx.draw_networkx_edges(G, pos, width=0.5, alpha=0.5, edge_color='gray')  # Edges in gray

    # Add node labels (Here, I suggest showing only the first 50 nodes for clarity, modify as needed)
    labels = {i: str(i) for i in range(50)}  # Displaying labels for the first 50 nodes for clarity
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=8, font_color='black')

    plt.title("Document Graph with Labels")
    plt.axis('off')  # Turn off axis
    plt.show()

# Main function
def main():
    num_documents = 1500  # Number of document nodes
    adj_matrix = generate_synthetic_adjacency_matrix(num_documents)  # Generate adjacency matrix
    visualize_graph(adj_matrix)  # Visualize the graph

if __name__ == "__main__":
    main()

