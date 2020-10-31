from collections import defaultdict
import json
import math

data = json.load(open("raw_output.json"))

ride_locations = {


}

for ride in data:
    name = ride["name"]
    lat = ride["meta"]["latitude"]
    lon = ride["meta"]["longitude"]

    ride_locations[name] = [lat, lon]

nested_dict = lambda: defaultdict(nested_dict)
ride_distances = nested_dict()

#return dist between two coords in meters
#https://gmigdos.wordpress.com/2010/03/31/python-calculate-the-distance-between-2-points-given-their-coordinates/
def calculateDistance(coords, ocoords):
    lat1, lon1 = coords
    lat2, lon2 = ocoords

    if ((lat1 == lat2) and (lon1 == lon2)):
        return 0

    delta = lon2 - lon1
    a = math.radians(lat1)
    b = math.radians(lat2)
    C = math.radians(delta)
    x = math.sin(a) * math.sin(b) + math.cos(a) * math.cos(b) * math.cos(C)
    distance = math.acos(x) # in radians
    distance  = math.degrees(distance) # in degrees
    distance  = distance * 60 # 60 nautical miles / lat degree
    distance = distance * 1852 # conversion to meters
    distance  = round(distance)
    return distance


for ride, coords in ride_locations.items():
    for oride, ocoords in ride_locations.items():
        if ride != oride:
            ride_distances[ride][oride] = calculateDistance(coords, ocoords)
            ride_distances[oride][ride] = calculateDistance(coords, ocoords)

print(ride_distances)


json.dump(ride_distances, open("ride_distances.json", "w+"))    