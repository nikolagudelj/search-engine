__author__ = "Nikola"

from TrieParser.loadHtml import HtmlLoader

"""
    Console script which is used as a UI. 
    On initialization, it loads all the HTML files into a Trie structure.
    After the initialization, it allows the user to run different search methods from the terminal.
"""
class ConsoleUI(object):

    def __init__(self):
        self.operator = -1
        """ 
            pageOccurrences keeps a reference to every trie.pages[] array that trie.findContainingPages() returns.
            During filtering, we cycle through all the trie.pages[] arrays it contains.
            1 array == 1 search word
        """
        self.pageOccurrences = []

        print("Loading HTML files...")
        self.htmlLoader = HtmlLoader()
        self.htmlLoader.loadTrieViaHTML()

    """
        Displays the number of occurrences for the <word> in the <page>
        <word> and <page> are input via console.
    """
    def searchPageForWord(self):
        pageName = input("Unesite stranicu za pretragu: ")
        pageNum = self.htmlLoader.getPageNum(pageName)
        if pageNum == -1:
            print("Data stranica ne postoji.")
            return
        word = input("Unesite rec za pretragu na stranici \"" + pageName + "\": ")

        word_occurrences = self.htmlLoader.trie.getWordCountForPage(word, pageNum)
        print("Rec \"" + word + "\" se javlja " + str(word_occurrences) + " puta.")

    """
        Parses the given query (e.g. "python AND programming") and divides it into <words> and an <operator>.
        <operator> : AND, OR, NOT
        Then proceeds to get a pages[] array for every <word> in query.
        After gathering 1 pages[] array for every inputted word, it combines the given arrays
        into one final binary array - resultPages[]. 
        In resultPages the rule is the following:
            resultsPages[pageNum] == 0  ->  page doesn't fit the query
            resultsPages[pageNum] == 1  ->  page fits the query
    """
    def parseQuery(self, query):
        " We reset the current page occurrence array, to erase previous query results. "
        self.pageOccurrences = []
        " Default operator is OR. "
        self.operator = Operator.OR
        queryTokens = query.split(' ')

        for token in queryTokens:
            if token.lower() == "and":
                self.operator = Operator.AND
            elif token.lower() == "not":
                self.operator = Operator.NOT
            elif token.lower() != "or":
                pageOccurrenceArray = self.htmlLoader.trie.findContainingPages(token)
                " If the given word doesn't appear in any of the files. "
                if pageOccurrenceArray.__len__() == 0:
                    continue
                " Array must be the same length as the number of pages in total. We append zeros if necessary"
                while pageOccurrenceArray.__len__() < self.htmlLoader.dict.__len__():
                    pageOccurrenceArray.append(0)
                " We add the resulting array to the list of arrays, for further filtering. "
                self.pageOccurrences.append(pageOccurrenceArray)

        " Depending on the state of self.operator, we call an appropriate filter function. "
        if self.operator == Operator.OR:
            resultPages = self.OperationOR()
        elif self.operator == Operator.AND:
            resultPages = self.OperationAND()
        else:
            resultPages = self.OperationNOT()

        """ 
            After getting the appropriate binary array, we print the names of pages that fit the query.
            Given that a page is identified via pageNum, we check whether node.pages[pageNum] == 1 (if yes, we print it)
        """
        print("These are the pages that fit the query \"" + query + "\":")
        pageNum = -1
        for page in resultPages:
            pageNum += 1
            if page == 1:
                print("\t" + self.htmlLoader.getPageName(pageNum))
        print()

    " 3 functions for 3 operators (AND, OR, NOT). "
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
            if flags[0] > 0 and flags[1] == 0:
                resultPages[pageIndex] = 1
            else:
                resultPages[pageIndex] = 0

        return resultPages


" Enumeration class for easier identification of query operators. "
class Operator(enumerate):
    OR = 0
    AND = 1
    NOT = 2


" Runnable part of the application. "
consoleUI = ConsoleUI()

userInput = ""


while userInput != 'Q':
    query = input("Search: ")
    consoleUI.parseQuery(query)
    print("Press Q to exit, or any button to repeat search: ", end = "")
    userInput = input()







