from Lexer import *
from Transition import *
from State import *
from Edge import *
from Operations import *

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
        self.states = []
        self.transitions = []
        self.final = []
        self.alphabet = []
        self.initial_state = ''

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
                    self.states.append(State(name=self.current_token.value))
                    if self.lexer.expr_end():
                        break
                    self.pop_token(LETTER_CAPITAL)
                    if self.current_token.type == COMMA:
                        self.pop_token(COMMA)
            elif token.value == 'final:':
                self.pop_token(RESERVED)
                while self.current_token.type == LETTER_CAPITAL:
                    self.final.append(State(self.current_token.value))
                    if self.lexer.expr_end():
                        break
                    self.pop_token(LETTER_CAPITAL)
                    if self.current_token.type == COMMA:
                        self.pop_token(COMMA)
            elif token.value == 'transitions:':
                self.pop_token(RESERVED)
                while not self.current_token.value == 'end.':
                    origin = self.current_token.value
                    if type(self.initial_state) == str:
                        for state in self.states:
                            if state.state_name == origin:
                                self.initial_state = state
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

    def process_regex(self):
        token = self.current_token
        node = ""

        if token.type == LETTER_SMALL:
            # probably for assigning an alphabet letter!
            # self.pred_list.append(token.value)
            node = Letter(self.current_token)
            self.pop_token(LETTER_SMALLq)

            if self.current_token.type == COMMA:
                self.pop_token(COMMA)

            if self.current_token.type == RPAR:
                self.pop_token(RPAR)

            return node

        # Logic if the current token is a start for repeating the letter.
        elif token.type == STAR:
            op = Token(type=STAR, value='*')
            self.pop_token(STAR)
            if self.current_token.type == LPAR:
                self.pop_token(LPAR)
            node = Repeat(op=op, letter=self.process_regex())
            return node

        elif token.type == UNDERSCORE:
            # Logic if the current token is a start for repeating the letter.
            op = Token(type=UNDERSCORE, value='e')
            self.pop_token(UNDERSCORE)
            if self.current_token.type == LPAR:
                self.pop_token(LPAR)
            node = ET(symbol=self.process_regex())
            return node

        # Logic if the current token is one of the Contingency operators.
        elif token.type in (DOT, PIPE):
            if token.type == DOT:
                op = Token(type=DOT, value='.')
            elif token.type == BICOND:
                op = Token(type=PIPE, value='|')
            self.pop_token(token.type)
            self.pop_token(LPAR)
            node = TransitionOp(left=self.op_statement(), op=op, right=self.op_statement())
            return node

        # Logic if the current token is a right parentheses.
        elif token.type == RPAR:
            self.pop_token(RPAR)
            node = self.op_statement()
            return node

        # Logic if the current token is a comma.
        elif token.type == COMMA:
            self.pop_token(COMMA)
            node = self.op_statement()
            return node

        return node

    def new_lexer(self, _expression):
        self.lexer = Lexer(_expression)
        self.tokens_list = self.lexer.lex()
        self.current_token = self.tokens_list[0]


    def parse(self):
        node = self.process_regex()
        return node

    # def validate_word(self, word):
    #     valid = False
    #     current_state = self.initial_state
    #     edges_with_same_label_count = 0
    #     for letter in word:
    #         possible_states = []
    #         print(letter)
    #         for edge in current_state.state_edges:
    #             if edge.edge_label == letter:
    #                 edges_with_same_label_count +=1
    #                 possible_states = self.check_states(edge.edge_destination.state_name)
    #         if edges_with_same_label_count == 1:
    #             current_state = possible_states[0]
    #             edges_with_same_label_count == 0
    #             valied = True
    #         elif edges_with_same_label_count == 0:
    #             valied = False
    #         if current_state.state_name == self.final[0].state_name:
    #             break
    #     return valid





