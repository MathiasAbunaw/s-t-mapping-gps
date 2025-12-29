import json

with open('Mst_graph.json', 'r') as file:
    data = json.load(file)
edges  = data['edges']
def FindNeighbors(loca):
    dic = {}
    for i in edges:
        if (i["from"] == loca) or (i["to"] == loca):
            if i["from"] == loca:
                dic[i["to"]] = i['distance']
            else:
                dic[i["from"]] = i['distance']
    print(f'{loca} neighbors:')
    for key, value in dic.items():      
        print(f'- {key}, ({value}m)')
    else:
        print(f'No neighbors found for {loca}')

if __name__ == "__main__":
    building = input("Enter a building you would like: ").strip()
    FindNeighbors(building)
