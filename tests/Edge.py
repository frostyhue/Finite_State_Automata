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