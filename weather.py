import datetime as dt
import requests

def get_weather(city_name):
    API_KEY = "f887d5ff61d0ed7cc4f14df9022c4838"
    BASE_URL = f"http://api.openweathermap.org/data/2.5/weather"
    
    # Construct the URL for the API request
    url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"
    
    try:
        # Send the API request and get the response
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()

        # Extract weather data
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        description = data['weather'][0]['description']
        sunrise_time = dt.datetime.utcfromtimestamp(data['sys']['sunrise'] + data['timezone'])
        sunset_time = dt.datetime.utcfromtimestamp(data['sys']['sunset'] + data['timezone'])

        # Display weather information
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Sunrise Time (UTC): {sunrise_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Sunset Time (UTC): {sunset_time.strftime('%Y-%m-%d %H:%M:%S')}")

    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to retrieve weather data. {e}")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
