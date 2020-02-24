__author__ = "Nikola"

from BasicQuery.Operator import Operator
from Misc.Config import Config
from PageRank.rank import page_rank
from Set.set import arrayToSet


class BasicParser(object):
    def __init__(self, loader):
        self.path = Config.inputPath()
        self.loader = loader
        print("Loading HTML files...")
        self.loader.loadTrieViaHTML(self.path)
        self.operator = -1

        self.pageOccurrences = []
        """ 
           pageOccurrences keeps a reference to every Trie.pages[] array that trie.findContainingPages() returns.
           During filtering, we cycle through all the Trie.pages[] arrays it contains.
           1 array == 1 search word
        """

    def parseQuery(self, query):
        operator_counter = 0
        token_counter = 0
        self.pageOccurrences.clear()  # clear the list of any previous queries

        tokens = query.split(" ")
        words = []
        self.operator = Operator.OR  # default operator is OR

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
                pages = self.loader.trie.findContainingPages(token.lower())
                _set = arrayToSet(self.loader, pages)
                self.pageOccurrences.append(_set)
        result_set = self.executeQuery()
        result_set.print_set()
        #ranks = page_rank(5, self.htmlLoader.pages, self.htmlLoader.graph, self.htmlLoader, words, result_set)
        #Config.print_ranks(ranks)

    def executeQuery(self):
        """
            For the sets contained within self.pageOccurrences, based on the Operator recognized in the query,
            it calculates the resulting set for the given operation.
            Returns the result set.
        """
        _set1 = self.pageOccurrences[0]
        if self.operator == Operator.NOT:
            if self.pageOccurrences.__len__() != 1:         # "python not java"
                _set2 = self.pageOccurrences[1]
                return _set1.complement(_set2)
            else:                                           # "not python"
                return _set1.complementUniversal(self.loader)

        if self.pageOccurrences.__len__() == 1:             # "python"
            return _set1

        _set2 = self.pageOccurrences[1]

        if self.operator == Operator.OR:                # "python or java"
            return _set1.__or__(_set2)
        elif self.operator == Operator.AND:             # "python and java"
            return _set1.__and__(_set2)