from TrieParser.loadHtml import HtmlLoader

"""
    Console script which is used as a UI. 
    On initialization, it loads all the HTML files into a Trie structure.
    After the initialization, it allows the user to command different search methods from the terminal.
"""
class ConsoleUI(object):

    def __init__(self):
        self.query = ""
        self.pageOccurrences = []
        self.operator = -1
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
        page_counter = -1
        for pageOccurrences in pageArray:
            page_counter += 1
            if pageOccurrences > 0:
                print(self.htmlLoader.getPageName(page_counter) + " -> ocurrences: " + str(pageOccurrences))

        print("Total occurences in Trie for word \"" + word + "\" = " + str(self.htmlLoader.trie.getTotalWordCount(word)))
        return pageArray

    def searchPageForWord(self):
        pageName = input("Unesite stranicu za pretragu: ")
        pageNum = self.htmlLoader.getPageNum(pageName)
        if pageNum == -1:
            print("Data stranica ne postoji.")
            return
        word = input("Unesite rec za pretragu na stranici \"" + pageName + "\": ")

        word_occurrences = self.htmlLoader.trie.getWordCountForPage(word, pageNum)
        print("Rec \"" + word + "\" se javlja " + str(word_occurrences) + " puta.")

    def parseQuery(self, query):
        " Resetujemo postojeci beleznik pojavljivanja reci "
        self.pageOccurrences = []
        " Defaultni operator je OR "
        self.operator = Operator.OR
        queryTokens = query.split(' ')
        for token in queryTokens:
            if token.lower() == "and":
                self.operator = Operator.AND
            elif token.lower() == "not":
                self.operator = Operator.NOT
            elif token.lower() != "or":
                pageOccurrenceArray = self.htmlLoader.trie.findContainingPages(token)
                if pageOccurrenceArray.__len__() == 0:
                    continue
                while pageOccurrenceArray.__len__() < self.htmlLoader.dict.__len__():
                    pageOccurrenceArray.append(0)
                self.pageOccurrences.append(pageOccurrenceArray)

        resultPages = []
        if self.operator == Operator.OR:
            resultPages = self.OperationOR()
        elif self.operator == Operator.AND:
            resultPages = self.OperationAND()
        else:
            resultPages = self.OperationNOT()

        " Kada dobijemo odgovarajuci binarni niz, printujemo imena stranica koje imaju '1' na indeksu svog broja"
        pageNum = -1
        for page in resultPages:
            pageNum += 1
            if page == 1:
                print(self.htmlLoader.getPageName(pageNum))

    def OperationOR(self):
        numberOfPages = self.htmlLoader.dict.__len__()
        resultPages = [0] * numberOfPages
        for pageIndex in range(0, numberOfPages):
            flag = 0
            for occurrence in self.pageOccurrences:
                if occurrence[pageIndex] > 0:
                    flag = 1
            resultPages[pageIndex] = flag

        return resultPages

    def OperationAND(self):
        numberOfPages = self.htmlLoader.dict.__len__()
        resultPages = [0] * numberOfPages
        for pageIndex in range(0, numberOfPages):
            flag = 1
            for occurrence in self.pageOccurrences:
                if occurrence[pageIndex] == 0:
                    flag = 0
            resultPages[pageIndex] = flag

        return resultPages

    def OperationNOT(self):
        numberOfPages = self.htmlLoader.dict.__len__()
        resultPages = [0] * numberOfPages
        for pageIndex in range(0, numberOfPages):
            flags = [0] * 2
            counter = -1
            for occurrence in self.pageOccurrences:
                counter += 1
                flags[counter] = occurrence[pageIndex]
            if flags[0] == 1 and flags[1] == 0:
                resultPages[pageIndex] = 1
            else:
                resultPages[pageIndex] = 0

        return resultPages


" Klasa za flagovanje odgovarajuce operacije u queriju "
class Operator(enumerate):
    OR = 0
    AND = 1
    NOT = 2


consoleUI = ConsoleUI()

userInput = ""


while userInput != 'Q':
    query = input("Search: ")
    consoleUI.parseQuery(query)
    print("Press Q to exit, or any button to repeat search: ", end = "")
    userInput = input()







