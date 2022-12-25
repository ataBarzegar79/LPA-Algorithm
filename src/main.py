from lpa import Lpa

if __name__ == '__main__':
    algorithm = Lpa('./sample/karate_club.txt')
    algorithm.execute_algorithm()
    algorithm.get_graph_as_graphical()
