from csv import DictReader
from math import radians, cos, sin, asin, sqrt

#


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km


html = open("file.html", "w")
print(f"<ul> ", file=html)

with open("cow.txt") as f:
    reader = DictReader(f)
    for d in reader:
        lon = float(d["lon"])
        lan = float(d["lat"])
        dec = haversine(31.5, 34.75, lon, lan)
        # format_float = "{:,2f}".format(dec)
        print(f'<li> {d["name"]}: {int(dec)}</li> ', file=html)

print(f"</ul> ", file=html)
html.close()
