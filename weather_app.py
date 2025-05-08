import requests

def get_weather_data(city_name, api_key):
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = base_url + 'q=' + city_name + '&appid=' + api_key + '&units=metric'
    
    response = requests.get(complete_url)
    return response.json()
def show_weather_data(city_name, api_key):
    data = get_weather_data(city_name, api_key)
    
    if data["cod"] != "404":
        main = data["main"]
        wind = data["wind"]
        weather = data["weather"][0]
        
        city_name = data["name"]
        temperature = main["temp"]
        description = weather["description"]
        humidity = main["humidity"]
        wind_speed = wind["speed"]
        
        print(f"City: {city_name}")
        print(f"Temperature: {temperature}°C")
        print(f"Weather: {description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("City not found!")