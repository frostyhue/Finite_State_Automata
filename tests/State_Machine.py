from State import *
from Transition import *
from Interpreter import *
import re


class SateMachine(object):

    def __init__(self, parser):
        self.interpreter = Interpreter(parser)
        self.regex = self.interpreter.interpret()
        self.states = self.interpreter.parser.states
        self.transitions = self.interpreter.parser.transitions
        self.final = self.interpreter.parser.final
        self.alphabet = self.interpreter.parser.alphabet
        self.initial_state = self.interpreter.parser.initial_state

    def process_if_dfa(self):
        is_dfa = True
        for transition in self.transitions:
            for transition_to_compare_wtih in self.transitions:
                if not transition_to_compare_wtih.checked == True:
                    if transition.origin == transition_to_compare_wtih.origin \
                        and transition.edge == transition_to_compare_wtih.edge \
                            and not transition.destination == transition_to_compare_wtih.destination:
                        is_dfa = False
                        break
                    if not is_dfa:
                        break
                if not is_dfa:
                    break

            if not is_dfa:
                break
            transition.checked = True
        return is_dfa

    def check_states(self, label):
        states = []
        for state in self.states:
            if state.state_name == label:
                states.append(state)
        return states

    def process_transitions(self):
        for transition in self.transitions:
            for state in self.states:
                if transition.origin == state.state_name:
                    state.add_edge(Edge(destination=transition.destination, label=transition.edge))
