from Lexer import *
from Transition import *

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
        self.alphabet = []
        self.states = []
        self.final = []
        self.transitions = []

    # Method that raises and error.
    def error(self, type_got):
        print('Token type {type} expected, received {type_got}!'.format(type=self.current_token.type, type_got=type_got))

    # Method that goes to the next token if the current one has already been processed.
    def pop_token(self, token_type):
        if self.current_token.type == token_type:
            if not self.lexer.expr_end():
                self.current_token = self.lexer.token_next()
        else:
            self.error(token_type)

    def process_statement(self):
        token = self.current_token
        if token.type == RESERVED:
            if token.value == 'alphabet:':
                self.pop_token(RESERVED)
                while self.current_token.type == LETTER_SMALL:
                    self.alphabet.append(self.current_token)
                    if self.lexer.expr_end():
                        break
                    self.pop_token(LETTER_SMALL)
            elif token.value == 'states:':
                self.pop_token(RESERVED)
                while self.current_token.type == LETTER_CAPITAL:
                    self.states.append(self.current_token)
                    if self.lexer.expr_end():
                        break
                    self.pop_token(LETTER_CAPITAL)
                    if self.current_token.type == COMMA:
                        self.pop_token(COMMA)
            elif token.value == 'final:':
                self.pop_token(RESERVED)
                while self.current_token.type == LETTER_CAPITAL:
                    self.final.append(self.current_token)
                    if self.lexer.expr_end():
                        break
                    self.pop_token(LETTER_CAPITAL)
                    if self.current_token.type == COMMA:
                        self.pop_token(COMMA)
            elif token.value == 'transitions:':
                self.pop_token(RESERVED)
                while not self.current_token.value == 'end.':
                    origin = self.current_token.value
                    self.pop_token(LETTER_CAPITAL)
                    self.pop_token(COMMA)
                    edge = self.current_token.value
                    self.pop_token(LETTER_SMALL)
                    self.pop_token(DASH)
                    self.pop_token(DASH)
                    self.pop_token(ANGLE_BRACKET)
                    destination = self.current_token.value
                    self.pop_token(LETTER_CAPITAL)
                    self.transitions.append(Transition(origin=origin, edge=edge, destination=destination))
                    if self.lexer.expr_end():
                        break
                self.pop_token(RESERVED)
        else:
            print('Unexpected type!')