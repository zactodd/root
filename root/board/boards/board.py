import networkx as nx
from root.board.clearing import Clearing
import json


class Board:
    """Class for holding Graph information about board"""

    def __init__(self, graph_json):
        self.clearings = []
        self.graph = self._read_graph_json(graph_json)

    def _read_graph_json(self, graph_json):
        with open(graph_json) as f:
            graph_json = json.load(f)
        g = nx.Graph()
        for src, targets in graph_json["edges"].items():
            g.add_edges_from((src, targets))
            self.clearings.append(Clearing(idx=src, **graph_json["nodes"]))


