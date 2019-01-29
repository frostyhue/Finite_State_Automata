###############################################################################
#                                                                             #
#  OPERATIONS                                                                 #
#                                                                             #
###############################################################################


# AST class that when finished being iterated through, continues to the next one.
class AST(object):
    pass


# Contingency Operation base.
class TransitionOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

    def __str__(self):
        return str("TransitionOp({left}, {op}, {right})".format(left=self.left, op=self.op, right=self.right))

# Preposition base.
class Letter(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

    def __str__(self):
        return str("Letter({token}, {value})".format(token=self.token, value=self.value))


# Preposition base.
class ET(AST):
    def __init__(self, symbol):
        self.symbol = symbol

    def __str__(self):
        return str("ET({token}, {value})".format(token=self.symbol.token, value=self.symbol.value))

# Contradiction Operation base.
class Repeat(AST):
    def __init__(self, op, letter):
        self.token = self.op = op
        self.letter = letter

    def __str__(self):
        return str("Repeat({op}, {prep})".format(op=self.op, prep=self.letter))
