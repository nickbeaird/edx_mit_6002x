
from depth_first_search import printPath, shortestPath, testSP

def BFS(graph, start, end, toPrint = False):
    """: Breadth First Search example
    
    Arguments:
        graph {[Digraph]} -- [relationship of cities (Nodes)]
        start {[Node]} -- [city]
        end {[Node]} -- [city]
    
    Keyword Arguments:
        toPrint {bool} -- [if True print out path for each call] (default: {False})
    
    Returns:
        [str] -- [description of the first shortest path found]
    """
    initPath = [start]
    pathQueue = [initPath]
    if toPrint:
        print('Current BFS path:', printPath(pathQueue))
    while len(pathQueue) != 0:
        # Get and remove oldest element in pathQueue
        tmpPath = pathQueue.pop(0)
        print('Current BFS path:', printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    return None

testSP('Boston', 'Phoenix')
