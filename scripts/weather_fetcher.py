import urllib.request
import json

def fetch_weather(latitude=52.52, longitude=13.41):
    """
    Fetches current weather data from the public Open-Meteo API.
    Default coordinates are for Berlin, Germany.
    """
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    
    try:
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                data = json.loads(response.read().decode('utf-8'))
                return data.get('current_weather')
            else:
                print(f"Failed to fetch data. HTTP Status code: {response.status}")
                return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    print("Fetching current weather...")
    weather = fetch_weather()
    if weather:
        print("\nCurrent Weather Data:")
        print(f"Temperature: {weather.get('temperature')}°C")
        print(f"Wind Speed: {weather.get('windspeed')} km/h")
        print(f"Wind Direction: {weather.get('winddirection')}°")
        print(f"Time: {weather.get('time')}")
    else:
        print("Could not retrieve weather data.")
