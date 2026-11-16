LOCATIONS = {
    "jakarta": {"latitude": -6.2088, "longitude": 106.8456},
    "manado": {"latitude": 1.4748, "longitude": 124.8421},
    "kalasey dua": {"latitude": 1.4500, "longitude": 124.8000},
    "kalasey": {"latitude": 1.4500, "longitude": 124.8000},
    "kepulauan talaud": {"latitude": 3.9515, "longitude": 126.8286},
    "talaud": {"latitude": 3.9515, "longitude": 126.8286},
    "miangas": {"latitude": 5.5564, "longitude": 125.2289},
    "berlin": {"latitude": 52.52, "longitude": 13.41},
    "tokyo": {"latitude": 35.6762, "longitude": 139.6503},
    "london": {"latitude": 51.5074, "longitude": -0.1278},
}

def get_coordinates(city_name):
    key = city_name.strip().lower()
    return LOCATIONS.get(key)
