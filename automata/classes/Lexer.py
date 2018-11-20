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
    def __init__(self, expression):
        self.token_expressions = token_expressions
        self.expression = expression
        self.pos = 0
        self.tokens = []
        self.current_token = ''

    # The method that divides the expression into Tokens.
    def lex(self):
        pos = 0
        tokens = []
        while self.pos < len(self.expression):
            match = None
            for token_expression in self.token_expressions:
                pattern, type = token_expression[0], token_expression[1]
                regex = re.compile(pattern)
                match = regex.match(self.expression, pos)
                if match:
                    value = match.group(0)
                    if type:
                        tokens.append(Token(value, type))
                    break
                if not match:
                    sys.stderr.write('Illegal character: %s' % self.expression[pos])
                    sys.exit(1)
                else:
                    pos = match.end(0)
            self.tokens = tokens
            self.current_token = self.tokens[self.pos]
            return tokens

    # The method that checks if it is the end of the expression, if yes return True, else return False.
    def expr_end(self):
        if self.pos == len(self.tokens)-1:
            return True
        else:
            return False

    # The method that progresses to the next token.
    def token_next(self):
        self.pos += 1
        self.current_token = self.tokens[self.pos]
        return self.current_token