import requests

tequila_endpoint = "https://tequila-api.kiwi.com"
api_key = "2Wyg72cT5sE0FbJ708ZtHq8S0b-iQLFS"

class FlightSearch:
    def destination_code(self, city):
        headers = {
            "apikey": api_key
        }
        query = {
            "term": city,
            "location_type": "city"
        }
        code = requests.get(url = f"{tequila_endpoint}/locations/query", headers=headers, params=query)
        response = code.json()['locations'][0]['code']
        return response

