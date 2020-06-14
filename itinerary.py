from copy import copy
from enum import Enum
import json
import gc

gc.disable()

data = json.load(open("fake_times.json"))
rides = sorted(data[str(0)].keys())
n = len(rides)

def getVisitedArray():
    return [False for _ in range(len(rides))]

class Event(Enum):
    ATTRACTION = "ATTRACTION"
    WALKING = "WALKING"
    WAITING = "WAITING"

class ItineraryNode:
    def __init__(self, time: int, duration: int, eventType: Event, rideId: int = None):
        self.time = time
        self.duration = duration
        self.eventType = eventType
        self.rideId = rideId
        
        self.next = None
        self.prev = None

        self.root = 55
        self.totalTime = 0

    def __str__(self):
        if self.rideId != None:
            return "%s -- %s -- %s -- %s -- %s" % (rides[self.rideId], self.eventType.value, self.time, self.duration, self.totalTime)
        else:
            return "%s -- %s -- %s -- %s" % (self.eventType.value, self.time, self.duration, self.totalTime)



def printItinerary(itin):

    lagger = itin
    while itin.prev is not None:
        itin = itin.prev
        itin.next = lagger
        lagger = lagger.prev

    while lagger is not None:
        print(lagger)
        lagger = lagger.next




def rideRides(itinerary, visited, time, depth):
    
    if all(visited):
        printItinerary(itinerary)
        print("\n\n\n---------")
        return

    for i in range(n):
        if visited[i] == False:
            ride_duration = 5

            ride_node = ItineraryNode(
                time + ride_duration,
                ride_duration,
                Event.ATTRACTION,
                i
            )
            ride_node.prev = copy(itinerary)

            c_visited = list(visited)
            c_visited[i] = True

            rideRides(
               ride_node,
               c_visited,
               time + ride_duration,
               depth + 1
            )



rideRides(ItineraryNode(
    0,
    0,
    Event.WAITING
), getVisitedArray(), 0, 0)