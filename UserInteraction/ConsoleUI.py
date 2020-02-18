__author__ = "Nikola"

from os import path

from TrieParser.HtmlLoader import HtmlLoader
from Set.set import arrayToSet

" Enumeration class for easier identification of query operators. "
class Operator(enumerate):
    OR = 0
    AND = 1
    NOT = 2

"""
    Console script which is used as a UI. 
    On initialization, it loads all the HTML files into a Trie structure and creates a Graph
    After the initialization, it allows the user to run different search methods from the terminal.
"""
class ConsoleUI(object):

    def __init__(self):
        self.operator = -1
        self.path = inputPath()
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
        self.pageOccurrences.clear()        # clear the list of any previous queries
        tokens = query.split(" ")
        self.operator = Operator.OR         # default operator is OR
        for token in tokens:
            if token.lower() == 'and':
                self.operator = Operator.AND
            elif token.lower() == 'not':
                self.operator = Operator.NOT
            elif token.lower() != 'or':
                pages = self.htmlLoader.trie.findContainingPages(token.lower())
                _set = arrayToSet(self.htmlLoader, pages)
                self.pageOccurrences.append(_set)
        result_set = self.executeQuery()
        result_set.print_set()

    def executeQuery(self):
        _set1 = self.pageOccurrences[0]
        _set2 = self.pageOccurrences[1]
        if self.operator == Operator.OR:
            result_set = _set1.__or__(_set2)
        elif self.operator == Operator.AND:
            result_set = _set1.__and__(_set2)
        else:
            result_set = _set1.complement(_set2)
        return result_set


def inputPath():
    while True:
        absolute_path = input("Enter the absolute path to your folder: ")
        if not path.exists(absolute_path):
            print("Path does not exist!")
        else:
            return absolute_path


" Runnable part of the application. "
consoleUI = ConsoleUI()

userInput = ""

while userInput != 'Q':
    query = input("Search: ")
    consoleUI.parseQuery(query)
    print("Press Q to exit, or any button to repeat search: ", end="")
    userInput = input()







