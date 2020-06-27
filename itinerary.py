#TODO: assign a unique ID to each ride so we can use bitmasks for visited!!!

from copy import copy
from enum import Enum
import json
import random



data = json.load(open("times.json"))

start_time = 615
ride_names = sorted(data[str(start_time)].keys())
n = len(ride_names)


def getVisitedArray():
    return [False for _ in range(n)]

class Event(Enum):
    ATTRACTION = "ATTRACTION"
    WALKING = "WALKING"
    WAITING = "WAITING"

class ItineraryNode:
    def __init__(self, time: int, duration: int, eventType: Event, rideId: int = None, pos=0):
        self.pos = 1
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
    
    def print(self):
        lagger = itin
        while itin.prev is not None:
            itin = itin.prev
            itin.next = lagger
            lagger = lagger.prev

        while lagger is not None:
            print(lagger)
            lagger = lagger.next



def printItinerary(itin):

    lagger = itin
    while itin.prev is not None:
        itin = itin.prev
        itin.next = lagger
        lagger = lagger.prev

    while lagger is not None:
        print(lagger)
        lagger = lagger.next

most_rides_ridden = 0
best_itinerary = None
best_visited = None
xc = 0

def rideRides(itinerary, visited, time, maxEndTime, depth):
    global best_itinerary, best_visited, xc
    xc += 1
    if xc % 10**3 == 0 : print(xc)
    if time >= maxEndTime:
        return
    
    if itinerary.pos > most_rides_ridden:
        best_itinerary = itinerary
        best_visited = visited
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
            ride_node.pos = itinerary.pos + 1

            ride_node.prev = copy(itinerary)

            c_visited = list(visited)
            c_visited[i] = True

            '''
            queue.append(
                (
                    ride_node,
                    c_visited,
                    time + ride_duration,
                    depth + 1
                )
            )'''
            
            rideRides(
               ride_node,
               c_visited,
               time + ride_duration,
               maxEndTime,
               depth + 1
            )


    #while queue: rideRides(*(queue.pop()))
    #while queue: rideRides(*(queue.pop(random.randrange(len(queue)))))



base = 60
rideRides(ItineraryNode(0,0,Event.WAITING), getVisitedArray(), time=900, maxEndTime=960, depth=0)
for i in range(8):
    print("Now starting iteratioin...", i)
    rideRides(best_itinerary, best_visited, time=900+base, maxEndTime=900+base+60, depth=0)
    base += 60

printItinerary(best_itinerary)