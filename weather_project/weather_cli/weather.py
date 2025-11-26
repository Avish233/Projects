import requests
import os
from dotenv import load_dotenv

load_dotenv()

weather = requests.get(
    "http://api.openweathermap.org/data/2.5/weather?q=Mauritius,mu&appid=" + os.getenv("api_key")
)

print(weather.json())