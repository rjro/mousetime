# MouseTime 

This is an attempt at writing a psuedo-TSP like program to calculating the fastest way to ride every ride in Disneyland.

Background is that most people walk through Disneyland in a greedy manner. They start at the entrance, and walk to the closest ride with the nearest wait, or they have some heuristic for deciding upon a ride depending on (how much they like it, how far it is, and how long the wait time is).

The idea is that these itineraries are not that efficient. If you've been, you may have noticed some patterns, like rides for smaller children being popular during the day and empty at night, Space Mountain being empty during the day and popular at night, popular rides having relatively short wait-times during a parade, etc.

If you can reasonably predict the wait time of a ride, and you know the walk time between two rides, then you can come up with an "efficient" itinerary that allows you to ride more attractions than a naive walk.

