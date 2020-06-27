import json

data = json.load(open("times.json"))
new_data = {}

common_to_all = set()



for time, rides in data.items():
    for ride in rides:
        common_to_all.add(ride)
    break

for time, rides in data.items():
    temp_rides = set()
    print(time, len(rides))

    for ride in common_to_all:
        if ride in rides:
            temp_rides.add(ride)
    common_to_all = temp_rides

print("---------")
print(len(common_to_all))
print("~~~~~~~~~")

for time, rides in data.items():
    for ride in common_to_all:
        new_data[time][ride] = data[time][ride]

json.dump("times_common.json")
