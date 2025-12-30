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
        return None
def build_graph():
    graph = {}
    for i in nodes:
        graph[i['id']] = get_neighborhood(i['id'])
    return graph


if __name__ == "__main__":
    building = input("Enter a building you would like: ").strip()
    print(build_graph())
