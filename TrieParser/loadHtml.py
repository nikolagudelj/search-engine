__author__ = "Nikola"

import os
import time

from TrieParser.parser import Parser
from TrieParser.trie import Trie
class HtmlLoader(object):

    def __init__(self):
        self.trie = Trie()
        " Dictionary koristimo da belezimo parove Stranica : broj stranice"
        self.dict = {}

    def loadTrieViaHTML(self):
        parser = Parser()

        path = "C:\\Users\\Gudli\\Desktop\\OISISI Drugi projekat\\python-2.7.7-docs-html"

        start = time.time()
        """
            OS.Walk() prolazi kroz ceo zadati direktorijum i belezi imena fajlova, kao i path do njih. 
            Zatim pomocu for petlje, uzimamo svaki .html fajl koji smo pronasli i parsiramo ga. 
            Nakon sto isparsiramo svaki, u okviru polja parser.words ce se nalaziti Array Stringova koji predstavljaju 
            reci. Taj Array onda prosledimo strukturi Trie, koja svaku rec ponaosob ubacuje u strukturu.
            Loop se ponavlja za svaki .html fajl dok ne popunimo drvo u potpunosti.
        """

        file_counter = -1
        python_word_counter = 0
        for root, dirs, files in os.walk(path, topdown = True):
            for filename in files:
                if r".html" in filename:
                    file_counter += 1
                    self.dict[file_counter] = filename

                    "Ova linija uzima filename, i spaja ga sa root directorijem, tako da dobijemo Absolute Path"
                    parser.parse(os.path.join(root, filename))
                    print(filename + " " + str(parser.words.__len__()))
                    for word in parser.words:
                        if word == "python":
                            python_word_counter += 1
                        self.trie.insertWord(word, file_counter)

        end = time.time()
        print("Parsed files and loaded the Trie structure in " + str((end - start).__round__(2)) + " seconds.")
        print("Python word occured " + str(python_word_counter) + " times.")

    def getDictionary(self):
        return self.dict

    """
        Since all pages are kept in a dictionary in a "Page number":"Page Name" format, this function 
        returns a corresponding page name for a given page number.
    """
    def getPageName(self, pageNum):
        return self.dict.get(pageNum)

    def getPageNum(self, word):
        for key in self.dict.keys():
            if self.dict[key] == word:
                return key
        return -1
