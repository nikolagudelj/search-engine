import TrieParser.loadHtml

"""
    Console script which is used as a UI. 
    On initialization, it loads all the HTML files into a Trie structure.
    After the initialization, it allows the user to command different search methods from the terminal.
"""
class ConsoleUI(object):

    def __init__(self):
        self.query = ""
        print("Loading HTML files...")
        self.trie = TrieParser.loadHtml.loadTrieViaHTML()

    def searchWord(self):
        self.query = input("Enter a word to search: ")
        self.searchTrieForWord(self.query.lower())

    def searchTrieForWord(self, word):
        retVal = self.trie.findWord(word)
        if retVal == -1:
            print("Word " + word + " not found.\n")
        else:
            print("Word " + word + " appears " + str(retVal) + " times.\n")

consoleUI = ConsoleUI()

userInput = ""

while userInput != 'Q':
    consoleUI.searchWord()
    print("Press Q to exit, or any button to repeat search: ", end = "")
    userInput = input()








