__author__ = "Nikola"


def checkQuery(query):
    """
        Brute force method for checking whether the BasicQuery is logically correct.
    """
    tokens = query.split()
    if tokens.__len__() == 2:
        if isOperator(tokens[1]):                  # Error if 'python not'
            raise SyntaxError
    if tokens.__len__() == 3:
        if isOperator(tokens[0]) or isOperator(tokens[2]):      # Error if 'python java not'
            raise SyntaxError
    if tokens.__len__() > 3:
        for token in tokens:
            if isOperator(token):
                raise SyntaxError


def isOperator(token):
    if token in ['and', 'or', 'not']:
        return True
