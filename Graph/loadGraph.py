import os
from Graph.graph import Graph
from Graph.page import Page
from TrieParser.parser import Parser


class GraphLoader:

    def __init__(self):
        self.graph = Graph()

    def load_graph(self):
        parser = Parser()
        #path = "C:\\Users\\Gudli\\Desktop\\OISISI Drugi projekat\\python-2.7.7-docs-html"
        path =  "C:\\Users\\Asus\\Desktop\\Projekat_Python\\python-2.7.7-docs-html"
        pages = []

        """
            For each html file in the specified directory, a new object which represents an html page and all the pages
            it links to is created and added into a list of pages
        """
        for root, dirs, files in os.walk(path, topdown=True):
            for filename in files:
                if r".html" in filename:
                    parser.parse(os.path.join(root, filename))
                    page = Page(Graph.Vertex(os.path.join(root, filename)), parser.links)
                    pages.append(page)

        """
            Looping through the list of html pages and adding them into a graph as vertices
        """
        for page in pages:
            self.graph.insert_vertex(page.vertex)

        """
            Looping through the list of html pages and creating edges between the current page and the pages it links to
        """
        for page in pages:
            if len(page.links) != 0:
                for link in page.links:
                    self.graph.insert_edge(page.vertex, Graph.Vertex(link))

    def get_graph(self):
        return self.graph
