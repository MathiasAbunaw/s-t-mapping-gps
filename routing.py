import json

with open('Mst_graph.json', 'r') as file:
    data = json.load(file)
edges  = data['edges']
def get_neighborhood(building_id):
    dic = {}
    for i in edges:
        if (i["from"] == building_id) or (i["to"] == building_id):
            if i["from"] == building_id:
                dic[i["to"]] = i['distance']
            else:
                dic[i["from"]] = i['distance']
    print(f'{building_id} neighbors:')
    if dic:
        for key, value in dic.items():      
            print(f'- {key}, ({value}m)')
    else:
        print(f'No neighbors found for {building_id}')

if __name__ == "__main__":
    building = input("Enter a building you would like: ").strip()
    get_neighborhood(building)
