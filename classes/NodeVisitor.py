###############################################################################
#                                                                             #
#  NodeVisitor                                                                #
#                                                                             #
###############################################################################


# The NodeVisitor class is used to be the base of the Interpreter.
class NodeVisitor(object):

    """
    Method that distinguishes the node type and depending on it,
    returns the function that should be used to handle the node type.
    """
    def visit(self, node):
        node_type = type(node).__name__
        if node_type == 'Letter':
            return self.visit_Letter(node)

        elif node_type == 'Repeat':
            return self.visit_Repeat(node)

        elif node_type == 'TransitionOp':
            return self.visit_TransitionOp(node)

        elif node_type == 'ET':
            return self.visit_ET(node)

    def generic_visit(self, node):
        raise Exception("No visit_{} method".format(type(node).__name__))
