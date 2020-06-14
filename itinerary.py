import json

data = json.load(open("fake_times.json"))

rides = sorted(data[str(0)].keys())

def visitedArray():
    return [False for _ in range(len(rides))]


def rideRides(itinerary, visited, time, depth):
    pass



