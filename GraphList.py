class GraphAdjcaenyList:
    def __init__(self):
        self.edges = {}

    def addEdges(self, edge):
        if edge not in self.edges:
            self.edges[edge] = []

    def addVertex(self, from_v, to_u):
        if from_v not in self.edges:
            self.edges[from_v] = []
        if to_u not in self.edges:
            self.edges[to_u] = []

        if to_u not in self.edges[from_v]:
            self.edges[from_v].append(to_u)

        if from_v not in self.edges[to_u]:
            self.edges[to_u].append(from_v)

    def isEdge(self, from_v, to_u):
        if from_v not in self.edges:
            return False

        if to_u not in self.edges:
            return False

        return to_u in self.edges[from_v]



def loadGraph(simple=None):
    if not simple:
        simple = {
                    1: [2,3,5],
                    2: [1,4],
                    3: [1],
                    4: [2,5],
                    5: [1,4]
                }
    g = GraphAdjcaenyList()
    for v in simple:
        g.addEdges(v)
        for u in simple[v]:
            g.addVertex(u, v)
    return g