__author__ = "Nikola"

import os
import time

from Graph.graph import Graph
from Graph.page import Page
from TrieParser.parser import Parser
from TrieParser.trie import Trie
from TrieParser.trie2 import Trie2


class HtmlLoader(object):

    def __init__(self):
        self.trie = Trie()      # Only change Trie <-> Trie2 here to test the other class
        self.graph = Graph()
        self.pages = []
        self.dict = {}      # Dictionary is used to keep record of pages, in the format <PageNumber>:<PageName>
        self.files = []

    def loadTrieViaHTML(self, path):
        parser = Parser()

        start = time.time()
        """
            By using 'self.getAllFiles(path), we collect the absolute paths for every '.html' file in the given
            directory. Paths are kept within the list 'self.files'. 
            Using a for loop and a parser, we iterate through the list, and parse every file, add its words
            to the Trie structure, and subsequently build a Graph.
        """

        page_counter = -1
        self.getHtmlFiles(path)

        for file in self.files:
            page_counter += 1
            self.dict[page_counter] = file

            parser.parse(file)                      # Parse the page at the given path

            page = Page(file, parser.links)         # Create a new Page object to be used for Graphing
            self.pages.append(page)

            for word in parser.words:                   # Insert every word from the page into Trie
                self.trie.insertWord(word, page_counter)

        " Graph creation below: "
        " Creating a Vertex for every page "
        for page in self.pages:
            self.graph.insert_vertex(Graph.Vertex(page.path))

        " Adding edges for every link between pages "
        for page in self.pages:
            for link in page.links:
                self.graph.insert_edge(Graph.Vertex(page.path), Graph.Vertex(link))

        end = time.time()
        print("Parsed files, loaded Trie and formed a Graph in  " + str((end - start).__round__(2)) + " seconds.")


    " Returns a page name corresponding to the page number which is passed as a parameter. "
    def getPageName(self, pageNum):
        return self.dict.get(pageNum)

    " Return a corresponding page number for a given page name. "
    def getPageNum(self, pageName):
        for key in self.dict.keys():
            if self.dict[key] == pageName:
                return key
        return -1

    " Iterates through all the files and subfolders in the given path folder, and adds .html file names to self.files "
    def getHtmlFiles(self, path):
        for file in os.scandir(path):
            filepath = file.path
            if file.name.endswith('html'):
                self.files.append(filepath)
            elif file.is_dir():
                self.getHtmlFiles(filepath)
