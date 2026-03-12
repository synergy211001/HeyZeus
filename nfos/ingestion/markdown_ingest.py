import os
import networkx as nx

CORPUS_PATH = "docs/corpus"

graph = nx.DiGraph()

def extract_sections(file_path):
    sections = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                sections.append(line.strip("# ").strip())
    return sections


def ingest_file(file_path):
    sections = extract_sections(file_path)
    paper = os.path.basename(file_path)

    for section in sections:
        graph.add_node(section, source=paper)


def scan_corpus():
    for root, dirs, files in os.walk(CORPUS_PATH):
        for file in files:
            if file.endswith(".md"):
                ingest_file(os.path.join(root, file))


scan_corpus()

print("Nodes:", graph.number_of_nodes())
print("Edges:", graph.number_of_edges())
