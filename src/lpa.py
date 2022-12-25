import random

from graph import Graph


class Lpa:

    def __init__(self, graph_file_path):
        self.graph = Graph(graph_file_path)
        self.algorithm_execution_count = 0

    def execute_algorithm(self):
        self.initialize_label_for_nodes()
        while True:
            self.algorithm_execution_count += 1
            self.propagate_labels()
            if self.algorithm_stop_condition_is_prepared():
                print('Algorithm is finished , process takes ', self.algorithm_execution_count, 'iterations')
                print(self.graph.get_nodes_and_data())
                break

    def initialize_label_for_nodes(self):  # O(n)
        for node, node_data in self.graph.get_nodes_and_data():
            self.graph.set_label_to_node(node, node)

    def propagate_labels(self):
        nodes_and_data = self.graph.get_nodes_and_data()
        for node, data in nodes_and_data:
            node_neighbours = self.graph.get_node_neighbours(node)
            maximum_label_among_neighbours = self.graph.get_maximum_label_among_nodes(node_neighbours)
            self.graph.set_label_to_node(maximum_label_among_neighbours, node)

    def algorithm_stop_condition_is_prepared(self):
        for node, data in self.graph.get_nodes_and_data():
            node_current_label = self.graph.get_node_current_label(node)
            node_neighbours = self.graph.get_node_neighbours(node)
            maximum_label_among_neighbours = self.graph.get_maximum_label_among_nodes(node_neighbours)
            if maximum_label_among_neighbours != node_current_label:
                return False
        return True

    def get_graph_as_graphical(self):
        self.graph.draw_graph()
