class Graph:
    class Vertex:
        __slots__ = '_element'

        def __init__(self, x):
            self._element = x

        def element(self):
            return self._element
        
        def __hash__(self):
            return hash(self._element)

        def __eq__(self, other):
            return str(self) == str(other)

        def __str__(self):
            return str(self._element)

    class Edge:

        __slots__ = '_origin', '_destination', '_element'

        def __init__(self, u, v, x):

            self._origin = u
            self._destination = v
            self._element = x

        def endpoints(self):
            return self._origin, self._destination

        def opposite(self, v):
            if not isinstance(v, Graph.Vertex):
                raise TypeError('v must be a Vertex')
            return self._destination if v is self._origin else self._origin

        def element(self):
            return self._element

        def destination(self):
            return self._destination

        def origin(self):
            return self._origin

        def __hash__(self):  # will allow edge to be a map/set key
            return hash((self._origin, self._destination))

        def __str__(self):
            return '({0},{1},{2})'.format(self._origin, self._destination, self._element)

    def __init__(self):
        self._outgoing = {}
        self._incoming = {}

    def _validate_vertex(self, v):
        if not isinstance(v, self.Vertex):
            raise TypeError('Vertex expected')
        if v not in self._outgoing:
            raise ValueError('Vertex does not belong to this graph.')

    def is_directed(self):
        return self._incoming is not self._outgoing  # directed if maps are distinct

    def vertex_count(self):
        return len(self._outgoing)

    def vertices(self):
        return self._outgoing.keys()

    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total

    def edges(self):
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result

    def get_edge(self, u, v):
        self._validate_vertex(u)
        self._validate_vertex(v)
        return self._outgoing[u].get(v)  # returns None if v not adjacent

    def degree(self, v, outgoing=True):
        self._validate_vertex(v)
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        self._validate_vertex(v)
        ret = []
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            ret.append(edge)
        return ret

    def insert_vertex(self, v):
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v

    def insert_edge(self, u, v, x=None):
        if self.get_edge(u, v) is not None:
            raise ValueError('u and v are already adjacent')
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e
