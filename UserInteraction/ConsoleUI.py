__author__ = "Nikola"

import sys

from BasicQuery.BasicParser import BasicParser
from ComplexQuery.ComplexParser import ComplexParser
from ComplexQuery.PolishNotation import PolishNotation
from Misc.Config import Config
from QueryCheck import NonPYLChecker
from QueryCheck.BasicQueryChecker import basicChecker
from TrieParser.HtmlLoader import HtmlLoader
from QueryCheck.ComplexQueryChecker import complexChecker, query_array


class ConsoleUI(object):
    """
        Console script which is used as a UI.
        On initialization, it calls the loading functions from Trie/HtmlLoader/Graph.
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
                query = query.strip()

                #try: NonPYLChecker.checkQuery(query)
                try: basicChecker.parse(Config.adaptQueryForParsing(query))              # Regular search
                except SyntaxError: continue

                self.basicParser.parseQuery(query)
            else:
                query = query.strip()                           # If query starts with double space, do a complex search

                query_array.clear()
                try: complexChecker.parse(query)             # Check whether the complex query is logically correct
                except SyntaxError: continue
                Config.removeNones(query_array)           # Create a list from tokens

                self.complexParser.parseQuery(query_array)      # Pass that list to ComplexParser object
                _resultSet = self.polishCalculator.calculateResultSet(self.complexParser.output)    # Calculate result
                if _resultSet.set:
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







