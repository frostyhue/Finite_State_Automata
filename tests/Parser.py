from Lexer import *

###############################################################################
#                                                                             #
#  PARSER                                                                     #
#                                                                             #
###############################################################################

class Parser(object):


    def __init__(self, lexer):
        self.lexer = lexer
        self.tokens_list = lexer.lex()
        self.current_token = self.tokens_list[0]

    # Method that raises and error.
    def error(self):
        print('Expression is incorrect!')

    # Method that goes to the next token if the current one has already been processed.
    def pop_token(self, token_type):
        if self.current_token.type == token_type:
            if not self.lexer.expr_end():
                self.current_token = self.lexer.get_next_token()
        else:
            self.error()
