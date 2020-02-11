__author__ = "Nikola"

import os
import time

from TrieParser.parser import Parser
from TrieParser.trie import Trie
class HtmlLoader(object):

    def __init__(self):
        self.trie = Trie()
        """
            We use a dictionary to identify pages using numbers.
            Storing format: <pageNum>:<pageName>
        """
        self.dict = {}

    def loadTrieViaHTML(self):
        parser = Parser()

        path = "C:\\Users\\Gudli\\Desktop\\OISISI Drugi projekat\\python-2.7.7-docs-html"

        start = time.time()
        """
            OS.Walk() runs through the whole given directory and loads filenames. 
            Then using the os.path.join(root, filename), we are able to get the full path for every .html page.
            Each filename is passed onto the parser, which parses it, and creates a String array <parser.words>, 
            which stores all the words from a single file.
            We then loop through <parser.words> and insert every single one into the Trie structure.
        """

        file_counter = -1
        for root, dirs, files in os.walk(path, topdown = True):
            for filename in files:
                if r".html" in filename:
                    file_counter += 1
                    full_filename = os.path.join(root, filename)
                    self.dict[file_counter] = full_filename

                    parser.parse(full_filename)
                    for word in parser.words:
                        self.trie.insertWord(word, file_counter)

        end = time.time()
        print("Parsed files and loaded the Trie structure in " + str((end - start).__round__(2)) + " seconds.")

    def getDictionary(self):
        return self.dict

    """
        Since all pages are kept in a dictionary in a <pageNum>:<pageName> format, this function 
        returns a corresponding page name for a given page number.
    """
    def getPageName(self, pageNum):
        return self.dict.get(pageNum)

    " Get pageNum for a given page name. "
    def getPageNum(self, pageName):
        for key in self.dict.keys():
            if self.dict[key] == pageName:
                return key
        return -1
