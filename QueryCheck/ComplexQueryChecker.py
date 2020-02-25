__author__ = "Nikola"

import ply.lex as lex
import ply.yacc as yacc

# LEXICAL ANALYSIS

tokens = (
    'WORD',
    'AND', 'OR', 'NOT',
    'LPAREN', 'RPAREN',
)

# Token definitions
t_AND = r'\&\&'
t_OR = r'\|\|'
t_NOT = r'\!'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_WORD = r'[a-zA-Z0-9_@]+'      # Allowed characters for search word tokens


# Ignores spaces
t_ignore = " "


# Lexical error detection
def t_error(t):
    print("Illegal character in query: '" + t.value[0] + "'.")
    raise SyntaxError


# Build the lexer
lexer = lex.lex()


# GRAMMAR RULES

query_array = []        # Used to keep tokens from search
                        # !python || java -> [!, python, ||, java]


def p_query(t):
    """
        QUERY :  OPERAND
               | UNARY _LPAREN QUERY _RPAREN
               | QUERY BINOP QUERY
    """


def p_operand(t):
    """ OPERAND : UNARY WORD
    """
    query_array.append(t.slice[-1].value)


def p_lparen(t):
    """ _LPAREN : LPAREN
    """
    query_array.append(t.slice[-1].value)


def p_rparen(t):
    """ _RPAREN : RPAREN
    """
    query_array.append(t.slice[-1].value)


def p_expression_unop(t):
    """ UNARY :
               | NOT
    """
    query_array.append(t.slice[-1].value)


def p_expression_binop(t):
    '''  BINOP : AND
               | OR
    '''
    query_array.append(t.slice[-1].value)


def p_error(t):
    print("Incorrect query!")
    raise SyntaxError


# Building a parser from the above-written rules
complexChecker = yacc.yacc()
