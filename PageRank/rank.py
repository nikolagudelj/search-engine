import time
from Graph.graph import Graph

"""
    PageRank algorithm is an iterative algorithm. Initially, all pages are ranked 1/n, where n is the total number
    of pages. In each iteration, rank of page A is given by the following formula:
        rank(A) = (1 - d) + d * Σ(rank(Bi) / L(Bi)
        d - damping factor (suggested value is 0.85)
        Bi - pages which link to page A
        L(Bi) - total number of pages Bi links to
    Pages are ranked and kept in a dictionary, in pairs of <page_path>:<rank>

    Arguments required are:
        max_iter - maximum number of iterations for the algorithm
        pages - a list of all pages in the graph
        graph - a graph which represents pages and links between them
"""


def page_rank(max_iter, pages, graph):
    start = time.time()
    rank = {}
    d = 0.85
    n = len(pages)
    for page in pages:
        rank[page] = 1/n

    for i in range(max_iter):
        for page in pages:
            incoming_edges = graph.incident_edges(Graph.Vertex(page.path), False)

            vertices = []
            for edge in incoming_edges:
                vertices.append(edge.origin())

            rank_sum = 0
            for vertex in vertices:
                rank_sum = rank_sum + rank[vertex.element()]/len(graph.incident_edges(vertex))

            rank[page.path] = (1-d) + d*rank_sum

    end = time.time()
    print("Ranked all pages in " + str((end - start).__round__(2)) + " seconds.")

    return rank
