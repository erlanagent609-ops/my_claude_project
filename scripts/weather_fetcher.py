import sys
import urllib.request
import urllib.parse

def fetch_weather(city="Manado"):
    url = f"https://wttr.in/{urllib.parse.quote(city)}?format=3"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'curl'})
        with urllib.request.urlopen(req) as response:
            result = response.read().decode('utf-8').strip()
            print(result)
            return result
    except Exception as e:
        print(f"Error fetching weather for {city}: {e}")
        return None

if __name__ == "__main__":
    city_name = "Manado"
    if len(sys.argv) > 1:
        city_name = " ".join(sys.argv[1:])
    fetch_weather(city_name)
