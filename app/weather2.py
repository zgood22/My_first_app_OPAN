from pgeocode import Nominatim
import requests
import json
from IPython.display import display, Image

def fetch_data(zip_code, country_code="US"):
    nomi = Nominatim(country_code)
    geo = nomi.query_postal_code(zip_code)
    #The first two functions use the paramaters to create 'geo' variables whic can then extract longitude and latitude
    latitude = geo["latitude"]
    longitude = geo["longitude"]
    request_url = f"https://api.weather.gov/points/{latitude},{longitude}"
    #creates a request with long and lat
    print(request_url)
    response = requests.get(request_url)
    #print(response.status_code)
    parsed_response = json.loads(response.text)
    forecast_url = parsed_response["properties"]["forecast"]
    forecast_response = requests.get(forecast_url)
    #print(forecast_response.status_code)
    parsed_forecast_response = json.loads(forecast_response.text)
    return parsed_forecast_response, response.status_code
    #the return function is for testing


def display_weather(parsed_forecast_response):
     periods = parsed_forecast_response["properties"]["periods"]
     daytime_periods = [period for period in periods if period["isDaytime"] == True]
     degree_sign = "*"
     for period in daytime_periods:
        print("-------------")
        print(period["name"], period["startTime"][0:7])
        print(period["shortForecast"], f"{period['temperature']} {degree_sign}{period['temperatureUnit']}")
        print(period["detailedForecast"])
     return daytime_periods

    





if __name__ == "__main__":
    zipcode = input("Please enter a 5-digit zipcode: ")
    weather_data, empty_var = fetch_data(zipcode, country_code="US" )
    #empty var enables code to both work and create another "test" parameter
    display_weather(weather_data)
