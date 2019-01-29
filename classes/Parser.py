from classes.Lexer import *
from classes.Transition import *
from classes.State import *
from classes.Operations import *

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
        self.states = []
        self.transitions = []

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
        self.initial_state = self.parse_nfa()[0]
        return self.states, self.transitions

    def parse_nfa(self):

        token = self.current_token
        # the base condition where the next token is a letter or underscore
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
        # if the current operation is from a to b aka Dot
        elif token.type == DOT:
            self.pop_token(DOT)
            self.pop_token(LPAR)
            # if first param is a letter
            if self.current_token.type in (LETTER_SMALL, STAR):
                not_star = False
                if not self.current_token.type == STAR:
                    not_star = True
                _origin, _edge_o = self.parse_nfa()
                if not_star:
                    self.states.append(_origin)
                # if second param is a letter
                if self.current_token.type in (LETTER_SMALL, STAR):
                    _dest, _edge_d = self.parse_nfa()
                    if not self.current_token.type == STAR:
                        self.states.append(_dest)
                    _end_state = State('S' + str(self._state_number))
                    self._state_number += 1
                    self.states.append(_end_state)
                    self.transitions.append(Transition(_origin.state_name, _edge_o, _dest.state_name))
                    self.transitions.append(Transition(_dest.state_name, _edge_d, _end_state.state_name))
                    return _origin, _end_state
                # if second param is an operation
                else:
                    # self.pop_token(COMMA)
                    _dest, _end_state = self.parse_nfa()
                    self.transitions.append(Transition(_origin.state_name, _edge_o, _dest.state_name))
                    return _origin, _end_state
            # if first param is an operation
            else:
                _origin, _state_mid= self.parse_nfa()
                self.pop_token(COMMA)
                # if second param is a letter
                if self.current_token.type in (LETTER_SMALL, STAR):
                    not_star = False
                    if not self.current_token.type == STAR:
                        not_star = True
                    _dest, _edge_d = self.parse_nfa()
                    if not_star:
                        self.states.append(_dest)
                    self.transitions.append(Transition(_state_mid.state_name, _edge_d, _dest.state_name))
                    return _origin, _dest
                # if second param i sn operation
                else:
                    _dest, _end_state = self.parse_nfa()
                    self.transitions.append(Transition(_state_mid.state_name, '_', _dest.state_name))
                    return _origin, _end_state
        # If the current operation is repeat aka STAR
        elif token.type == STAR:
            self.pop_token(STAR)
            self.pop_token(LPAR)
            """If the next token is a letter, meaning it will be looping only a letter"""
            _origin, _edge_o = self.parse_nfa()
            self.states.append(_origin)
            self.transitions.append(Transition(_origin.state_name, _edge_o, _origin.state_name))
            if self.current_token.type == COMMA:
                self.pop_token(COMMA)
            return _origin, '_'
        # it the operation is an or aka PIPE
        elif token.type == PIPE:
            self.pop_token(PIPE)
            self.pop_token(LPAR)
            # if the next token is a letter
            if self.current_token.type in (LETTER_SMALL, STAR):
                not_star = False
                if not self.current_token.type == STAR:
                    not_star = True
                _origin, _edge_o = self.parse_nfa()
                if not_star:
                    self.states.append(_origin)
                _end_o = State('S' + str(self._state_number))
                self._state_number += 1
                self.states.append(_end_o)
                self.transitions.append(Transition(_origin.state_name, _edge_o, _end_o.state_name))
                # if the next token is a letter
                if self.current_token.type in (LETTER_SMALL, STAR):
                    _dest, _edge_d = self.parse_nfa()
                    self.transitions.append(Transition(_origin.state_name, _edge_d, _end_o.state_name))
                    return _origin, _end_o
                # if second param is an operation
                else:
                    _dest, _end_d = self.parse_nfa()
                    _start = State('S' + str(self._state_number))
                    self._state_number += 1
                    self.states.append(_start)
                    _end_state = State('S' + str(self._state_number))
                    self._state_number += 1
                    self.states.append(_end_state)
                    self.transitions.append(Transition(_start.state_name, '_', _origin.state_name))
                    self.transitions.append(Transition(_start.state_name, '_', _dest.state_name))
                    self.transitions.append(Transition(_end_o.state_name, '_', _end_state.state_name))
                    self.transitions.append(Transition(_end_d.state_name, '_', _end_state.state_name))
                    return _start, _end_state
            else:
                _left_o, _left_d = self.parse_nfa()
                self.pop_token(COMMA)
                # if the next token is a letter
                if self.current_token.type in (LETTER_SMALL, STAR):
                    not_star = False
                    if not self.current_token.type == STAR:
                        not_star = True
                    _right_o, _right_l = self.parse_nfa()
                    if not_star:
                        self.states.append(_right_o)
                    _right_d = State('S' + str(self._state_number))
                    self._state_number += 1
                    self.states.append(_right_d)
                    self.transitions.append(Transition(_right_o.state_name, _right_l, _right_d.state_name))
                    _start = State('S' + str(self._state_number))
                    self._state_number += 1
                    self.states.append(_start)
                    _end_state = State('S' + str(self._state_number))
                    self._state_number += 1
                    self.states.append(_end_state)
                    self.transitions.append(Transition(_start.state_name, '_', _left_o.state_name))
                    self.transitions.append(Transition(_start.state_name, '_', _right_o.state_name))
                    self.transitions.append(Transition(_left_d.state_name, '_', _end_state.state_name))
                    self.transitions.append(Transition(_right_d.state_name, '_',_end_state.state_name))
                    return _start, _end_state
                # if second param is an operation
                else:
                    _right_o, _right_d = self.parse_nfa()
                    _start = State('S' + str(self._state_number))
                    self._state_number += 1
                    self.states.append(_start)
                    _end_state = State('S' + str(self._state_number))
                    self._state_number += 1
                    self.states.append(_end_state)
                    self.transitions.append(Transition(_start.state_name, '_', _left_o.state_name))
                    self.transitions.append(Transition(_start.state_name, '_', _right_o.state_name))
                    self.transitions.append(Transition(_left_d.state_name, '_', _end_state.state_name))
                    self.transitions.append(Transition(_right_d.state_name, '_', _end_state.state_name))
                    return _start, _end_state

        return self.states, self.transitions

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
