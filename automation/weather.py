import requests

API_KEY = "9dddd65fcfb033dd59be135f005d9ac8"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]["description"]
    print("The weather is :", weather)
    temperature = round(data["main"]["temp"] - 273.15, 2)
    print("The temperature is: ",temperature, "celsius")
else:
    print("Internal server error")