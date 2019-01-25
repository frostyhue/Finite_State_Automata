from Parser import *
from NodeVisitor import *

###############################################################################
#                                                                             #
#  INTERPRETER                                                                #
#                                                                             #
###############################################################################

"""The interpreter class that inherits from the class NodeVisitor and contains all of the logic
        for visiting each node type and returning the final version of the expression 
                                depending on the desired type."""

class Interpreter(NodeVisitor):

    """Method that whenever an object of the class has been created,
    assigns the values asked to their corresponding variables(base method in python)."""
    def __init__(self, parser):
        self.parser = parser

    # Method that processes the node and returns the format for the Contingency Operations for both expression.
    def visit_TransitionOp(self, node):
        return '(' + str(self.visit(node.left)) + str(node.op.value) + str(self.visit(node.right)) + ')'

    # Method that processes the node and returns the format for the Conditional Operations for the boolean expression.
    def visit_Repeat(self, node):
        return str(self.visit(node.letter)) + str(node.op.value)

    # Method that processes the node and returns the format for the Preposition for both expression.
    def visit_Letter(self, node):
        return str(node.value)

    # Method that processes the node and returns the format for the Preposition for both expression.
    def visit_ET(self, node):
        return str(node.symbol.value)

    # Method that returns the final AST tree for the infix expression notation.
    def interpret(self):
        tree = self.parser.parse_regex()
        return self.visit(tree)
