import random

ride_locations = [{"name": "Astro Orbitor", "x": 132, "y": -150}, {"name": "Autopia", "x": 371, "y": -98}, {"name": "Big Thunder Mountain Railroad", "x": -175, "y": -86}, {"name": "Buzz Lightyear Astro Blasters", "x": 186, "y": -133}, {"name": "Casey Jr. Circus Train", "x": -7, "y": 128}, {"name": "Dumbo the Flying Elephant", "x": 41, "y": 108}, {"name": "Finding Nemo Submarine Voyage", "x": 308, "y": -62}, {"name": "Gadget's Go Coaster", "x": -5, "y": 397}, {"name": "Haunted Mansion Holiday", "x": -390, "y": -227}, {"name": "Indiana Jones\u2122 Adventure", "x": -171, "y": -287}, {"name": "Jungle Cruise", "x": -138, "y": -264}, {"name": "King Arthur Carrousel", "x": 21, "y": 84}, {"name": "Mad Tea Party", "x": 100, "y": 94}, {"name": "Matterhorn Bobsleds", "x": 184, "y": 81}, {"name": "Mr. Toad's Wild Ride", "x": 49, "y": 69}, {"name": "Peter Pan's Flight", "x": 35, "y": 37}, {"name": "Pinocchio's Daring Journey", "x": 4, "y": 53}, {"name": "Pirates of the Caribbean", "x": -241, "y": -273}, {"name": "Roger Rabbit's Car Toon Spin", "x": 147, "y": 381}, {"name": "Snow White's Scary Adventures", "x": 8, "y": 32}, {"name": "Space Mountain", "x": 292, "y": -246}, {"name": "Splash Mountain", "x": -521, "y": -126}, {"name": "Star Tours \u2013 The Adventures Continue", "x": 162, "y": -169}, {"name": "Storybook Land Canal Boats", "x": 130, "y": 111}, {"name": "The Many Adventures of Winnie the Pooh", "x": -497, "y": -104}, {"name": "\"it's a small world\"", "x": 190, "y": 243}, {"name": "Alice in Wonderland", "x": 124, "y": 57}, {"name": "Millennium Falcon: Smugglers Run", "x": -320, "y": 323}]

def random_path():
    path = []

    cur_locations = ride_locations.copy()
    random.shuffle(cur_locations)

    
    for loc in cur_locations:
        x, y = int(loc["x"]), int(loc["y"])
        new_x, new_y = x/90, y/90
        path.append((new_x, new_y))

random_path()