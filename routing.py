import json

with open('Mst_graph.json', 'r') as file:
    data = json.load(file)
updated  = data['nodes'][1]
print(updated)