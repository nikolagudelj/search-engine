__author__ = "Nikola"


class PolishNotation(object):
    """
        Class which is in charge of holding the Polish notation - form query, returned by the Complex query parser.
        It's duty is to use the given notation (in array form) and return the proper Set as a result.
    """

    def __init__(self, polish_expression, loader):
        self.expression = polish_expression
        self.loader = loader

    def calculateResultSet(self):
        index = 0
        while index < self.expression.__len__():
            if not isOperator(self.expression[index]):      # Word token is skipped
                index += 1
            elif isComplement(self.expression[index]):      # ! token is unary, so we work with [index-1] set
                set1 = self.expression[index-1]
                set1 = set1.complementUniversal(self.loader)
                self.expression[index-1] = set1
                self.expression.pop(index)
                index -= 1
            else:                                           # && and || are binary, we work with -1 and -2 sets
                set1 = self.expression[index-1]
                set2 = self.expression[index-2]
                operator = self.expression[index]

                self.expression[index - 2] = calculate(set1, set2, operator)
                self.expression.pop(index)
                self.expression.pop(index-1)
                index -= 2

        return self.expression[0]                    # Reverse-polish is finished when the expression converges to 1 set


def calculate(set1, set2, operator):
    if operator == '&&':
        return set1.__and__(set2)
    if operator == '||':
        return set1.__or__(set2)


def isOperator(exp):
    if exp == '&&': return True
    if exp == '||': return True
    if exp == '!' : return True
    if exp == '(' : return True
    if exp == ')' : return True

    return False


def isComplement(exp):
    if exp == '!':
        return True
    return False
