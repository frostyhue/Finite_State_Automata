from Parser import *
import unittest

class TestLexer(unittest.TestCase):

    def test_parser_if_assigns_alphabet(self):

        alphabet_test_value = 'alphabet: ab'
        alphabet_test_lexer = Lexer(alphabet_test_value)
        alphabet_test_parser = Parser(alphabet_test_lexer)
        alphabet_test_parser.process_statement()
        alphabet_test_output = alphabet_test_parser.alphabet

        alphabet_test_expected = [Token('a', LETTER_SMALL), Token('b', LETTER_SMALL)]

        self.assertEqual(alphabet_test_expected, alphabet_test_output)

    def test_parser_if_assigns_states(self):
        states_test_value = 'states: Z, A, B'
        states_test_lexer = Lexer(states_test_value)
        states_test_parser = Parser(states_test_lexer)
        states_test_parser.process_statement()
        states_test_output = states_test_parser.states

        states_test_expected = [Token('Z', LETTER_CAPITAL), Token('A', LETTER_CAPITAL), Token('B', LETTER_CAPITAL),]

        self.assertEqual(states_test_expected, states_test_output)

    def test_parser_if_assigns_final(self):
        states_test_value = 'final: B'
        final_test_lexer = Lexer(states_test_value)
        final_test_parser = Parser(final_test_lexer)
        final_test_parser.process_statement()
        final_test_output = final_test_parser.final

        final_test_expected = [Token('B', LETTER_CAPITAL),]

        self.assertEqual(final_test_expected, final_test_output)

    def test_parser_if_assigns_transitions(self):
        transitions_test_value = 'transitions: \
                                        Z,a --> A \
                                        Z,b --> Z \
                                        A,b --> Z \
                                        A,a --> B \
                                        B,b --> B \
                                        B,a --> B \
                                        end.'
        transitions_test_lexer = Lexer(transitions_test_value)
        transitions_test_parser = Parser(transitions_test_lexer)
        transitions_test_parser.process_statement()
        transitions_test_output = transitions_test_parser.transitions

        transitions_test_expected = [Transition(origin='Z', edge='a', destination='A'), \
                                     Transition(origin='Z', edge='b', destination='Z'), \
                                     Transition(origin='A', edge='b', destination='Z'), \
                                     Transition(origin='A', edge='a', destination='B'), \
                                     Transition(origin='B', edge='b', destination='B'), \
                                     Transition(origin='B', edge='a', destination='B'),]

        self.assertEqual(transitions_test_expected, transitions_test_output)

    def test_parser_if_input_is_dfa(self):
        dfa_test_value = 'transitions: \
                                                Z,a --> A \
                                                Z,b --> Z \
                                                A,b --> Z \
                                                A,a --> B \
                                                B,b --> B \
                                                B,a --> B \
                                                end.'
        dfa_test_lexer = Lexer(dfa_test_value)
        dfa_test_parser = Parser(dfa_test_lexer)
        dfa_test_parser.process_statement()
        dfa_test_result = dfa_test_parser.process_if_dfa()

        self.assertEqual(True, dfa_test_result)



if __name__ == '__main__':
    unittest.main()
