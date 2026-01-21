import os
import osmnx as ox
def download_mst_network():
    #coordinate of missouri S&T
    print("Downloading MST maps from open streetMap")
    north = 37.9600
    south = 37.9450
    east = -91.7650
    west = -91.7800
    output_dir = "C:/output"

    #Dowload the walkable road network of MST from openStreetMap 
    print(f"Dowloading road networking for MST")
    G = ox.graph_from_bbox(north, south, east, west, network_type='walk', simplify=True)

    # create a data folder inorder to store the output of ox into a directory 
    os.makedirs('data', exist_ok=True)

    
if __name__ == "__main__":
    print("HI")