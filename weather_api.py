import requests


def get_weather(city):
    api_key = 'your_api_key_here'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        print(f"The weather in {city}is {weather} with a temperature of {temperature}°C.")
    else:
        print("Failed to fetch weather data.")


city_name = input("Enter city name: ")
get_weather(city_name)
