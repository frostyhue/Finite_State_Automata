from Edge import *
from Interpreter import *
import re


class StateMachine(object):

    def __init__(self, parser):
        self.parser = parser
        self.interpreter = None
        self.regex = None
        self.states = None
        self.transitions = None
        self.alphabet = None
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

    def from_file(self):
        list = []
        list_formatted = []
        _text = ''
        with open('file.txt') as f:
            f_contents = f.readlines()
            for line in f_contents:
                if not line.isspace():
                    list.append(line.strip())
            for line in list:
                if re.search(r'end.', str(line)) or re.search(r'transitions:', str(line)) or re.search(r'-->',
                                                                                                       str(line)):
                    _text += str(line)
                    if re.search(r'end.', str(line)):
                        list_formatted.append(_text)
                        break
                else:
                    list_formatted.append(str(line))
        return list_formatted

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
        # dest_stat = ''
        # for transition in self.transitions:
        #     for state in self.states:
        #         if state.state_name == transition.origin:
        #             for destination in self.states:
        #                 if destination.state_name == transition.destination:
        #                     dest_stat = destination
        #             print('Destination')
        #             print(dest_stat)
        #             state.add_edge(Edge(label=transition.edge, destination=dest_stat))
        for transition in self.transitions:
            for state in self.states:
                if state.state_name == transition.origin:
                    for dest_state in self.states:
                        if dest_state.state_name == transition.destination:
                            state.add_edge(Edge(label=transition.edge, destination=dest_state))

    def check_if_finite(self):
        return True

    def regex_to_nfa(self, regex):
        NFA = StateMachine(self.parser)
        result = NFA.parser.regex_nfa(regex)
        NFA.states, NFA.transitions = result
        NFA.process_transitions()
        print(NFA.states)

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
