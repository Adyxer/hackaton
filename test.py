import requests
import json
from datetime import datetime
import folium

def get_user_location():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        location = data['loc'].split(',')
        latitude = location[0]
        longitude = location[1]
        return f"{latitude},{longitude}"
    except Exception as e:
        print("Error:", e)
        return None

def get_vehicles_near_user():
    user_location = get_user_location()
    if user_location:
        try:
            latitude, longitude = user_location.split(',')
            latitude = float(latitude)
            longitude = float(longitude)
            # Радиус в градусах, соответствующий примерно 2 км
            radius = 0.018
            # Рассчитываем координаты квадрата вокруг пользователя
            north = latitude + radius
            south = latitude - radius
            east = longitude + radius
            west = longitude - radius
            # Формируем URL для запроса
            url = f"https://spb-transport.gate.petersburg.ru/api/vehicles/{west},{north},{east},{south}"
            response = requests.get(url)
            data = response.json()
            return user_location, data
        except Exception as e:
            print("Error:", e)
            return None
    else:
        return None, None

def parse_date(timestamp):
    try:
        dt_object = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        return dt_object.strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        print("Error:", e)
        return None

def save_data_to_json(filename, user_location, data):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump({'user_location': user_location, 'vehicles': data}, f, ensure_ascii=False, indent=4)
        print("Data saved to", filename)
    except Exception as e:
        print("Error:", e)

user_location, vehicles_data = get_vehicles_near_user()
if user_location and vehicles_data:
    save_data_to_json('vehicles_data.json', user_location, vehicles_data)

# Load the JSON data from the file
with open('vehicles_data.json', 'r') as file:
    data = json.load(file)

# Extract user location
user_location = data['user_location']
print("User Location:", user_location)
print()

# Print vehicle information within 2 km radius of user location
vehicles = data['vehicles']['result']
for vehicle in vehicles:
    lon = vehicle['position']['lon']
    lat = vehicle['position']['lat']
    distance = vincenty((float(user_location.split(',')[0]), float(user_location.split(',')[1])), (lat, lon)).kilometers
    if distance <= 2:
        timestamp = vehicle['timestamp']
        lon = vehicle['position']['lon']
        lat = vehicle['position']['lat']
        direction = vehicle['direction']
        route_id = vehicle['routeId']
        vehicle_label = vehicle['vehicleLabel']
        velocity = vehicle['velocity']
        vehicle_id = vehicle['vehicleId']
        order_number = vehicle['orderNumber']
        license_plate = vehicle['licensePlate']
        direction_id = vehicle['directionId']

        print("Timestamp:", timestamp)
        print("Vehicle ID:", vehicle_id)
        print("Vehicle Label:", vehicle_label)
        print("Route ID:", route_id)
        print("Order Number:", order_number)
        print("License Plate:", license_plate)
        print("Velocity:", velocity)
        print("Direction:", direction)
        print("Direction ID:", direction_id)
        print("Longitude:", lon)
        print("Latitude:", lat)
        print("-" * 50)

# Create map centered around user location
map_center = [float(x) for x in user_location.split(',')]
mymap = folium.Map(location=map_center, zoom_start=13)

# Extract vehicle information and plot on map
for vehicle in vehicles:
    lon = vehicle['position']['lon']
    lat = vehicle['position']['lat']
    vehicle_label = vehicle['vehicleLabel']
    distance = vincenty((float(user_location.split(',')[0]), float(user_location.split(',')[1])), (lat, lon)).kilometers
    if distance <= 2:
        popup_text = f"Vehicle ID: {vehicle_label}<br>Latitude: {lat}<br>Longitude: {lon}"
        folium.Marker(location=[lat, lon], popup=popup_text).add_to(mymap)

# Save the map
mymap.save("vehicles_map.html")
