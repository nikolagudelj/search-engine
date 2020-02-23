class Set:
    """
        Set is implemented as a dictionary where the keys are actually set's elements.
        Accessing keys takes O(1) time.
    """
    def __init__(self):
        self.set = {}

    " No values need to be associated with keys. "
    def add(self, element):
        self.set[element] = None

    " Union of two sets. Returns a new set. Usage: union = A | B where A and B are sets "
    def __or__(self, other):
        ret = Set()
        for element in self.set.keys():
            ret.add(element)
        for element in other.set.keys():
            ret.add(element)
        return ret

    "Intersection of two sets. Returns a new set. Usage: intersection = A & B where A and B are sets "
    def __and__(self, other):
        ret = Set()
        for element in self.set.keys():
            if element in other.set.keys():
                ret.add(element)
        return ret

    "Complement of a set. Returns a new set. 'X' must exist in Set1, and not exist in Set2 "
    def complement(self, other):
        ret = Set()
        for element in self.set.keys():
            if element not in other.set.keys():
                ret.add(element)
        return ret

    def complementUniversal(self, loader):
        """ Uses loader to find the set of ALL pages in the directory. Then returns a complement of that set and
        the one on which the method is being called. """
        file_list = [1] * loader.files.__len__()
        universal_set = arrayToSet(loader, file_list)
        return universal_set.complement(self)

    def exists(self, element):
        return element in self.set.keys()

    def print_set(self):
        for element in self.set.keys():
            print(element)


def arrayToSet(loader, array):
    """ Takes a list argument which contains [x1 x2 x3...], where 'xk' is the number of occurrences of a certain word
        in page whose numeration index is 'k'. Searches for all the pages where xk > 0, and loads their names into a set
    """
    ret = Set()
    page_counter = 0
    for pageOccurrence in array:
        if pageOccurrence > 0:
            page_name = loader.getPageName(page_counter)
            ret.add(page_name)
        page_counter += 1
    return ret
