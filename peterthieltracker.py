import requests
import time
import folium


def gen_map(map_points):
    sky_map = folium.Map(location=[0, 0], zoom_start=2)
    folium.PolyLine(map_points, color='red').add_to(sky_map)
    sky_map.save('peter_thiel_plot.html')


username = "YOUR_USERNAME"
password = "YOUR_PASSWORD"

map_points = []

while True:
    sky_data = requests.get('https://opensky-network.org/api/states/all?time=0&icao24=ac145b%27).json()')

    if sky_data['states'] != None:
        map_points.append((sky_data['states'][0][6], sky_data['states'][0][5]))
        gen_map(map_points)
    else:
        print("The Eagle sleeps...for now...")
    time.sleep(87) #<--So you can run the program constantly and not exceed the rate limitation