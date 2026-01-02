import json

with open('Mst_graph.json', 'r') as file:
    data = json.load(file)
edges  = data['edges']
nodes = data['nodes']
def get_neighborhood(building_id):
    dic = {}
    for i in edges:
        if (i["from"] == building_id) or (i["to"] == building_id):
            if i["from"] == building_id:
                dic[i["to"]] = i['distance']
            else:
                dic[i["from"]] = i['distance']
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
        for k in graph[current].keys():
            candidate_distance = graph[current][k] + distance[current]
            if candidate_distance < distance[k]:
                distance[k] = candidate_distance
                previous[k] = current

    return distance, previous
def recostruction_path(previous, start, end):
    path = []
    current = end
    while current != None:
        if current == start:
            break
        path.append(current) 


if __name__ == "__main__":
    # = input("Enter a building you would like: ").strip()
    distance, previous = dijkstra(build_graph(), "cs", 'havener')
    print(previous)

