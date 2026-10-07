import requests

def get_weather(city_name):
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=no&format=json"
    geo_response = requests.get(geo_url)
    
    if geo_response.status_code != 200:
        return None
        
    geo_data = geo_response.json()
    

    if not geo_data.get("results"):
        return None
        
    location = geo_data["results"][0]
    lat = location["latitude"]
    lon = location["longitude"]
    found_name = location["name"]
    country = location.get("country", "")

    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    weather_response = requests.get(weather_url)
    
    if weather_response.status_code != 200:
        return None
        
    weather_data = weather_response.json()
    temp = weather_data["current_weather"]["temperature"]
    
    return found_name, country, temp



while True:
    city = input("\nSkriv inn en by (eller 'avbryt' for å avslutte): ").strip()
    
    if city.lower() == 'avbryt':
        print("Programmet avsluttes. Ha en fin dag!")
        break
        
    if not city:
        continue
        
    print(f"Henter vær for {city}...")
    
    result = get_weather(city)
    
    if result is None:
        print(f"Feil: Kunne ikke finne byen '{city}' eller hente værdata.")
    else:
        found_name, country, temp = result
        print(f"Været i {found_name} ({country}) i dag: {temp}°C")