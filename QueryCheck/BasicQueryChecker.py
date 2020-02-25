__author__ = "Nikola"

import ply.lex as lex
import ply.yacc as yacc

# LEXICAL ANALYSIS

reserved = {
    '&&' : 'AND',       # At this moment redundant, left here for code clarity
    '||'  : 'OR',
    '!' : 'NOT'
}

tokens = ['WORD', 'AND', 'OR', 'NOT']

t_ignore = " "


def t_WORD(t):
    r'[a-z*()~@%^/\\]+'


def t_AND(t):
    r'\&\&'


def t_OR(t):
    r'\|\|'


def t_NOT(t):
    r'\!'


def t_error(t):
    print("Invalid character in query: '" + t.value[0] + "'")
    raise SyntaxError


lexer = lex.lex()


def p_input(t):
    """ INPUT : QUERY
    """


def p_query(t):
    """
        QUERY :  _WORDS
              | _WORD BINOP _WORD
              | NOT _WORD
              | _WORD NOT _WORD
    """


def p_words(t):
    """
        _WORDS : _WORD
               | _WORDS _WORD
    """


def p_word(t):
    """
        _WORD : WORD
    """


def p_binop(t):
    """
        BINOP : AND
              | OR
    """


def p_error(t):
    print("Incorrect query.")
    raise SyntaxError


# Building a parser from the above-written rules
basicChecker = yacc.yacc()
