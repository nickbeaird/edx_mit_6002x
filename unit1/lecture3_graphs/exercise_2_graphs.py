

"""Exercise 2: Get all unique nodes using a Graph class (2 way Digraph Class)

The below code is set to test our understanding of what is a unique node, knowing that the 
Graph class sets to Edge classes in a two way fashion (bi-directional).

Run the following code by running the file with `python exercise_2_graphs.py`
"""

from graph_class import Node, Graph, Edge


nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)

g.addEdge(Edge(g.getNode('ABC'), g.getNode('ACB')))
g.addEdge(Edge(g.getNode('ABC'), g.getNode('BAC')))
g.addEdge(Edge(g.getNode('ACB'), g.getNode('CAB')))
g.addEdge(Edge(g.getNode('BAC'), g.getNode('BCA')))
g.addEdge(Edge(g.getNode('BCA'), g.getNode('CBA')))
g.addEdge(Edge(g.getNode('CAB'), g.getNode('CBA')))

if __name__ == "__main__":
    print(g)