###############################################################################
#                                                                             #
#  State                                                                      #
#                                                                             #
###############################################################################

class State(object):

    def __init__(self, name):
        self.state_name = name
        self.state_edges = []
        self.final = False

    def __eq__(self, other):
        return self.state_edges == other.state_edges and self.state_name == other.state_name and self.final == other.final

    def add_edge(self, edge):
        self.state_edges.append(edge)

