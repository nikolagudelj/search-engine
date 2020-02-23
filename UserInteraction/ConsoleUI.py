__author__ = "Nikola"

import sys

from BasicQuery.BasicParser import BasicParser
from Misc.Config import Config
from ComplexQuery.ComplexParser import ComplexParser
from ComplexQuery.PolishNotation import PolishNotation
from PageRank.rank import page_rank
from Set.set import arrayToSet
from TrieParser.HtmlLoader import HtmlLoader
from TrieParser.trie import Trie


class ConsoleUI(object):
    """
        Console script which is used as a UI.
        On initialization, it loads calls the loading functions from Trie/HtmlLoader/Graph.
        After the initialization, it allows the user to run different search methods from the terminal.
    """

    def __init__(self):
        self.loader = HtmlLoader()
        self.complexParser = ComplexParser(self.loader)
        self.basicParser = BasicParser(self.loader)
        self.polishCalculator = PolishNotation(self.loader)

    def start(self):
        """
            Starts an infinite loop, taking input from user, and calling the Complex/Basic parser (input dependent)
            Exits when 'Q' is recognized.
        """
        userInput = ""

        while userInput != 'Q':
            query = input("Search (double space for complex query): ")
            if not query.startswith("  "):
                self.basicParser.parseQuery(query.strip())      # Regular search
            else:
                self.complexParser.parseQuery(query.strip())  # If query starts with double space, do a complex search
                _resultSet = self.polishCalculator.calculateResultSet(self.complexParser.output)
                if _resultSet != -1:
                    _resultSet.print_set()
                else:
                    print("No resulting set available.")

            print("Press Q to exit, or any button to repeat search: ", end="")
            userInput = input()


" Runnable part of the application. "
consoleUI = ConsoleUI()
consoleUI.start()


#     C:\Users\Gudli\Desktop\OISISI Drugi projekat\python-2.7.7-docs-html
#     C:\Users\Asus\Desktop\Projekat_Python\python-2.7.7-docs-html







