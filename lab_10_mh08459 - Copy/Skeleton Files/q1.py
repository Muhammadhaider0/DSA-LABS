from helper_functions import *
UG = {1: [(2, 1), (5, 1)], 2: [(1, 1), (3, 1), (4, 1), (5, 1)], 3: [(2, 1), (4, 1)], 4: [(2, 1), (3, 1), (5, 1)], 5: [(1, 1), (2, 1), (4, 1)]}

'''addNodes(UG, listOfNodes(UG))  # Ensure all nodes are added before adding edges
print("Adjacency List Representation of the Graph:")'''
print(UG)

print("\nList of Nodes in the Graph:", listOfNodes(UG))

print("\nList of Edges in the Graph:", listOfEdges(UG))

print("\nNeighbors of Each Node:")
for node in listOfNodes(UG):
    neighbors = getNeighbors(UG, node)
    print(f"Node {node}: {neighbors}")

'''
EXPECTED OUTPUT:

GRAPH
{1: [(2, 1), (5, 1)], 2: [(1, 1), (3, 1), (4, 1), (5, 1)], 3: [(2, 1), (4, 1)], 4: [(2, 1), (3, 1), (5, 1)], 5: [(1, 1), (2, 1), (4, 1)]}

LIST OF NODES
[1, 2, 3, 4, 5]

LIST OF EDGES
[(1, 2, 1), (1, 5, 1), (2, 3, 1), (2, 4, 1), (2, 5, 1), (3, 4, 1), (4, 5, 1)]

NEIGHBOURS FOR EACH NODE IN A GRAPH
1 : [2, 5]
2 : [1, 3, 4, 5]
3 : [2, 4]
4 : [2, 3, 5]
5 : [1, 2, 4]
'''