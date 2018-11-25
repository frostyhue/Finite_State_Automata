###############################################################################
#                                                                             #
#  TOKEN CLASS                                                                #
#                                                                             #
###############################################################################

class Token(object):

    # Method that whenever an object of the class has been created, assigns the values asked to their corresponding values(base method in python).
    def __init__(self, value, type):
        self.type = type
        self.value = value

    # Method returning the token as a string(base method in python).
    def __str__(self):
        return 'Token({value}, {type})'.format(type=self.type, value = self.value)

    def __eq__(self, other):
        return self.type == other.type and self.value == other.value

    # Method returning the token as a string(base method in python).
    def __repr__(self):
        return self.__str__()