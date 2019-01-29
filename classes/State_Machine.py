from classes.Edge import *
from classes.Interpreter import *
import re
"""
TO-DO
1.Method getting the alphabet after regex parsing. DONE
2.Method making states without any edges to final.
3.
"""

class StateMachine(object):

    def __init__(self, parser):
        self.parser = parser
        self.interpreter = None
        self.regex = None
        self.states = None
        self.transitions = None
        self.alphabet = []
        self.initial_state = None

    def process_if_dfa(self):
        is_dfa = True
        for transition in self.transitions:
            for transition_to_compare_with in self.transitions:
                if not transition_to_compare_with.checked:
                    if transition.origin == transition_to_compare_with.origin \
                        and transition.edge == transition_to_compare_with.edge \
                            and not transition.destination == transition_to_compare_with.destination:
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

    def parse_regex(self, _expr):
        self.parser.regex_nfa(_expr)
        self.update_lists()

    def from_regex(self, _expression):
        self.interpreter = Interpreter(self.parser)
        self.parser.new_expression(_expression=_expression)
        self.regex = self.interpreter.interpret()
        return self.regex

    def update_lists(self):
        self.states = self.parser.states
        self.transitions = self.parser.transitions
        self.alphabet = self.parser.alphabet
        self.initial_state = self.parser.initial_state

    def process_transitions(self):
        for transition in self.transitions:
            for state in self.states:
                for dest_state in self.states:
                    if state.state_name == transition.origin and dest_state.state_name == transition.destination:
                        state.add_edge(Edge(label=transition.edge, destination=dest_state))

    def process_alphabet_regex(self):
        for transition in self.transitions:
            if not transition.edge == '_' and transition.edge not in self.alphabet:
                self.alphabet.append(transition.edge)


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
