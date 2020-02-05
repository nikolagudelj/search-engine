from TrieParser.loadHtml import HtmlLoader

"""
    Console script which is used as a UI. 
    On initialization, it loads all the HTML files into a Trie structure.
    After the initialization, it allows the user to command different search methods from the terminal.
"""
class ConsoleUI(object):

    def __init__(self):
        self.query = ""
        print("Loading HTML files...")
        self.htmlLoader = HtmlLoader()
        self.htmlLoader.loadTrieViaHTML()

    def searchWord(self):
        self.query = input("Enter a word to search: ")
        self.searchTrieForWord(self.query.lower())

    """
        Trazi rec u Trie drvetu, i vraca pageArray polje. 
        Vraca niz imena stranica u kojima se pojavljuje data rec.
    """
    def searchTrieForWord(self, word):
        pageArray = self.htmlLoader.trie.findContainingPages(word)
        page_counter = 0
        for pageOccurrences in pageArray:
            page_counter += 1
            if pageOccurrences > 0:
                print(self.htmlLoader.getPageName(page_counter) + " -> ocurrences: " + str(pageOccurrences))

        return pageArray

    def splitQuery(self, query):
        andQuery = query.split(r"AND")
        # Ovo je tek zapoceto


consoleUI = ConsoleUI()

userInput = ""


while userInput != 'Q':
    consoleUI.searchWord()
    print("Press Q to exit, or any button to repeat search: ", end = "")
    userInput = input()







