import os

from Graph.graph import Graph
from Graph.page import Page
from TrieParser.parser import Parser

"""
    Potentially redundant class!
    Graph loading has been moved to HtmlLoader class, to prevent double parsing.
    
"""
class GraphLoader:

    def __init__(self):
        self.graph = Graph()
        self.pages = []

    def load_graph(self):
        parser = Parser()
        path = "C:\\Users\\Gudli\\Desktop\\OISISI Drugi projekat\\python-2.7.7-docs-html"
        #path =  "C:\\Users\\Asus\\Desktop\\Projekat_Python\\python-2.7.7-docs-html"

        """
            For each html file in the specified directory, a new object which represents an html page and all the pages
            it links to is created and added into a list of pages
        """
        for root, dirs, files in os.walk(path, topdown=True):
            for filename in files:
                if r".html" in filename:
                    parser.parse(os.path.join(root, filename))
                    page = Page(os.path.join(root, filename), parser.links)
                    self.pages.append(page)

        """
            Looping through the list of html pages and adding them into a graph as vertices
        """
        for page in self.pages:
            self.graph.insert_vertex(Graph.Vertex(page.path))

        """
            Looping through the list of html pages and creating edges between the current page and the pages it links to
        """
        for page in self.pages:
            for link in page.links:
                self.graph.insert_edge(Graph.Vertex(page.path), Graph.Vertex(link))

    def get_graph(self):
        return self.graph

    def get_pages(self):
        return self.pages
