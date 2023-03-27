import requests
import random


url = ["https://www.google.com/",
       "https://www.facebook.com/",
       "https://www.twitter.com/",
       "https://www.amazon.com/",
       "https://www.apple.com/"]

website = random.choice(url)
res = requests.get(random.choice(url))

print(f"Response status code: {res.status_code}")
print(f"Website: {website}")
print(f"HTML code length: {len(res.text)}")
print("-" * 37)


url2 = ("https://geocoding-api.open-meteo.com/v1/search?name=")
city_country = input("Please enter a city or country here: ")
res2 = requests.get(f"{url2}{city_country}")
data = res2.json()
if "results" in data:
       latitude = round(data["results"][0]["latitude"], 2)
       longitude = round(data["results"][0]["longitude"], 2)
       url_api = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&current_weather=true&past_days=1&forecast_days=1&timezone=auto")
       data_api = url_api.json()
       print(f"Temperature in {city_country} is {data_api['current_weather']['temperature']} degree celsius!")
else:
       print("Sorry, i cant find results for this input")


