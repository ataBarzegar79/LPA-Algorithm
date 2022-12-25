import networkx as nx
import random
import matplotlib.pyplot as plt


# noinspection PyMethodMayBeStatic
# as we are using networkx package
# graph class is just a wrapper !
class Graph:

    def __init__(self, graph_file_path):
        self.graph = None
        self.graph_file_path = graph_file_path
        self.read_graph_from_path()

    def read_graph_from_path(self):
        self.graph = nx.read_edgelist(self.graph_file_path, data=(('weight', float),))
        return self.graph

    def get_nodes_and_data(self):
        return self.graph.nodes.data()

    def get_node_neighbours(self, node):
        return list(self.graph.adj[node])

    def get_maximum_label_among_nodes(self, nodes):
        labels_count = dict()
        for node in nodes:
            node_label = self.graph.nodes[node]['label']
            labels_count = self.add_label_count(labels_count, node_label)
        label_with_maximum_count = [
            key for m in [max(labels_count.values())] for key, val in labels_count.items() if val == m
        ]
        return random.choice(label_with_maximum_count)

    def add_label_count(self, labels_count, label):
        if label not in labels_count:
            labels_count[label] = 0
            return labels_count
        else:
            labels_count[label] += 1
            return labels_count

    def set_label_to_node(self, label, node):
        self.graph.nodes.data()[node]['label'] = label

    def get_node_current_label(self, node):
        return self.graph.nodes.data()[node]['label']

    def draw_graph(self):  # copied from GitHub !
        node_color = [float(self.graph.nodes.data()[node]['label']) for node in self.graph]
        labels = dict([(node, node) for node, data in self.graph.nodes.data()])
        nx.draw_networkx(self.graph, node_color=node_color)
        plt.show()
