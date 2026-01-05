import json
import math
with open('Mst_graph.json', 'r') as file:
    data = json.load(file)
edges  = data['edges']
nodes = data['nodes']
def get_neighborhood(building_id):
    dic = []
    for i in edges:
        if (i["from"] == building_id) or (i["to"] == building_id):
            if i["from"] == building_id:
                dic.append(i["to"])
            else:
                dic.append(i["from"])
    if dic:
        #for key, value in dic.items():      
            #print(f'- {key}, ({value}m)')
        return dic
    else:
        return {}
def build_graph():
    graph = {}
    for i in nodes:
        NeighDista_dic_ = {}
        for j in get_neighborhood(i['id']):
            NeighDista_dic_[j] = get_distance(i['id'], j)
        graph[i['id']] = NeighDista_dic_
    return graph
def dijkstra(graph, start, end):
    distance = {}
    visited = set()
    previous = {}
    new_distance = 0
    for i in graph.keys():
        distance[i] = float('inf')
    distance[start] = 0
    print(distance)
    while len(visited) < len(distance.keys()):
        current = None
        min_distance = float('inf')
        for j in distance.keys():
            if j not in visited and distance[j] < min_distance:
                min_distance = distance[j]
                current = j
        if current == None:
            break #because that is not the starting point
        elif  current == end:
            visited.add(current)
            break
        else:
            visited.add(current)
            print(f'visiting: {current}, Distance: {min_distance}')
        for k in graph[current].keys():
            candidate_distance = graph[current][k] + distance[current]
            if candidate_distance < distance[k]:
                distance[k] = candidate_distance
                previous[k] = current

    return distance, previous
def recostruction_path(previous, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current) 
        if current == start:
            break
        current = previous[current]
    path.reverse()
    return path
def get_distance(Loca1, Loca2):
    FirstPoint = []
    SecondPoint = []
    for i in nodes:
        if i['id'] == Loca1:
            FirstPoint.append(i['lat'])
            FirstPoint.append(i['long'])
        elif i['id'] == Loca2:
            SecondPoint.append(i['lat'])
            SecondPoint.append(i['long'])
    return haversine_distance(FirstPoint, SecondPoint)
def haversine_distance(firstSet, SecondSet):
    R = 6371.0
    lati1 = math.radians(firstSet[0])
    long1 = math.radians(firstSet[1])
    lati2 = math.radians(SecondSet[0])
    long2 = math.radians(SecondSet[1])
    dlong = long2 - long1
    dlati = lati2 - lati1
    a = (
        math.sin(dlati / 2) ** 2
        + math.cos(lati1) * math.cos(lati2) * math.sin(dlong / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance * 1000
def direction(graph, path):
    node = get_names()
    print(f'Starting at {node[path[0]]}')
    for i in range(len(path) - 1):
        print(f'Walking to {node[path[i+1]]} ({graph[path[i]][path[i+1]]}m)')
        if path[i+1] == path[-1]:
            print(f'Arrived at {node[path[i+1]]}')

def get_names():
    names = {}
    for nam in nodes:
        names[nam['id']] = nam["name"]
    return names 
def Shortest_path(start, end):
    distance, previous = dijkstra(build_graph(), start, end)
    path = recostruction_path(previous, start, end)
    return distance[end], path
    
if __name__ == "__main__":
   # curLoca = input("Enter your current location")
   # Destination = input("Enter your destination you would like to go")

    dis, path = Shortest_path('cs', 'havener')
    print(path)
    direction(build_graph(), path)
    print(f'Total distance: {dis} m')
    
