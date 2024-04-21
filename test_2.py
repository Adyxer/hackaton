import json
from math import radians, sin, cos, sqrt, atan2


def parse_json(file_name):
    with open(file_name, 'r') as json_file:
        data = json.load(json_file)
    return data


def calculate_distance(lat1, lon1, lat2, lon2):
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    R = 6371.0

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance


def find_leti_location(stops_data):
    leti_location = (59.9343, 30.3241)

    min_distance = float('inf')
    closest_stop = None

    for stop in stops_data:
        stop_location = (stop['lat'], stop['lon'])
        distance = calculate_distance(*leti_location, *stop_location)

        if distance < min_distance:
            min_distance = distance
            closest_stop = stop

    return closest_stop, min_distance


if __name__ == "__main__":
    stops_data = parse_json("stops_data.json")
    closest_stop, distance = find_leti_location(stops_data)
    print("Closest stop to LETI:", closest_stop['name'])
    print("Distance to LETI:", round(distance, 2), "km")
