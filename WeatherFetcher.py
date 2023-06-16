# Weather Fetcher 
# https://home.openweathermap.org

import requests
import json

def get_weather(city):
    api_key = "864e6b748dc2088531a3ae80444472f6"  # OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Send a GET request to the OpenWeatherMap API
    response = requests.get(base_url, params={"q": city, "appid": api_key})
    data = response.json()

    # Check if the request was successful
    if response.status_code == 200:
        # Retrieve the relevant weather information
        weather_desc = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        

        # Convert temperature from Kelvin to Celsius
        temperature = round(temperature - 273.15, 2)
        
        # Display the weather information
        print(f"Weather in {city}:")
        print(f"Description: {weather_desc}")
        print(f"Temperature: {temperature}°C")
    else:
        print("Error retrieving weather information.")

# Loop until user ends
while True or input == "Q":
    city = input.lower(("Enter a city or press Q to quit: "))
    get_weather(city)

    # Validate the user input
    if city.strip() == "":
        print("Please enter a valid city name or zip code.")
    else:
        # Get and display the weather for the specified location
        get_weather(city)

