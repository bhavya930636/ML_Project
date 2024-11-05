import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from scipy.sparse import csr_matrix

def load_data():
    try:
        # Attempt to load the adjacency data as a binary file
        adj_matrix = np.load('data/ind.adj', allow_pickle=True)  # Allow loading pickled data
        print(f"Loaded adjacency data size: {adj_matrix.shape}")

        # Check if the loaded data is a square matrix
        if adj_matrix.shape[0] != adj_matrix.shape[1]:
            raise ValueError(f"Adjacency matrix not square: nx,ny=({adj_matrix.shape})")

    except Exception as e:
        print(f"Failed to load the adjacency matrix: {e}")
        raise e

    # Load test node features
    try:
        test_features = np.load('data/ind.tx', allow_pickle=True)  # Allow loading pickled data
        print("Loaded test features")
        
        # Load test labels
        labels = np.load('data/ind.y', allow_pickle=True)  # Adjust as needed
        print("Loaded test labels")

    except Exception as e:
        print(f"Failed to load features/labels: {e}")
        raise e

    return adj_matrix, test_features, labels

def plot_graph(adj_matrix):
    # Create a graph from the adjacency matrix
    G = nx.from_scipy_sparse_array(csr_matrix(adj_matrix))  # Create graph from sparse matrix

    # Generate layout for visualization
    pos = nx.spring_layout(G)  # positions for all nodes

    # Draw the graph
    plt.figure(figsize=(10, 8))  # Set the figure size
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=10, font_color='black')
    plt.title("Graph Representation")
    plt.axis('off')  # Hide axes for better visualization
    plt.show()  # Display the plot

def main():
    try:
        adj_matrix, test_features, labels = load_data()
        plot_graph(adj_matrix)  # Plot the graph after loading data
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

