class Set:

    """
        Set is implemented as a dictionary where the keys are actually set's elements because accessing keys takes O(1) time.
    """
    def __init__(self):
        self.set = {}

    """
        No values need to be associated with keys.
    """
    def add(self, element):
        self.set[element] = None

    """
        Union of two sets. Returns a new set. Usage: union = A | B where A and B are sets
    """
    def __or__(self, other):
        ret = Set()
        for element in self.set.keys():
            ret.add(element)
        for element in other.set.keys():
            ret.add(element)

    """
        Intersection of two sets. Returns a new set. Usage: intersection = A & B where A and B are sets
    """
    def __and__(self, other):
        ret = Set()
        for element in self.set.keys():
            if element in other.set.keys():
                ret.add(element)
        return ret

    """
        Complement of a set. Returns a new set. Requires the universal set as argument.
    """
    def complement(self, universal_set):
        ret = Set()
        for element in universal_set:
            if element not in self.set.keys():
                ret.add(element)
        return ret

    def exists(self, element):
        return element in self.set.keys()

    def print_set(self):
        for element in self.set.keys():
            print(element)
