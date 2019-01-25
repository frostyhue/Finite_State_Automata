import re
import sys
from Token import *
from Token_Regex import *

###############################################################################
#                                                                             #
#  LEXER                                                                      #
#                                                                             #
###############################################################################

class Lexer(object):


    # The constructor of the Lexer class that makes the setup for the other methods.
    def __init__(self):
        self.token_expressions = token_expressions
        self.pos = 0
        self.tokens = []
        self.current_token = ''

    # Method that divides the expression into Tokens.
    def lex(self, expression):
        self.pos = 0
        pos = 0
        tokens = []
        while pos < len(expression):
            match = None
            for token_expr in self.token_expressions:
                pattern, type = token_expr[0], token_expr[1]
                regex = re.compile(pattern)
                match = regex.match(expression, pos)
                if match:
                    value = match.group(0)
                    if type:
                        tokens.append(Token(value, type))
                    break
            if not match:
                sys.stderr.write('Illegal character: {}\n'.format(expression[pos]))
                sys.exit(1)
            else:
                pos = match.end(0)
        self.tokens = tokens
        self.current_token = self.tokens[self.pos]
        return tokens

    # Method that checks if it is the end of the expression, if yes return True, else return False.
    def expr_end(self):
        if self.pos == len(self.tokens)-1:
            return True
        else:
            return False

    # Method that goes to the position of the next token.
    def token_next(self):
        self.pos += 1
        self.current_token = self.tokens[self.pos]
        return self.current_token
