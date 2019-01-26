from Lexer import *
from Transition import *
from State import *
from Operations import *

###############################################################################
#                                                                             #
#  PARSER                                                                     #
#                                                                             #
###############################################################################


class Parser(object):

    def __init__(self, lexer):
        self.current_token = ''
        self.tokens_list = []
        self.lexer = lexer
        self.states = []
        self.transitions = []
        self.alphabet = []
        self.initial_state = ''
        self._state_number = 0

    # Method that raises and error.
    def error(self, type_got):
        raise Exception('Token type {type} expected, received {type_got}!'.format(type=self.current_token.type, type_got=type_got))

    # Method that goes to the next token if the current one has already been processed.
    def pop_token(self, token_type):
        if self.current_token.type == token_type:
            if not self.lexer.expr_end():
                self.current_token = self.lexer.token_next()
        else:
            self.error(token_type)

    def find_state_change_final(self, state_name):
        for state in self.states:
            if state.state_name == state_name:
                state.final = True

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
                    self.find_state_change_final(self.current_token.value)
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
                    if self.current_token.type == LETTER_SMALL:
                        self.pop_token(LETTER_SMALL)
                    else:
                        self.pop_token(UNDERSCORE)
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
            self.pop_token(LETTER_SMALL)

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
            op = Token(type=UNDERSCORE, value=u'\u03B5')
            self.pop_token(UNDERSCORE)
            if self.current_token.type == LPAR:
                self.pop_token(LPAR)
            node = ET(symbol=op)
            return node

        # Logic if the current token is one of the Contingency operators.
        elif token.type in (DOT, PIPE):
            if token.type == DOT:
                op = Token(type=DOT, value='.')
            elif token.type == PIPE:
                op = Token(type=PIPE, value='|')
            self.pop_token(token.type)
            self.pop_token(LPAR)
            node = TransitionOp(left=self.process_regex(), op=op, right=self.process_regex())
            return node

        # Logic if the current token is a right parentheses.
        elif token.type == RPAR:
            self.pop_token(RPAR)
            node = self.process_regex()
            return node

        # Logic if the current token is a comma.
        elif token.type == COMMA:
            self.pop_token(COMMA)
            node = self.process_regex()
            return node

        return node

    def regex_nfa(self, _expression):
        self.new_expression(_expression)
        self.parse_nfa()
        return self._states, self._transitions

    def parse_nfa(self):
        self._states = []
        self._transitions = []

        token = self.current_token
        if token.type in (LETTER_SMALL, UNDERSCORE):
            state = State('S' + str(self._state_number))
            self._state_number += 1
            letter = self.current_token.value
            self.pop_token(LETTER_SMALL)
            if self.current_token.type == COMMA:
                self.pop_token(COMMA)
            if self.current_token.type == RPAR:
                self.pop_token(RPAR)
            return state, letter
        elif token.type == DOT:
            self.pop_token(DOT)
            self.pop_token(LPAR)
            _origin_and_edge = self.parse_nfa()
            self._states.append(_origin_and_edge[0])
            _dest_and_edge = self.parse_nfa()
            self._states.append(_dest_and_edge[0])
            _end_state = State('S' + str(self._state_number))
            self._states.append(_end_state)
            self._transitions.append(Transition(_origin_and_edge[0].state_name, _origin_and_edge[1], _dest_and_edge[0].state_name))
            self._transitions.append(Transition(_dest_and_edge[0].state_name, _dest_and_edge[1], _end_state.state_name))
            return _origin_and_edge[0], _end_state
        elif token.type == STAR:
            self.pop_token(STAR)
            self.pop_token(LPAR)
            _origin_and_end = self.parse_nfa()
            self._states.append(_origin_and_end[0])
            _e_state_1 = State('S' + str(self._state_number))
            self._states.append(_e_state_1)
            self._transitions.append(Transition(_e_state_1.state_name, '_', _origin_and_end[0].state_name))
            _e_state_2 = State('S' + str(self._state_number))
            self._states.append(_e_state_2)
            self._transitions.append(Transition(_origin_and_end[1].state_name, '_', _e_state_2.state_name))
            self._transitions.append(Transition(_origin_and_end[1].state_name, '_', _origin_and_end[0].state_name))
            self._transitions.append(Transition(_e_state_1.state_name, '_', _e_state_2.state_name))
            self.pop_token(RPAR)
            return _e_state_1, _e_state_2
        elif token.type == PIPE:
            self.pop_token(PIPE)
            self.pop_token(LPAR)
            _origin_edge_letter = self.parse_nfa()
            self._states.append(_origin_edge_letter[0])
            _dest_second_edge = self.parse_nfa()
            self._states.append(_dest_second_edge[0])
            self._transitions.append(Transition(_origin_edge_letter[0].state_name, _origin_edge_letter[1], _dest_second_edge[0].state_name))
            self._transitions.append(Transition(_origin_edge_letter[0].state_name, _dest_second_edge[1], _dest_second_edge[0].state_name))
            return _origin_edge_letter[0], _dest_second_edge[0]

        return self._states, self._transitions

    def new_expression(self, _expression):
        self.tokens_list = self.lexer.lex(_expression)
        self.current_token = self.tokens_list[0]

    def parse_file(self, list):
        for item in list:
            self.new_expression(str(item))
            self.process_statement()

    def parse_regex(self):
        node = self.process_regex()
        return node
