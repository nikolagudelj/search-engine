__author__ = "Nikola"

from BasicQuery.Operator import Operator
from Misc.Config import Config
from PageRank.rank import page_rank
from Set.set import arrayToSet
from Set.set import Set


class BasicParser(object):
    """
        Class in charge of parsing the regular/basic query inputted by the user.
    """
    def __init__(self, loader):
        self.loader = loader
        self.operator = -1
        self.pageOccurrences = []
        """ pageOccurrences keeps a reference to every Trie.pages[] array that trie.findContainingPages() returns.
            During filtering, we cycle through all the Trie.pages[] arrays it contains.
            1 array == 1 search word  """

    def parseQuery(self, query):
        """
            Parses the given Basic query. Allowed formats are the following:
                not word
                word and word
                word or word
                word not word
                words (default operation between all words is 'or')

            Prints ranked pages after calculating the result set.
        """
        self.pageOccurrences.clear()  # clear the list of any previous queries

        tokens = query.split(" ")
        words = Set()
        self.operator = Operator.OR  # default operator is OR

        for token in tokens:
            if token.lower() == 'and':
                self.operator = Operator.AND
            elif token.lower() == 'not':
                self.operator = Operator.NOT
            elif token.lower() != 'or':
                if self.operator != Operator.NOT:
                    words.add(token)
                pages = self.loader.trie.findContainingPages(token.lower())
                _set = arrayToSet(self.loader, pages)
                self.pageOccurrences.append(_set)
        result_set = self.executeQuery()

        ranks = page_rank(5, self.loader.pages, self.loader.graph, self.loader, words, result_set)
        Config.print_ranks(ranks)

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