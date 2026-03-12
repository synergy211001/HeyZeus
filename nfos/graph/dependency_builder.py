import os
import networkx as nx

CORPUS_PATH = "docs/corpus"

graph = nx.DiGraph()

concepts = set()

def collect_concepts():
    for root, dirs, files in os.walk(CORPUS_PATH):
        for file in files:
            if file.endswith(".md"):
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    for line in f:
                        if line.startswith("#"):
                            concept = line.strip("# ").strip()
                            concepts.add(concept)
                            graph.add_node(concept)

def detect_dependencies():
    for root, dirs, files in os.walk(CORPUS_PATH):
        for file in files:
            if file.endswith(".md"):
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    text = f.read()

                for concept in concepts:
                    if concept in text:
                        for other in concepts:
                            if other != concept and other in text:
                                graph.add_edge(other, concept)

collect_concepts()
detect_dependencies()

print("Nodes:", graph.number_of_nodes())
print("Edges:", graph.number_of_edges()) 

import pickle

with open("data/knowledge_graph/graph.gpickle", "wb") as f:
    pickle.dump(graph, f)
