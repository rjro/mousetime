from bs4 import BeautifulSoup

html = open("disneyland_ride_durations.html").read()
soup = BeautifulSoup(html)
print(html)
rows = soup.find_all("tr")

for row in rows:
    rides = row.get_text().split("\n")[1:-1]
    print(rides)