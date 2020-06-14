from copy import copy
from enum import Enum
import json
import random

def shift(seq, n):
    return seq[n:]+seq[:n]

data = json.load(open("times.json"))
ride_names = sorted(data[str(495)].keys())
n = len(ride_names)

#ride_names = shift(ride_names, 3)

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

#TODO: exploration needs to be more BFS
#and figure out some way to prune!
def rideRides(itinerary, visited, time, depth):
    global earliest_time, executions

    if executions % (10**6) == 0:
        print ("Executions:", executions)
        print("depth:", depth)
        print("~~~~~~~~~~~")
        printItinerary(itinerary)

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

    queue = []

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

            queue.append(
                (
                    ride_node,
                    c_visited,
                    time + ride_duration,
                    depth + 1
                )
            )

            '''
            rideRides(
               ride_node,
               c_visited,
               time + ride_duration,
               depth + 1
            )'''


    #while queue: rideRides(*(queue.pop()))
    while queue: rideRides(*(queue.pop(random.randrange(len(queue)))))



rideRides(ItineraryNode(
    0,
    0,
    Event.WAITING
), visited=getVisitedArray(), time=495, depth=0)