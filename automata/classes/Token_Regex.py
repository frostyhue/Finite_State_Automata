###############################################################################
#                                                                             #
#  TOKEN REGULAR EXPRESSIONS                                                  #
#                                                                             #
###############################################################################

# Token types
LETTER_CAPITAL = 'LETTER_CAPITAL'
LETTER_SMALL = 'LETTER_SMALL'
COLON = 'COLON'
HASHTAG = 'HASHTAG'
COMMA = 'COMMA'
DASH = 'DASH'
ANGLE_BRACKET = 'ANGLE_BRACKET'
UNDERSCORE = 'UNDERSCORE'
STAR = 'STAR'
DOT = 'DOT'
PIPE = 'PIPE'
NUMBER = 'NUMBER'
RESERVED = 'RESERVED'
LPAR = 'LPAR'
RPAR = 'RPAR'

# List with regular expressions to recognise token types.
token_expressions = [
    (r'[ \n\t]+',                   None),
    (r'alphabet:',                  RESERVED),
    (r'states:',                    RESERVED),
    (r'final:',                     RESERVED),
    (r'transitions:',               RESERVED),
    (r'end.',                       RESERVED),
    (r'[A-Z]',                      LETTER_CAPITAL),
    (r'[a-z]',                      LETTER_SMALL),
    (r'[0-9]',                      NUMBER),
    (r'[:]',                        COLON),
    (r'[#]',                        HASHTAG),
    (r'[,]',                        COMMA),
    (r'[-]',                        DASH),
    (r'[>]',                        ANGLE_BRACKET),
    (r'[_]',                        UNDERSCORE),
    (r'[*]',                        STAR),
    (r'[.]',                        DOT),
    (r'[|]',                        PIPE),
    (r'[(]',                        LPAR),
    (r'[)]',                        RPAR),
]
