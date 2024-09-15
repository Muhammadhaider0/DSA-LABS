from helper_functions import *


def one_way_connection(G):
    for nodes in G:
        for edges in G[nodes]:
            if nodes in 


def nearest_airport(G, A):
    pass

def not_more_than_one_intermediate(G, node):
    pass



'''
EXPECTED OUTPUT:

GRAPH
{'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900)], 'Austin': [('Dallas', 200), ('Houston', 160)], 'Washington': [('Dallas', 1300), ('Atlanta', 600)], 'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 'Atlanta': [('Washington', 600), ('Houston', 800)], 'Chicago': [('Denver', 1000)], 'Houston': [('Atlanta', 800)]}

ONE WAY CONNECTION
[('Dallas', 'Denver'), ('Dallas', 'Chicago'), ('Austin', 'Houston'), ('Washington', 'Dallas'), ('Denver', 'Atlanta')]

NEAREST AIRPORT
Dallas : Austin
Austin : Houston
Washington : Atlanta
Denver : Chicago
Atlanta : Washington
Chicago : Denver
Houston : Atlanta

CONNECTED WITH NOT MORE THAN ONE INTERMEDIATE AIRPORT
Dallas : ['Austin', 'Washington', 'Atlanta']

REMOVING WASHINGTON, ADDING PATH FROM ATLANTA TO DALLAS AND DISPLAYING A GRAPH
{'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900), ('Atlanta', 1700)], 'Austin': [('Dallas', 200), ('Houston', 160)], 'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 'Atlanta': [('Houston', 800), ('Dallas', 1700)], 'Chicago': [('Denver', 1000)], 'Houston': [('Atlanta', 800)]}
'''
















'''
# Task 1: Create adjacency list representation of the directed and weighted graph
DG = {}
edges_airports = [
    ('Chicago', 'New York', 1000),
    ('Chicago', 'Los Angeles', 2000),
    ('New York', 'Dallas', 800),
    ('Los Angeles', 'Dallas', 1500),
    ('New York', 'Chicago', 900),
    ('Dallas', 'New York', 1000),
    ('Dallas', 'Los Angeles', 800)
]

addNodes(DG, ['Chicago', 'New York', 'Los Angeles', 'Dallas'])
addEdges(DG, edges_airports, directed=True)

# Task 2: Function to find one-way connections
def oneWayConnections(graph):
    one_way_pairs = []
    for node in listOfNodes(graph):
        neighbors = getNeighbors(graph, node)
        for neighbor in neighbors:
            reverse_edge = (neighbor, node, None)  # Representing reverse edge without weight
            if reverse_edge not in listOfEdges(graph):
                one_way_pairs.append((node, neighbor))
    return one_way_pairs

# Task 3: Function to find the nearest airport
def nearestAirport(graph, airport):
    return getNearestNeighbor(graph, airport)

# Task 4: Function to find airports with not more than one intermediate airport
def airportsWithOneIntermediate(graph, airport):
    neighbors = getNeighbors(graph, airport)
    result = []
    for neighbor in neighbors:
        intermediate_airports = getNeighbors(graph, neighbor)
        intermediate_airports.remove(airport)
        result.extend([(airport, intermediate, neighbor) for intermediate in intermediate_airports])
    return result

# Task 5: Update graph with new route and display
DG['Atlanta'] = [('Dallas', 1700)]
displayGraph(DG)

# Example usage:
print("One-way connections:", oneWayConnections(DG))
print("Nearest airport from Chicago:", nearestAirport(DG, 'Chicago'))
print("Airports with not more than one intermediate from New York:", airportsWithOneIntermediate(DG, 'New York'))'''