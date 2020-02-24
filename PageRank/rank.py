import time
from math import log

from Graph.graph import Graph

"""
   This is an iterative algorithm used for ranking html pages. Initially, all pages are ranked 1/n, where n is the total number
    of pages. In each iteration, rank of page A is given by the following formula:
        rank(A) = (1 - d) + d * (Σ(rank(Bi) / L(Bi)) * (1 + log(wcA/wcAt + 1, 2)))
        wcA - number of searched keywords on page A
        wcAt - total number of words on page A
        d - damping factor (suggested value is 0.85)
        Bi - pages which link to page A
        L(Bi) - total number of pages Bi links to
    Pages are ranked and kept in a dictionary, in pairs of <page_path>:<rank>

    Arguments required are:
        max_iter - maximum number of iterations for the algorithm
        pages - a list of all pages in the graph
        graph - a graph which represents pages and links between them
        htmlLoader - HtmlLoader object (used for calling certain methods)
        words - a set of keywords which need to be contained
        result_set - a set of pages which satisfy the query
"""


def page_rank(max_iter, pages, graph, loader, words, result_set):
    start = time.time()
    print("Ranking pages...")
    word_count_dictionary = {}
    for page in pages:
        word_count_dictionary[page.path] = page.word_count
    rank = {}
    d = 0.85
    n = len(pages)
    for page in pages:
        rank[page.path] = 1 / n

    for i in range(max_iter):
        for page in pages:
            incoming_edges = graph.incident_edges(Graph.Vertex(page.path), False)
            vertices = []
            for edge in incoming_edges:
                vertices.append(edge.origin())

            rank_sum = 0
            for vertex in vertices:
                rank_sum += rank[vertex.element()] / len(graph.incident_edges(vertex))

            word_count = 0
            for word in words.set.keys():
                word_count += loader.trie.getWordCountForPage(word, loader.getPageNum(page.path))
            rank_sum *= (1 + log(word_count / word_count_dictionary[page.path] + 1, 2))
            rank[page.path] = (1 - d) + d * rank_sum

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



