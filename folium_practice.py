import folium

if __name__ == "__main__":
    #create variables 
    map_filepath = "folium.map.html"
    center_coord = [38.825908458819775, -90.95601869227515]
    marker_coord = [37.955501020671036, -91.77383546890499]
    marker_radius = 25_000

    location_marker_coord = [37.95211066819258, -91.77679276668788]
    line_coord = [
        marker_coord,
        location_marker_coord
    ]
    
    polygon_coords = [
        [37.955702683302995, -91.76070446243888],
        [37.95504227322239, -91.78613992900482],
        [37.939712139434896, -91.78428847389951],
        [37.955702683302995, -91.76070446243888]
    ]
    polygon_lines = [
        [polygon_coords[i], polygon_coords[i+1]] for i in range(len(polygon_coords) - 1)
    ]

    # create folium map
    vmap = folium.Map(center_coord, zoom_start= 9)
    #add a martker to the map
    folium.vector_layers.Circle(
        location = marker_coord,
        tooltip =f"The marker has a radius {marker_radius}",
        radius = marker_radius, 
        color = "red",
        fill = True,
        fill_color = "red"
    ).add_to(vmap)

    # add location markere
    folium.Marker(
        location= location_marker_coord,
        tooltip="Duisburg"
    ).add_to(vmap)

    #add a line to folium map
    folium.PolyLine(
        line_coord,
        color = "blue",
        weight="10",
        opacity = 0.8
    ).add_to(vmap)
    #add a line to folium map
    folium.PolyLine(
        polygon_coords,
        color = "blue",
        weight="10",
        opacity = 0.8
    ).add_to(vmap)
    #store the map to a file
    vmap.save(map_filepath)