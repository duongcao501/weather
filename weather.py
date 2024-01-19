# ===========
# mymodule.py 
# ===========
from urllib.request import urlopen
import json
import sys
#https://api.openweathermap.org/data/2.5/weather?q=OSLO&appid=499cd8cd149e4e4f03c2e67850670f4b
def get_weather(city):
    sock = urlopen("https://api.openweathermap.org/data/2.5/weather?q=" + 
                   city + "&appid=499cd8cd149e4e4f03c2e67850670f4b")
    result = sock.read()
    sock.close()
    weather = json.loads(result)
    return weather["main"]["temp"] - 273.15

def postal_lookup(postal_code):
    sock = urlopen("http://api.postcodes.io/postcodes/"+postal_code)
    result = sock.read()
    sock.close()
    details = json.loads(result)
    return (details["result"]["latitude"], details["result"]["longitude"])

if __name__ == "__main__":
    if len(sys.argv) > 1:
        city=sys.argv[1]
    else:
        city="OSLO"
    degrees = get_weather(city)
    print(f"Weather in {city} in {degrees:.2f} degree celcius.")
    postal = "B323PP"
    location = postal_lookup(postal)
    print(f"Postal code {postal} is at location {location}")
