class Page:
    path = None    # Path of the page
    links = []     # List of links the page refers to
    word_count = None

    def __init__(self, path, links, word_count):
        self.path = path
        self.links = links
        self.word_count = word_count
