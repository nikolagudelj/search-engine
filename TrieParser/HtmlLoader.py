__author__ = "Nikola"

import os
import time

from TrieParser.parser import Parser
from TrieParser.trie import Trie
from Graph.graph import Graph
from Graph.page import Page

class HtmlLoader(object):

    def __init__(self):
        self.trie = Trie()
        self.graph = Graph()
        self.pages = []
        self.dict = {}      # Dictionary is used to keep record of pages, in the format <PageNumber>:<PageName>

    def loadTrieViaHTML(self):
        parser = Parser()

        path = "C:\\Users\\Gudli\\Desktop\\OISISI Drugi projekat\\python-2.7.7-docs-html"
        #path =  "C:\\Users\\Asus\\Desktop\\Projekat_Python\\python-2.7.7-docs-html"

        start = time.time()
        """
            OS.Walk() runs through the whole given directory and loads filenames. 
            Then using the os.path.join(root, filename), we are able to get the full path for every .html page.
            Each filename is passed onto the parser, which parses it, and creates a String array <parser.words>, 
            which stores all the words from a single file.
            We then loop through <parser.words> and insert every single one into the Trie structure.
            Every Page object (pagename, links) is stored in an array, which is then used to create a Graph structure
            which shows how all the pages are interconnected.
        """

        page_counter = -1
        for root, dirs, files in os.walk(path, topdown=True):
            for filename in files:
                if r".html" in filename:
                    page_counter += 1
                    full_pagename = os.path.join(root, filename)     # Link a page name to a number in a dictionary
                    self.dict[page_counter] = full_pagename

                    parser.parse(full_pagename)                      # Parse the page at the given path

                    page = Page(full_pagename, parser.links)         # Create a new Page object to be used for Graphing
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

    def getDictionary(self):
        return self.dict

    def getGraph(self):
        return self.graph

    " Returns a page name corresponding to the page number which is passed as a parameter. "
    def getPageName(self, pageNum):
        return self.dict.get(pageNum)

    " Return a corresponding page number for a given page name. "
    def getPageNum(self, pageName):
        for key in self.dict.keys():
            if self.dict[key] == pageName:
                return key
        return -1
