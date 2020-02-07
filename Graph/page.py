class Page:
    vertex = None  # Vertex objekat
    links = []     # Lista stringova koja predstavlja stranice na koje cvor upucuje

    def __init__(self, vertex, links):
        self.vertex = vertex
        self.links = links
