import os
import osmnx as ox
def download_mst_network():
    #Gets a box of only the campus from open streat
    print("Downloading MST maps from open streetMap")
    north = 37.9600
    south = 37.9450
    east = -91.7650
    west = -91.7800
    output_dir = "C:/output"

    #Dowload the walkable road network from openStreetMap
    print(f"Dowloading road networking from {place_name}")
    G = ox.graph_from_place(place_name, network_type='walk')

    # convert the graph to a GEODATAFRAMES (nodes and Edges)
    nodes, edges = ox.graph_to_gdfs(G)

    #export
if __name__ == "__main__":
    print("HI")