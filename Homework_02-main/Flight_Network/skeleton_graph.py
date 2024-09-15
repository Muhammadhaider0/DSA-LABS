import csv

def addVertices(G: dict, vertices: list):
    for vertex in vertices:
        if vertex not in G:
            G[vertex] = {}

def addEdges(G: dict, edges: list):
    for edge in edges:
        source, destination, weight = edge
        if source in G:
            G[source][destination] = weight
        else:
            G[source] = {destination: weight}

def create_flight_network(filename: str, option: int):
    graph={}

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            origin =row[0]
            destination= row[1]
            weight= int(row[2]) if option == 1 else int(row[3])
            if origin not in graph:
                graph[origin]= {}
            graph[origin][destination]= weight

    return graph


def get_flight_connections(graph: dict, city: str, option: str) -> list:
    connections= []
    if option== 'i':
        for origin in graph:
            if city in graph[origin]:
                connections.append(origin)
    elif option == 'o':
        if city in graph:
            connections = list(graph[city].keys())
#    else:
    return connections

def get_number_of_flight_connections(graph: dict, 
                                     city: str, 
                                     option: str) -> int:

    connections= get_flight_connections(graph, city, option)

    return len(connections)


"""   if option== 'i':
        for origin in graph:
            if city in graph[origin]:
                connections.append(origin)
    elif option == 'o':
        if city in graph:
            connections = list(graph[city].keys())"""



def get_flight_details(graph: dict, origin: str, destination: str) -> int:

    if origin in graph and destination in graph[origin]:
        return graph[origin][destination]
    
    return None

def add_flight(graph: dict, origin: str, destination: str, weight: int):
    
    if origin not in graph:
        graph[origin] = {}
    graph[origin][destination] = weight
    
    print(f"Flight from {origin} to {destination} added with weight {weight}.")

def add_airport(graph: dict, city: str, destination: str, weight: int):
    
    if city in graph:
        print(f"Airport {city} already exists in the network.")
    
    else:
        graph[city]= {destination: weight}
        print(f"Airport {city} added with connection to {destination} with weight {weight}.")

def get_secondary_flights(graph: dict, city: str):
    immediate_connections= list(graph[city].keys()) if city in graph else []
    secondary_connections= []
    
    for connection in immediate_connections:
    
        if connection in graph:
            secondary_connections.extend(graph[connection].keys())
    
    return secondary_connections


def counting_common_airports(graph: dict, cityA: str, cityB: str) -> int:
    
    my_airports = set(get_flight_connections(graph, cityA, 'o')).intersection(set(get_flight_connections(graph, cityB, 'o')))
    return len(my_airports)

def remove_flight(graph: dict, origin: str, destination: str):

    if origin in graph and destination in graph[origin]:
        del graph[origin][destination]
        print(f"Flight connection between {origin} and {destination} removed.")

    else:
        print(f"Flight connection between {origin} and {destination} does not exist.")

def remove_airport(graph: dict, city: str):
    
    if city in graph:
        del graph[city]
        for i in graph:
            if city in graph[i]:
                del graph[i][city]
        print(f"Airport {city} removed from the network.")
    
    else:
        print(f"Airport {city} does not exist in the network.")

def DFS_all_routes(graph: dict,
                    origin: str, 
                    destination: str,
                    route: list, 
                    all_routes: list):
    route= route + [origin]

    if origin == destination:
        all_routes.append(route)
        return

    for node in graph.get(origin, {}):
        if node not in route:
            DFS_all_routes(graph, node, destination, route.copy(), all_routes)


def find_all_routes(graph: dict, origin: str, destination: str):
    all_routes=[]
    DFS_all_routes(graph, origin, destination, [], all_routes)
    return all_routes

def DFS_layovers(graph: dict, origin: str, destination: str, 
                 route: list, 
                 layovers_lst: list):
    route= route + [origin]
    if origin == destination:
        layovers_lst.append(len(route) - 2)
        return
    for node in graph.get(origin, {}):
        if node not in route:
            DFS_layovers(graph, node, destination, route.copy(), layovers_lst)

def find_number_of_layovers(graph: dict, origin: str, destination: str):
    layovers_lst= []
    DFS_layovers(graph, origin, destination, [], layovers_lst)
    return sorted(layovers_lst)
