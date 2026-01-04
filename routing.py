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
        graph[i['id']] = get_neighborhood(i['id'])
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
        for k in graph[current]:
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
    return
def get_distance(Loca1, Loca2):
    FirstPoint = []
    SecondPoint = []
    for i in nodes:
        if i['id'] == Loca1:
            FirstPoint.append(i['x'])
            FirstPoint.append(i['y'])
        elif i['id'] == Loca2:
            SecondPoint.append(i['x'])
            SecondPoint.append(i['y'])
    return math.dist(FirstPoint, SecondPoint)

if __name__ == "__main__":
    # = input("Enter a building you would like: ").strip()
    #distance, previous = dijkstra(build_graph(), "cs", 'havener')
    #print(previous)
   # print(f'Shortest path distance: {distance['havener']}')
   # print(recostruction_path(previous, "cs", 'havener'))
   # print(get_distance('cs', 'library'))
    print(get_neighborhood('havener'))
    print(build_graph())