from geopy.geocoders import Nominatim
import requests
Api = "https://api.weather.gov/"

def main():
    geolocator = Nominatim(user_agent="Forecast")
    location = geolocator.geocode(input("Enter location: "))
    print(location.latitude()+","+location.longitude())
    #print(requests.get(Api+"points/"+location.latitude()+","+location.longitude()).json())
main()