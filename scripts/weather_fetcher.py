import sys
import urllib.request
import urllib.parse

def fetch_weather(city="Manado"):
    url = f"https://wttr.in/{urllib.parse.quote(city)}?format=3"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'curl'})
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8').strip())
    except Exception as e:
        print(f"Error fetching weather for {city}: {e}")

if __name__ == "__main__":
    city = sys.argv[1] if len(sys.argv) > 1 else "Manado"
    fetch_weather(city)
