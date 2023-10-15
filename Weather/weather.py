import requests
import json

def get_weather(city_name):
  """Gets the weather data for a given city.

  Args:
    city_name: The name of the city.

  Returns:
    A dictionary containing the weather data for the city.
  """

  api_key = "4f7eb24d827e23b8037b6db1fafd4b15"
  base_url = "https://api.openweathermap.org/data/2.5/weather?"

  params = {
    "q": city_name,
    "appid": api_key
  }

  response = requests.get(base_url, params=params)
  weather_data = json.loads(response.content)

  return weather_data

def main():
  city_name = input("Type the name of the city you want to see the weather of: ")

  weather_data = get_weather(city_name)
  
  # Convert the temperature to Celsius
  celsius = weather_data["main"]["temp"] - 273.15


  # Convert the temperature to Celsius and round to one decimal place
  celsius = round(weather_data["main"]["temp"] - 273.15, 1)

  print("The weather in {} is:".format(city_name))
  print("Temperature:", celsius, "degrees Celsius")
  print("Wind speed:", weather_data["wind"]["speed"], "m/s")
  print("Wind direction:", weather_data["wind"]["deg"], "degrees")
  print("Precipitation forecast:", weather_data["weather"][0]["description"])

if __name__ == "__main__":
  main()
