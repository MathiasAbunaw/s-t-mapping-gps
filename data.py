{
    "Node": [ #This creates a data of all the nodes/building with a given dictionary key called ID and their value
        { "id": "cs", "name": "CS Building" },
        { "id": "library", "name": "Library" },
        { "id": "havener", "name": "Havener Center" },
        { "id": "butler", "name": "Butler-Carlton" },
        { "id": "hss", "name": "HSS" }
            
    ],
    "Edge": [
        {"from" : 'cs', "to": "library", "distance": 130},
        { "from": "library", "to": "havener", "distance": 210 },
        { "from": "cs", "to": "butler", "distance": 180 },
        { "from": "butler", "to": "hss", "distance": 160 },
        { "from": "hss", "to": "havener", "distance": 220 }
    ]
}
