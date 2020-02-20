import time
from Graph.graph import Graph
from math import log


"""
    This is an iterative algorithm used for ranking html pages. Initially, all pages are ranked 1/n, where n is the total number
    of pages. In each iteration, rank of page A is given by the following formula:
        rank(A) = log(wcA + 1, 100)*((1 - d) + d * Σ(rank(Bi) / L(Bi)*(1 + log(wcBi + 1, 100)))
        wcA - total number of searched keywords on page A
        wcBi - total number of searched keywords on page Bi
        d - damping factor (suggested value is 0.85)
        Bi - pages which link to page A
        L(Bi) - total number of pages Bi links to
    Pages are ranked and kept in a dictionary, in pairs of <page_path>:<rank>

    Arguments required are:
        max_iter - maximum number of iterations for the algorithm
        pages - a list of all pages in the graph
        graph - a graph which represents pages and links between them
        htmlLoader - HtmlLoader object (used for calling certain methods)
        words - a list of keywords which need to be contained
"""


def page_rank(max_iter, pages, graph, htmlLoader, words, result_set):
    start = time.time()
    print("Ranking pages...")
    rank = {}
    d = 0.85
    n = len(pages)
    for page in pages:
        rank[page.path] = 1/n

    for i in range(max_iter):
        for page in pages:
            incoming_edges = graph.incident_edges(Graph.Vertex(page.path), False)
            vertices = []
            for edge in incoming_edges:
                vertices.append(edge.origin())

            rank_sum = 0
            for vertex in vertices:
                word_count = 0
                for word in words:
                    word_count += htmlLoader.trie.getWordCountForPage(word, htmlLoader.getPageNum(vertex.element()))
                rank_sum = rank_sum + (rank[vertex.element()]/len(graph.incident_edges(vertex)))*(1 + log(word_count + 1, 100))

            word_count = 0
            for word in words:
                word_count += htmlLoader.trie.getWordCountForPage(word, htmlLoader.getPageNum(page.path))
            rank[page.path] = ((1-d) + d*rank_sum)*log(word_count + 1, 100)

    end = time.time()
    print("Ranked all pages in " + str((end - start).__round__(2)) + " seconds.")

    return sort_ranks(rank, result_set)

def sort_ranks(rank, result_set):
    rank_list = []
    for key in result_set.set:
        rank_list.append([key, rank[key]])
    quick_sort(rank_list, 0, len(rank_list) - 1)
    return rank_list


def quick_sort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quick_sort(arr, left, pivot - 1)
        quick_sort(arr, pivot + 1, right)


def partition(arr, left, right):
    pivot = arr[right][1]
    i = left - 1

    for j in range(left, right):
        if arr[j][1] <= pivot:
            i = i + 1
            arr[i][1], arr[j][1] = arr[j][1], arr[i][1]

    i = i + 1
    arr[i][1], arr[right][1] = arr[right][1], arr[i][1]
    return i



