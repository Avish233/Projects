import requests
import os
from dotenv import load_dotenv
#--------------------------------
# Load .env file
#--------------------------------
load_dotenv()


# Make a GET request to the OpenWeatherMap API
weather = requests.get(
    "http://api.openweathermap.org/data/2.5/weather?q=Mauritius,mu&appid=" + os.getenv("api_key")
)

# Print the JSON response
print(weather.json())