import os
import re
from Lexer import *
from Parser import *
from State_Machine import *

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
    print('Final: ')
    print(state_machine.final)
    state_machine.make_final_state()
    print('States: ')
    for state in state_machine.states:
        print(state)
    state_machine.process_transitions()
    print('States with edges: ')
    for state in state_machine.states:
        print(state.state_name + 's')
        for edge in state.state_edges:
            print(edge)



if __name__ == '__main__':
    main()


