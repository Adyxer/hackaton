import requests
import json
from datetime import datetime
import math
import folium
from geopy.geocoders import Nominatim

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371.0
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

def get_user_location():
    try:
        geolocator = Nominatim(user_agent="user_location")
        location = geolocator.geocode("СПбГЭТУ")
        latitude = location.latitude
        longitude = location.longitude
        return f"{latitude},{longitude}"
    except Exception as e:
        print("Ошибка при получении местоположения пользователя:", e)
        return None

def get_vehicles_near_user(user_location, radius_km=1):
    if user_location:
        try:
            latitude, longitude = [float(x) for x in user_location.split(',')]
            radius = radius_km / 111
            url = f"https://spb-transport.gate.petersburg.ru/api/vehicles/{longitude - radius},{latitude - radius},{longitude + radius},{latitude + radius}"
            response = requests.get(url)
            data = response.json()
            return user_location, data
        except Exception as e:
            print("Ошибка при получении данных о транспорте:", e)
            return None, None
    else:
        print("Не удалось получить местоположение пользователя.")
        return None, None

def parse_date(timestamp):
    try:
        dt_object = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        return dt_object.strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        print("Ошибка при разборе даты:", e)
        return None

def save_data_to_json(filename, user_location, data):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump({'user_location': user_location, 'vehicles': data}, f, ensure_ascii=False, indent=4)
        print("Данные сохранены в", filename)
    except Exception as e:
        print("Ошибка при сохранении данных в JSON:", e)

def get_university_location():
    try:
        geolocator = Nominatim(user_agent="university_location")
        location = geolocator.geocode("СПбГЭТУ")
        latitude = location.latitude
        longitude = location.longitude
        return f"{latitude},{longitude}"
    except Exception as e:
        print("Ошибка при получении местоположения университета:", e)
        return None

user_location = get_user_location()
university_location = get_university_location()
user_location, vehicles_data = get_vehicles_near_user(user_location)
if user_location and vehicles_data:
    save_data_to_json('vehicles_data.json', user_location, vehicles_data)
else:
    print("Не удалось получить местоположение пользователя и данные о транспорте.")

try:
    with open('vehicles_data.json', 'r') as file:
        data = json.load(file)
except Exception as e:
    print("Ошибка при загрузке данных из JSON:", e)
    exit()

user_location = data.get('user_location')
if not user_location:
    print("Местоположение пользователя не найдено в данных JSON.")
    exit()

print("Местоположение пользователя:", user_location)
print()

map_center = [float(x) for x in user_location.split(',')]
mymap = folium.Map(location=map_center, zoom_start=13)

vehicles = data.get('vehicles', {}).get('result', [])
for vehicle in vehicles:
    lon = vehicle.get('position', {}).get('lon')
    lat = vehicle.get('position', {}).get('lat')
    if lon is None or lat is None:
        continue
    distance = calculate_distance(float(user_location.split(',')[0]), float(user_location.split(',')[1]), lat, lon)
    if distance <= 1:
        vehicle_label = vehicle.get('vehicleLabel')
        if not vehicle_label:
            continue
        popup_text = f"ID транспорта: {vehicle_label}<br>Широта: {lat}<br>Долгота: {lon}"
        folium.Marker(location=[lat, lon], popup=popup_text).add_to(mymap)

if university_location:
    university_lat, university_lon = [float(x) for x in university_location.split(',')]
    folium.Marker(location=[university_lat, university_lon], popup="СПбГЭТУ").add_to(mymap)

try:
    mymap.save("vehicles_map.html")
    print("Карта сохранена в vehicles_map.html")
except Exception as e:
    print("Ошибка при сохранении карты:", e)