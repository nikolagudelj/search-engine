__author__ = "Nikola"


class Trie2(object):
    """
        Copy of the Trie class, but instead of predefined nodes, it uses a dictionary for storing characters.
        Performs 3 seconds faster.
    """
    def __init__(self):
        self.dict = {}
        self.pages = []

    def insertWord(self, word, pageNum):
        node = self
        word = word.lower()
        for c in word:
            if c not in node.dict.keys():
                node.dict[c] = Trie2()
            node = node.dict[c]

        while node.pages.__len__() <= pageNum:
            node.pages.append(0)
        node.pages[pageNum] += 1

    " Returns the node.pages[] for a given word parameter. "
    def findContainingPages(self, word):
        node = self
        for c in word:
            if c not in node.dict.keys():
                return {}
            else:
                node = node.dict[c]

        return node.pages
