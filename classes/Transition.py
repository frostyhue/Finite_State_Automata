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

    # Method returning the token as a string whenever the object if printed.
    def __str__(self):
        return 'Transition({origin}, {edge}, {destination})'.format(origin=self.origin, destination=self.destination, \
                                                               edge=self.edge)

    def __repr__(self):
        return self.__str__()
