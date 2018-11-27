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


if __name__ == '__main__':
    unittest.main()
