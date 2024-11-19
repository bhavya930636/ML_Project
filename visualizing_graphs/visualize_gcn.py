import torch
import matplotlib.pyplot as plt
import networkx as nx

# Function to visualize the graph with word and document nodes
def visualize_graph(adj_matrix, num_nodes=1500, word_nodes=1000, doc_nodes=500):
    # Create a graph from the adjacency matrix
    G = nx.from_numpy_array(adj_matrix.numpy())  # Convert adjacency matrix to graph using from_numpy_array

    # Create a random layout for the nodes
    pos = nx.spring_layout(G, seed=42)  # You can use different layouts like circular_layout, random_layout, etc.

    # Define node types
    word_node_range = range(word_nodes)  # First 1000 nodes are word nodes
    doc_node_range = range(word_nodes, word_nodes + doc_nodes)  # Next 500 nodes are document nodes

    # Create color mapping: word nodes are blue, doc nodes are green
    node_colors = ['blue' if i < word_nodes else 'green' for i in range(num_nodes)]

    # Create size mapping: word nodes are smaller, doc nodes are larger
    node_sizes = [50 if i < word_nodes else 300 for i in range(num_nodes)]  # Increase size for document nodes

    # Draw the graph
    plt.figure(figsize=(12, 12))  # Adjust the size of the plot
    nx.draw(G, pos, with_labels=True, node_size=node_sizes, font_size=6, font_color='black', node_color=node_colors, alpha=0.7)

    # Display the graph
    plt.title("Graph Visualization with Word and Document Nodes")
    plt.show()

# Step 1: Define a function to generate synthetic data
def generate_synthetic_data(word_nodes=1000, doc_nodes=500):
    # Create a random adjacency matrix for word and document nodes
    adj_matrix = torch.randint(0, 2, (word_nodes + doc_nodes, word_nodes + doc_nodes), dtype=torch.float)

    # Connect document nodes to word nodes (randomly, for illustration purposes)
    for i in range(word_nodes, word_nodes + doc_nodes):
        for j in range(word_nodes):
            if torch.rand(1).item() > 0.8:  # 80% chance a document connects to a word
                adj_matrix[i, j] = 1
                adj_matrix[j, i] = 1  # Ensure the graph is undirected

    # Add self-loops to the adjacency matrix (optional)
    adj_matrix = adj_matrix + torch.eye(word_nodes + doc_nodes)

    return adj_matrix

# Step 2: Main function to visualize the graph
if __name__ == "__main__":
    word_nodes = 1000  # Number of word nodes
    doc_nodes = 500    # Number of document nodes
    num_nodes = word_nodes + doc_nodes  # Total nodes
    adj_matrix = generate_synthetic_data(word_nodes, doc_nodes)  # Generate synthetic adjacency matrix
    visualize_graph(adj_matrix, num_nodes, word_nodes, doc_nodes)  # Visualize the graph

