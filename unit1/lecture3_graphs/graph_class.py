"""Test Basic Graphing

The classes in this file were taken from the lecture material provided in the MIT 6.00.2x
Intro to Data Science class.

The classes below are in introduction to creating Adjaceny Lists [wiki](https://en.wikipedia.org/wiki/Adjacency_list)
"""

class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest
    
    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest
    
    def __str__(self):
        return self.src.getName() + ' ->' \
                + self.dest.getName()


class Digraph(object):
    """edges is a dict mapping each node to a list of its children"""
    def __init__(self):
         self.edges = {}
    
    def addNode(self, node):
        if node in self.edges:
            raise ValueError("Duplicate Node")
        else:
            self.edges[node] = []
    
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError("Node note in graph")
        self.edges[src].append(dest)

    def childrenOf(self, node):
        return self.edges[node]
    
    def hasNode(self, node):
        return node in self.edges
    
    def getNode(self, name):
        for x in self.edges:
            if x.getName() == name:
                return x
        raise NameError(name)

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + ' ->'\
                    + dest.getName() + '\n'
        return result[:-1]


class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

def buildCityGraph(graphType):
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago', 'Denver', 'Phoenix', 'Los Angeles'):
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g

if __name__ == "__main__":
    a = buildCityGraph(Graph)
    print(a)