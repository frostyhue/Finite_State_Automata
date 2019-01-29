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

    # Method returning the token as a string whenever the object if printed.
    def __str__(self):
        return 'State({name}, {edges}, {final})'.format(name=self.state_name, edges=self.state_edges, final=self.final)

    def __repr__(self):
        return self.__str__()

    def add_edge(self, edge):
        self.state_edges.append(edge)
