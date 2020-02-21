__author__ = "Nikola"

from ComplexQuery.PolishNotation import isOperator
from Set.set import arrayToSet


class ComplexParser(object):
    """
        Parser used to parse a given complex query string, and turn it into a set-contained Polish notation array.
        Resulting polish-notation array is then used to calculate the resulting set, using the class
        PolishNotation.
        Correct format example is:
            python && java || ( clojure && !sql )
                ~ Spaces between tokens are necessary.
    """

    def __init__(self, query, loader):
        self.query = query
        self.output = []
        self.stack = []
        self.loader = loader

    def parseQuery(self):
        """
            Parses the complex query. Word tokens are pushed to the self.output (later used by PolishNotation object)
            Operator tokens need to behave according to the algorithm rules, which are defined in the pushOperator()
            function. After the function, self.output contains an array-like expression in Reverse-Polish form.
        """
        tokens = self.query.split(" ")
        for token in tokens:
            if not isOperator(token):
                _list = self.loader.trie.findContainingPages(token)
                _set = arrayToSet(self.loader, _list)
                self.output.append(_set)
            else:
                self.pushOperator(token)

        for index in reversed(range(self.stack.__len__())):
            self.output.append(self.stack[index])

    def pushOperator(self, operator):
        """
            Used to push ! && and || onto the operator-stack (self.stack[]). Rules being followed are taken from
            the Shunting-Yard algorithm.
        """
        if self.stack.__len__() == 0:
            self.stack.append(operator)
        elif operator == '(':
            self.stack.append(operator)
        elif operator == ')':
            while self.stack[-1] != '(':
                self.output.append(self.stack.pop())
            self.stack.pop()
        else:
            while operatorPrecedence(self.stack[-1]) > operatorPrecedence(operator):
                self.output.append(self.stack.pop())
                if self.stack.__len__() == 0:
                    break
            self.stack.append(operator)


def operatorPrecedence(operator):
    """
        In order to use the operator stack properly, we need to give different operators advantage/precedence over
        each other. In the way that '*' has precedence over '+', thus it has a greater integer value.
    """
    if operator == '!':
        return 3
    if operator == '&&':
        return 2
    if operator == '||':
        return 1

    return 0
