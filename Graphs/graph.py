from vertex import Vertex
from queue import Queue

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.time = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def getVertices(self):
        return self.vertList.keys()

    def addEdge(self, fromV, toV, cost=0):
        if fromV not in self.vertList:
            self.addVertex(fromV)
        if toV not in self.vertList:
            self.addVertex(toV)
        self.vertList[fromV].addNeightbor(self.vertList[toV], cost)

    def getEdges(self):
        return [vert.getConnections() for vert in self.vertList]

    # -------------------------- DOT-notation GRAPH PRINTING ------------------
    def getDot(self):
        from graphviz import Digraph
        dot = Digraph(comment="Wizualizacja grafu")

        for vert in self.vertList.values():
            dot.node(str(vert.id), str(vert.id))
            for conn in vert.getConnections():
                dot.edge(str(vert.id), str(conn))

        print(dot.source)

    # -------------------------  SEARCH METODS --------------------------------
    # Breadthfist searching
    def breadthfistSearch(self, start, finish):
        if not isinstance(start, Vertex):
            start = self.getVertex(start)
        if not isinstance(finish, Vertex):
            finish = self.getVertex(finish)

        vertQueue = Queue()
        vertQueue.enqueue(start)
        while (vertQueue.size() > 0):
            currentVert = vertQueue.dequeue()
            for nbr in currentVert.getConnections():
                if (nbr.getColor() == 'white'):
                    nbr.setColor('gray')
                    nbr.setPred(currentVert)
                    vertQueue.enqueue(nbr)
            currentVert.setColor('black')

        fin = finish

        while fin.getPred():
            print(fin.getId())
            fin = fin.getPred()
        print(fin.getId())

    # Depthfist searching
    def depthfistSearch(self, start, finish):
        if not isinstance(start, Vertex):
            start = self.getVertex(start)
        if not isinstance(finish, Vertex):
            finish = self.getVertex(finish)

        for vertex in self:
            vertex.setColor('white')
            vertex.setPred(-1)

        self.found = False

        self.dfsvisit(start, finish)

    def dfsvisit(self, start, finish):
        start.setColor('gray')
        print(str(start.id) + ' -> ', end='')
        if start == finish:
            self.found = True
            print('found')
            return
        for vertex in start.getConnections():
            if vertex.getColor() == 'white':
                if not self.found:
                    self.dfsvisit(vertex, finish)

        start.setColor('black')

    # ------------------ TOPOLOGICAL SORTING --------------------------

    def timeVertex(self, start):
        self.time = 0
        for vertex in self:
            vertex.setColor('white')
            vertex.setPred(-1)

        self.visitVertex(start)
        for vertex in self:
            if vertex.getColor() == 'white':
                self.visitVertex(vertex)

    def visitVertex(self, currentVertex):
        currentVertex.setColor('gray')
        self.time += 1
        currentVertex.setDiscovery(self.time)
        for nextVertex in currentVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(currentVertex)
                self.visitVertex(nextVertex)
        currentVertex.setColor('black')
        self.time += 1
        currentVertex.setFinish(self.time)

    def sortTopol(self, start):
        if not isinstance(start, Vertex):
            start = self.getVertex(start)
        self.timeVertex(start)

        self.topList = []
        for vertex in self:
            self.topList.append((vertex.fin, vertex))
        print("\n------------- TOPOLOGICAL SORTING ------------------")
        for vertex in sorted(self.topList, reverse=True):
            times = '({}/{})'.format(vertex[1].disc, vertex[1].fin)
            print(vertex[1].id, times, ' -> ', end='')
        print("\n")
    # ------------------------------------------------------------------------------


    def shortestPath(self, start):
        if not isinstance(start, Vertex):
            start = self.getVertex(start)

        for vertex in self:
            vertex.setColor('white')
            vertex.setPred(None)
            vertex.setDistance(0)

        vertQueue = Queue()
        vertQueue.enqueue(start)
        while (vertQueue.size() > 0):
            currentVert = vertQueue.dequeue()
            for nbr in currentVert.getConnections():
                if (nbr.getColor() == 'white'):
                    nbr.setColor('gray')
                    nbr.setDistance(currentVert.getDistance() + 1)
                    nbr.setPred(currentVert)
                    nbr.setPath()
                    vertQueue.enqueue(nbr)
            currentVert.setColor('black')

        print("\n---------------- SHORTEST PATHS IN GRAPH ------------------")
        for vertex in self:
            print(vertex.getPath())


    def __contains__(self, item):
        return n in self.vertList

    def __iter__(self):
        return iter(self.vertList.values())


# Build simple graph for testing graph class
def buildGraph():
    graph = Graph()
    graph.addVertex('Kalafiory')

    graph.addEdge('Kalafiory', 'Pomarancze')
    graph.addEdge('Kalafiory', 'Rzepy')
    graph.addEdge('Pomarancze', 'Banany')
    graph.addEdge('Pomarancze', 'Mandarynki')
    graph.addEdge('Pomarancze', 'Kalafiory')
    graph.addEdge('Rzepy', 'Banany')
    graph.addEdge('Banany', 'Mandarynki')
    graph.addEdge('Banany', 'Pomarancze')
    graph.addEdge('Banany', 'Rzepy')
    graph.addEdge('Kalafiory', 'Jablka')
    graph.addEdge('Jablka', 'Gruszki')

    return graph

if __name__ == "__main__":

    graph = buildGraph()
    graph.getDot()
    graph.breadthfistSearch('Rzepy', 'Mandarynki')
    graph.depthfistSearch('Rzepy', 'Gruszki')
    graph.sortTopol('Rzepy')
    graph.shortestPath('Kalafiory')
