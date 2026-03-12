import pickle
import networkx as nx

with open("data/knowledge_graph/graph.gpickle", "rb") as f:
    G = pickle.load(f)

print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())

print("\nTop central nodes:")

centrality = nx.degree_centrality(G)

for node, score in sorted(centrality.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(node, score)
