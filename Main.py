from geopy.geocoders import Nominatim
import requests

Api = "https://api.weather.gov/"

def Time(time):
    hour = int(time[11])*10+int(time[12])
    if (hour == 0):
        return "12 AM"
    if (hour < 12):
        return str(hour)+" AM"
    return str(hour-12)+" PM"

def main():
    global data
    geolocator = Nominatim(user_agent="Forecast")
    location = geolocator.geocode(input("Enter address: "))
    f = requests.get(Api + "points/" + str(location.latitude) + "," + str(location.longitude))
    if f.status_code == 200:
        data=f.json()
    else:
        print(str(f.status_code)+ ": ")
        print("Something went wrong!\n")
        main()
    x = data["properties"]["gridX"]
    y = data["properties"]["gridY"]
    cwa = data["properties"]["cwa"]
    headers = {"X-Correlation-Id":"vilsonzheng@gmail.com", "X-Request-Id":"vilsonzheng@gmail.com", "X-Server-Id":"vilsonzheng@gmail.com"}
    forecast = input("1 - 12 Hour forecasts\n2 - Hourly forecasts\n")
    match forecast:
        case "1":
            forecast = requests.get(Api+"gridpoints/"+cwa+"/"+str(x)+","+str(y)+"/forecast",headers=headers).json()
            p = forecast["properties"]["periods"]
            for i in p:
                print(i["name"] + " - " + str(i["temperature"]) + "F, "+i["shortForecast"]+"\n")
        case "2":
            forecast = requests.get(Api+"gridpoints/"+cwa+"/"+str(x)+","+str(y)+"/forecast/hourly",headers=headers).json()
            p = forecast["properties"]["periods"]
            for i in p:
                print(Time(i["startTime"]) + " - " + str(i["temperature"]) + "F, "+i["shortForecast"]+"\n")
        case _:
            print("Invalid input")


main()
