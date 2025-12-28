import networkx as nx
import matplotlib.pyplot as plt

# Create graph
G = nx.Graph()
G.add_nodes_from(["Library", "Dorm", "Cafeteria", "Engineering Building"])
G.add_edges_from([
    ("Library", "Dorm"),
    ("Library", "Cafeteria"),
    ("Dorm", "Engineering Building"),
    ("Cafeteria", "Engineering Building")
])

# Print all nodes (debugging step)
print("Nodes in graph:", G.nodes())

# Find the shortest path
path = nx.shortest_path(G, source="Dorm", target="Cafeteria")
print("Fastest route:", path)

# Draw graph
nx.draw(G, with_labels = True,  node_color="lightgreen", node_size=2000, font_size=10)


S = nx.Graph()
S.add_nodes_from(['Computer Science Building', 'Heavenor', 'Libery', "Civil Building", 'Tj hall',])
S.add_edges_from([
    ('Tj hall', 'Computer Science Building')
])
plt.show()