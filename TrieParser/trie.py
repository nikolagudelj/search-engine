__author__ = "Nikola"

class Trie(object):
    """""
        Every node of a Trie structure contains 26 references to the next Trie node. Every node represents 1 character.
        These 26 base characters represent lower-case alphabetical characters (a-z).
        The idea behind the implementation is that these 26 characters are the most common occurring ones, thus
        by having them all exist at the same time, we know where each letter stands in the array, which in turn
        allows us O(1) time complexity for access.
        In case where we add a non-letter character to the Trie node, we resort to a simple for loop, which
        starts at Trie.nextLetter[26] and loops until the end. If it finds the appropriate character, node becomes
        node->thatCharacter. If it doesn't, a new Trie() is appended to the end of the Trie.nextLetter array.

        Within the node.pages[] array, we keep an integer for every .html page loaded. Each index corresponds to
        a certain page (pages are numerated and kept in a Dictionary in pairs <pageNumber(0-N)>:<pageName>.
        Therefore if we wish to see how many times a word "python" appears in page "index.html", we look in the dictionary
        to see what is the pageNumber for the page "index.html". Say that number is 'k'. Then we go down the nodes
        to match the word "python". In the 'N' node, we look at node.pages[k], to see how many times the word appears
        in "index.html".
    """

    def __init__(self):
        self.nextLetter = [None] * 26
        self.pages = []

    def insertWord(self, word, pageNum):
        node = self
        word = word.lower()
        for c in word:
            index = node.getArrayPosition(c, 1)
            node = node.nextLetter[index]

        while node.pages.__len__() <= pageNum:
            node.pages.append(0)
        node.pages[pageNum] += 1

    def getArrayPosition(self, char, flag):
        """
            Function which returns the index of a character in the Node.nextLetter array.
            Flag parameter defines whether we want to CREATE a new node for a character (flag == 1), or
            if we want to see if such a node exists (flag == 0)
        """
        if ord(char) in range(ord('a'), ord('z') + 1):
            index = ord(char) - ord('a')
            if self.nextLetter[index] is None:
                if flag == 1:
                    self.nextLetter[index] = Trie()
                else:
                    return -1
            return index
        else:
            index = 26
            list_length = self.nextLetter.__len__()

            while index < list_length:
                if self.nextLetter[index].value == char:
                    return index
                index += 1

            " Flag determines whether we create a new node or not"
            if flag == 0:
                return -1
            self.nextLetter.append(Trie())
            self.nextLetter[index].value = char

            return index

    " Returns the array index value for the given character. "
    def getTrieArrayIndexForChar(self, char):
        return self.getArrayPosition(char, 0)

    " Returns the node.pages[] for a given word parameter. "
    def findContainingPages(self, word):
        node = self
        for char in word:
            index = node.getTrieArrayIndexForChar(char)
            if index == -1:
                return {}
            else:
                node = node.nextLetter[index]

        return node.pages

    " Returns the total number of occurrences for <word> in ALL the parsed pages "
    def getTotalWordCount(self, word):
        node = self

        for char in word:
            index = node.getArrayPosition(char, 0)
            if index == -1:
                return 0
            node = node.nextLetter[index]

        word_count = 0
        for pageCount in node.pages:
            word_count += pageCount

        return word_count

    " Returns total word count for <word> in the page identified via <pageNum> "
    def getWordCountForPage(self, word, pageNum):
        node = self

        for char in word:
            index = node.getArrayPosition(char, 0)
            if index == -1:
                return 0
            node = node.nextLetter[index]

        if node.pages.__len__() < pageNum + 1:
            return 0
        return node.pages[pageNum]