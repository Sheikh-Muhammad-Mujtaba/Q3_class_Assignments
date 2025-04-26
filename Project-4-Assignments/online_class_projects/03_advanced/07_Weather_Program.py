import requests as req
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()
API_Key = os.environ['WEATHER_API']

city = input("Enter a city: ")

base_url = f"http://api.openweathermap.org/data/2.5/weather?appid={API_Key}&q={city}"

weather_data = req.get(base_url).json()

pprint(weather_data)