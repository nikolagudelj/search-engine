class Page:
    path = None    # Path of the page
    links = []     # List of links the page refers to

    def __init__(self, path, links):
        self.path = path
        self.links = links
