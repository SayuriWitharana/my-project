import requests
from datetime import datetime, timedelta

endpoint = "https://tequila-api.kiwi.com"
header = {
    "apikey": "2Wyg72cT5sE0FbJ708ZtHq8S0b-iQLFS"
}
tomorrow = (datetime.now() + timedelta(days = 1)).strftime("%d/%m/%Y")
six_months = (datetime.now() + timedelta(days = (6*30))).strftime("%d/%m/%Y")

class FlightData:
    def get_price(city_code, stop_overs = 0, ):
        params = {
            "fly_from": "LON",
            "fly_to": city_code,
            "date_from": tomorrow,
            "date_to": six_months,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        price = requests.get(url = f"{endpoint}/v2/search", params= params, headers = header)
        price = price.json()
        try:
            return round(price["data"][0]['price'])
        except IndexError:
            return None
        except TypeError:
            print(f"No Flights from {city_code}")

