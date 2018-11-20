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
        return 'Token({type}, {value})'.format(type=self.type, value = self.value)

    # Method returning the token as a string(base method in python).
    def __repr__(self):
        return self.__str__()