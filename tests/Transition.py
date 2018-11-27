###############################################################################
#                                                                             #
#  TRANSITION                                                                 #
#                                                                             #
###############################################################################
class Transition(object):
    def __init__(self, origin, edge, destination):
        self.origin = origin
        self.destination = destination
        self.edge = edge
        self.checked = False

    def __eq__(self, other):
        return self.origin == other.origin and self.edge == other.edge and self.destination == other.destination