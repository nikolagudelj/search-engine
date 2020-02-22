__author__ = "Nikola"


from Misc.Config import Config
from ComplexQuery.ComplexParser import ComplexParser
from ComplexQuery.PolishNotation import PolishNotation
from PageRank.rank import page_rank
from Set.set import arrayToSet
from TrieParser.HtmlLoader import HtmlLoader


class Operator(enumerate):
    """ Enumeration class for easier identification of query operators. """
    OR = 0
    AND = 1
    NOT = 2


class ConsoleUI(object):
    """
        Console script which is used as a UI.
        On initialization, it loads all the HTML files into a Trie structure and creates a Graph
        After the initialization, it allows the user to run different search methods from the terminal.
    """

    def __init__(self):
        self.operator = -1
        self.path = Config.inputPath()
        print("Loading HTML files...")
        self.htmlLoader = HtmlLoader()
        self.htmlLoader.loadTrieViaHTML(self.path)
        """ 
           pageOccurrences keeps a reference to every trie.pages[] array that trie.findContainingPages() returns.
           During filtering, we cycle through all the trie.pages[] arrays it contains.
           1 array == 1 search word
        """
        self.pageOccurrences = []

    def parseQuery(self, query):
        operator_counter = 0
        token_counter = 0
        self.pageOccurrences.clear()        # clear the list of any previous queries

        tokens = query.split(" ")
        words = []
        self.operator = Operator.OR         # default operator is OR

        for token in tokens:
            token_counter += 1
            if token.lower() == 'and':
                operator_counter += 1
                if Config.isGreater(operator_counter, 1) or token_counter == tokens.__len__():
                    print("Incorrect expression.")
                    return
                self.operator = Operator.AND
            elif token.lower() == 'not':
                operator_counter += 1
                if Config.isGreater(operator_counter, 1) or token_counter == tokens.__len__():
                    print("Incorrect expression.")
                    return
                self.operator = Operator.NOT
            elif token.lower() == 'or':
                operator_counter += 1
                if Config.isGreater(operator_counter, 1) or token_counter == tokens.__len__():
                    print("Incorrect expression.")
                    return
            else:
                words.append(token)
                pages = self.htmlLoader.trie.findContainingPages(token.lower())
                _set = arrayToSet(self.htmlLoader, pages)
                self.pageOccurrences.append(_set)
        result_set = self.executeQuery()
        ranks = page_rank(5, self.htmlLoader.pages, self.htmlLoader.graph, self.htmlLoader, words, result_set)
        Config.print_ranks(ranks)

    def executeQuery(self):
        _set1 = self.pageOccurrences[0]
        if self.operator == Operator.NOT:
            if self.pageOccurrences.__len__() != 1:     # "not python"
                _set2 = self.pageOccurrences[1]
                return _set1.complement(_set2)
            else:                                       # "python not module"
                return _set1.complementUniversal(self.htmlLoader)

        _set2 = self.pageOccurrences[1]
        if self.operator == Operator.OR:                # "python or module"
            return _set1.__or__(_set2)
        elif self.operator == Operator.AND:             # "python and module"
            return _set1.__and__(_set2)


" Runnable part of the application. "
consoleUI = ConsoleUI()
complexParser = ComplexParser(consoleUI.htmlLoader)
polishNotation = PolishNotation(consoleUI.htmlLoader)

userInput = ""

while userInput != 'Q':
    query = input("Search (double space for complex query): ")
    if not query.startswith("  "):
        consoleUI.parseQuery(query)     # Regular search
    else:
        complexParser.parseQuery(query.strip())     # If query starts with double space, do a complex search
        _resultSet = polishNotation.calculateResultSet(complexParser.output)
        if _resultSet != -1:
            _resultSet.print_set()
        else:
            print("No resulting set available.")

    print("Press Q to exit, or any button to repeat search: ", end="")
    userInput = input()







