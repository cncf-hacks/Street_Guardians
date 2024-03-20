import folium

m = folium.Map(location=(5.543367, -73.361205), zoom_start=15, tiles="stadia alidadesmoothdark")

folium.Marker(
    location=[5.539232, -73.360074],
    tooltip="Police",
    popup="Location1",
    icon=folium.Icon(icon="glyphicon glyphicon-plus", color="blue")
).add_to(m)

folium.Marker(
    location=[5.543494, -73.363029],
    tooltip="Sample1",
    popup="Location1",
    icon=folium.Icon(color="green")
).add_to(m)

folium.Marker(
    location=[5.538737, -73.356973],
    tooltip="Sample1",
    popup="Location1",
    icon=folium.Icon(color="blue")
).add_to(m)

folium.Marker(
    location=[5.538737, -73.356973],
    tooltip="Sample2",
    popup="Location2",
    icon=folium.Icon(icon="glyphicon glyphicon-fire", color="red")
).add_to(m)

folium.Marker(
    location=[5.530990, -73.360887],
    tooltip="Sample2",
    popup="Location2",
    icon=folium.Icon(icon="glyphicon glyphicon-flash", color="purple")
).add_to(m)

folium.Marker(
    location=[5.526339, -73.367939],
    tooltip="Sample2",
    popup="Location2",
    icon=folium.Icon(icon="glyphicon glyphicon-tree-deciduous", color="green")
).add_to(m)

m.save("index.html")