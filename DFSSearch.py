from GraphList import loadGraph

White = 0
Gray  = 1
Black = 2


class DFSSearch:
    def __init__(self, graph, s):
        self.graph = graph
        self.start = s
        
        self.color = {}
        self.pred = {}

        for v in self.graph.edges:
            self.color[v] = White
            self.pred[v] = None
        
        self.dfs_search(s)

    def dfs_search(self, u):

        self.color[u] = Gray
        for v in self.graph.edges[u]:
            if self.color[v] == White:
                self.pred[v] = u
                self.dfs_search(v)
        self.color[u] = Black

    def dfs_solution(self, v):
        path = [v]
        
        if v not in self.graph.edges:
            return False

        if self.pred[v] is None:
            return None

        while v != self.start:
            v = self.pred[v]
            path.insert(0, v)

        return path

g = loadGraph()
gr = DFSSearch(g, 3)

print(gr.dfs_solution(5))