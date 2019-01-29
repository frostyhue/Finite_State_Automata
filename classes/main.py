import os
import re
from classes.Lexer import *
from classes.Parser import *
from classes.State_Machine import *


def main():
    lexer = Lexer()
    parser = Parser(lexer)
    state_machine = StateMachine(parser)
    # print(state_machine.from_regex('|(.(a,*(b)),*(c))'))
    list = state_machine.from_file()
    state_machine.parser.parse_file(list)
    state_machine.update_lists()
    for item in state_machine.transitions:
        print('Transition origin: {}, edge: {}, destination: {}'.format(item.origin, item.edge, item.destination))
    print('Initial state:')
    print(state_machine.initial_state.state_name)
    print('Alphabet: ')
    for letter in state_machine.alphabet:
        print(letter)
    for state in state_machine.states:
        print(state)
    state_machine.process_transitions()
    for state in state_machine.states:
        print(state.state_name)
        for edge in state.state_edges:
            print(edge.edge_label)
            print(edge.edge_destination)
    print(state_machine.process_if_dfa())
    state_machine.regex_to_nfa('*(a)')


if __name__ == '__main__':
    main()


