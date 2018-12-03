###############################################################################
#                                                                             #
#  State                                                                      #
#                                                                             #
###############################################################################

class State(object):

    def __init__(self, name):
        self.state_name = name
        self.state_edges = []

    def __eq__(self, other):
        return self.state_edges == other.state_edges and self.state_name == other.state_name

    def add_edge(self, edge):
        self.state_edges.append(edge)

