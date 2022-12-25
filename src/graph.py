import networkx as nx


# noinspection PyMethodMayBeStatic
# as we are using networkx package
# graph class is just a wrapper !
class Graph:

    def __init__(self):
        self.graph = None

    def read_graph_from_path(self, path):
        self.graph = nx.read_edgelist(path, data=(('weight', float),))
        return self.graph

    def initialize_label_for_nodes(self):
        for node in self.graph:
            node['label'] = node

