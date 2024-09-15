def addNodes(G, nodes):
    for node in nodes:
        G[node] = []
    

def addEdges(G, edges, directed=False):
    for edge in edges:
        node1, node2, weight = edge
        G[node1].append((node2, weight))
        if not directed:
            G[node2].append((node1, weight))

def displayGraph(G):
    print("G =", G)

def listOfNodes(G):
    A=list(G.keys())
    return (A)

def listOfEdges(G, directed=False):
    edges = []
    visited = set()

    for node in G:
        for neighbor, weight in G[node]:
            if (node, neighbor) not in visited and (neighbor, node) not in visited:
                edges.append((node, neighbor, weight))
                visited.add((node, neighbor))

    return sorted(edges)

def getNeighbors(G, nodes):
    return [neighbor for neighbor, _ in G[nodes]]

def removeNode(G, node):
#    del G[node]
#    for _, edges in G.items():
#        G[node] = [(neighbor, weight) for neighbor, weight in edges if neighbor != node]
    del G[node]

    # Remove all edges connected to the node
#    for _, edges in G.items():
#        G[node] = [(neighbor, weight) for neighbor, weight in edges if neighbor != node]

    # Update other nodes to remove edges pointing to the deleted node
    for _, edges in G.items():
        for i in range(len(edges)):
            neighbor, weight = edges[i]
            if neighbor == node:
                edges.pop(i)
                break

def removeNodes(G, nodes):
    for node in nodes:
        removeNode(G, node)


def getNearestNeighbor(G, node):
    neighbors = G[node]
    if neighbors:
        return min(neighbors, key=lambda x: x[1])[0]
    return None

'''G = { 0: [(1 , 1) , (2, 1)], 1: [(0 , 1) , (2, 1) , (3, 1)
], 2: [(0 , 1) , (1, 1) , (4, 1)], 3: [(1 , 1) , (4, 1) ,
(5, 1)], 4: [(3 , 1) , (2, 1) , (5, 1)], 5: [(3 , 1) , (4,
1)] }
print ( getNeighbors (G, 0))'''
#G = {'BOS': [('JFK', 1), ('MIA', 1), ('SFO', 1)], 'ORD': [('MIA', 1), ('DFW', 1)], 'JFK': [('BOS', 1), ('SFO', 1), ('MIA', 1), ('DFW', 1)], 'DFW': [('ORD', 1), ('SFO', 1), ('LAX', 1)], 'MIA': [('DFW', 1), ('LAX', 1)], 'SFO': [('LAX', 1)], 'LAX': [('ORD', 1)] }
#print(listOfEdges(G,True))
#print(sorted([('BOS', 'JFK', 1), ('BOS', 'MIA', 1), ('BOS', 'SFO', 1), ('ORD', 'MIA', 1), ('ORD', 'DFW', 1), ('JFK', 'SFO', 1), ('JFK', 'MIA', 1), ('JFK', 'DFW', 1), ('DFW', 'SFO', 1), ('DFW', 'LAX', 1), ('MIA', 'DFW', 1), ('MIA', 'LAX', 1), ('SFO', 'LAX', 1), ('LAX', 'ORD', 1)]))