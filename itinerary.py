from copy import copy
from enum import Enum
import json
import gc

gc.disable()

data = json.load(open("times.json"))
ride_names = sorted(data[str(495)].keys())
n = len(ride_names)

def getVisitedArray():
    return [False for _ in range(n)]

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
        self.endTime = self.time + self.duration

    def __str__(self):
        if self.rideId != None:
            return "%s -- %s -- %s -- %s -- %s" % (ride_names[self.rideId], self.eventType.value, self.time, self.duration, self.endTime)
        else:
            return "%s -- %s -- %s -- %s" % (self.eventType.value, self.time, self.duration, self.endTime)

shortest_itinerary_seen = None
earliest_time = float('inf')

def printItinerary(itin):

    lagger = itin
    while itin.prev is not None:
        itin = itin.prev
        itin.next = lagger
        lagger = lagger.prev

    while lagger is not None:
        print(lagger)
        lagger = lagger.next


executions = 0

def rideRides(itinerary, visited, time, depth):
    global earliest_time, executions

    if executions % (10**5) == 0: print ("Executions:", executions)
    executions += 1

    '''
    if depth == 5:
        if itinerary.endTime < earliest_time:
            earliest_time = itinerary.endTime
            shortest_itinerary_seen = itinerary
            printItinerary(itinerary)
            print("NEW END TIME:", earliest_time)
            print("\n\n\n---------")
        return
    '''
    if depth == n:
        if itinerary.endTime < earliest_time:
            earliest_time = itinerary.endTime
            shortest_itinerary_seen = itinerary
            printItinerary(itinerary)
            print("NEW END TIME:", earliest_time)
            print("\n\n\n---------")
        return

    '''
    if all(visited):
        printItinerary(itinerary)
        print("\n\n\n---------")
        return
    '''

    for i in range(n):
        if visited[i] == False:
            nearest_15_min_interval = 15 * (time//15)

            current_wait_times =data[str(nearest_15_min_interval)]
            ride_name = ride_names[i]

            if ride_name not in current_wait_times:
                return

            ride_duration = current_wait_times[ride_name]

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
), visited=getVisitedArray(), time=495, depth=0)