from Lexer import *
import unittest

class TestLexer(unittest.TestCase):


    def setUp(self):
        # Test if lexer recognizes capital and normal letters.
        self.letter_input = 'LeTtErS'
        self.letter_output = [Token('L', LETTER_CAPITAL), Token('e', LETTER_SMALL), Token('T', LETTER_CAPITAL),\
                              Token('t', LETTER_SMALL), Token('E', LETTER_CAPITAL), Token('r', LETTER_SMALL),\
                              Token('S', LETTER_CAPITAL)]

        # Test if lexer recognizes number spaces.
        self.number_input = '152'
        self.number_output = [Token('1', NUMBER), Token('5', NUMBER), Token('2', NUMBER)]

        # Test if lexer recognizes colon symbol.
        self.colon_input = ': :      :'
        self.colon_output = [Token(':', COLON), Token(':', COLON), Token(':', COLON)]

        # Test if lexer recognizes hashtag symbol.
        self.hashtag_input = '   # ### #                                                                                #'
        self.hashtag_output = [Token('#', HASHTAG), Token('#', HASHTAG), \
                               Token('#', HASHTAG), Token('#', HASHTAG), \
                               Token('#', HASHTAG), Token('#', HASHTAG)]

        # Test if lexer recognizes comma symbol.
        self.comma_input = ', ,,        ,          ,'
        self.comma_output = [Token(',', COMMA), Token(',', COMMA), Token(',', COMMA), Token(',', COMMA), Token(',', COMMA)]

        # Test if lexer recognizes dash symbol.
        self.dash_input = '- ---  '
        self.dash_output = [Token('-', DASH), Token('-', DASH), Token('-', DASH), Token('-', DASH)]

        # Test if lexer recognizes angle bracket symbol.
        self.angle_bracket_input = '>> >    '
        self.angle_bracket_output = [Token('>', ANGLE_BRACKET), Token('>', ANGLE_BRACKET), Token('>', ANGLE_BRACKET)]

        # Test if lexer recognizes underscore symbols.
        self.underscore_input = '_ __    _'
        self.underscore_output = [Token('_', UNDERSCORE), Token('_', UNDERSCORE), Token('_', UNDERSCORE), Token('_', UNDERSCORE)]

        # Test if lexer recognizes star symbol.
        self.star_input = '* * ***'
        self.star_output = [Token('*', STAR), Token('*', STAR), Token('*', STAR), Token('*', STAR), Token('*', STAR)]

        # Test if lexer recognizes dot symbol.
        self.dot_input = '. .. . . '
        self.dot_output = [Token('.', DOT), Token('.', DOT), Token('.', DOT), Token('.', DOT), Token('.', DOT)]

        # Test if lexer recognizes pipe symbol.
        self.pipe_input = '| | |||'
        self.pipe_output = [Token('|', PIPE), Token('|', PIPE), Token('|', PIPE), Token('|', PIPE), Token('|', PIPE)]

        # Test if the lexer recognizes a series of symbols and empty spaces.
        self.complex_string_input = '* | -- 23 as DD , ..'
        self.complex_string_output = [Token('*', STAR), Token('|', PIPE), Token('-', DASH), \
                                      Token('-', DASH), Token('2', NUMBER), Token('3', NUMBER), \
                                      Token('a', LETTER_SMALL), Token('s', LETTER_SMALL), \
                                      Token('D', LETTER_CAPITAL), Token('D', LETTER_CAPITAL), \
                                      Token(',', COMMA), Token('.', DOT), Token('.', DOT)]

        self.complex_string2_input = '>_>, #*BoY-|'
        self.complex_string2_output = [ Token('>', ANGLE_BRACKET), Token('_', UNDERSCORE), \
                                        Token('>', ANGLE_BRACKET), Token(',', COMMA),\
                                        Token('#', HASHTAG), Token('*', STAR), \
                                        Token('B', LETTER_CAPITAL),
                                        Token('o', LETTER_SMALL), Token('Y', LETTER_CAPITAL), \
                                        Token('-', DASH), Token('|', PIPE)]

    def test_lexer_letters(self):

        lexer_letters_test = Lexer(self.letter_input)
        result_letters_test = lexer_letters_test.lex()
        self.assertListEqual(result_letters_test, self.letter_output)
        self.assertEqual(result_letters_test, self.letter_output)

    def test_lexer_numbers(self):

        lexer_numbers_test = Lexer(self.number_input)
        result_numbers_test = lexer_numbers_test.lex()
        self.assertListEqual(result_numbers_test, self.number_output)

    def test_lexer_colon(self):

        lexer_colon_test = Lexer(self.colon_input)
        result_colon_test = lexer_colon_test.lex()
        self.assertListEqual(result_colon_test, self.colon_output)

    def test_lexer_hashtag(self):

        lexer_hashtag_test = Lexer(self.hashtag_input)
        result_hashtag_test = lexer_hashtag_test.lex()
        self.assertListEqual(result_hashtag_test, self.hashtag_output)

    def test_lexer_comma(self):

        lexer_comma_test = Lexer(self.comma_input)
        result_comma_test = lexer_comma_test.lex()
        self.assertListEqual(result_comma_test, self.comma_output)

    def test_lexer_dash(self):
        lexer_dash_test = Lexer(self.dash_input)
        result_dash_test = lexer_dash_test.lex()
        self.assertListEqual(result_dash_test, self.dash_output)

    def test_lexer_angle_bracket(self):
        lexer_angle_bracket_test = Lexer(self.angle_bracket_input)
        result_angle_bracket_test = lexer_angle_bracket_test.lex()
        self.assertListEqual(result_angle_bracket_test, self.angle_bracket_output)

    def test_lexer_underscore(self):
        lexer_underscore_test = Lexer(self.underscore_input)
        result_underscore_test = lexer_underscore_test.lex()
        self.assertListEqual(result_underscore_test, self.underscore_output)

    def test_lexer_star(self):
        lexer_star_test = Lexer(self.star_input)
        result_star_test = lexer_star_test.lex()
        self.assertListEqual(result_star_test, self.star_output)

    def test_lexer_dot(self):
        lexer_dot_test = Lexer(self.dot_input)
        result_dot_test = lexer_dot_test.lex()
        self.assertListEqual(result_dot_test, self.dot_output)

    def test_lexer_pipe(self):
        lexer_pipe_test = Lexer(self.pipe_input)
        result_pipe_test = lexer_pipe_test.lex()
        self.assertListEqual(result_pipe_test, self.pipe_output)

    def test_lexer_complex_string(self):
        lexer_complex_string = Lexer(self.complex_string_input)
        result_complex_string = lexer_complex_string.lex()
        self.assertListEqual(result_complex_string, self.complex_string_output)

    def test_lexer_complex_string2(self):
        lexer_complex_string2 = Lexer(self.complex_string2_input)
        result_complex_string2 = lexer_complex_string2.lex()
        self.assertListEqual(result_complex_string2, self.complex_string2_output)

if __name__ == '__main__':
    unittest.main()
