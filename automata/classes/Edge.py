from State import *
###############################################################################
#                                                                             #
#  EDGE                                                                       #
#                                                                             #
###############################################################################

class Edge(object):

    def __init__(self, label, destination):
        self.edge_label = label
        self.edge_destination = State(name=destination)

    def __eq__(self, other):
        return self.edge_destination.state_name == other.edge_destination.state_name and self.edge_label == other.edge_label

    # Method returning the token as a string when printed.
    def __str__(self):
        return 'Edge({label}, {destination})'.format(label=self.edge_label, destination=self.edge_destination)

    def __repr__(self):
        return self.__str__()
