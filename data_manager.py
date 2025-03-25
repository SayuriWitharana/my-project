import requests

endpoint = "https://api.sheety.co/4ccec6292ffed6f7db7c5f54a7971b1e/flightSearch/prices"

class DataManager:
    def __init__(self):
        self.data = {}

    def get_data(self):
        response = requests.get(url=endpoint)
        response = response.json()
        self.data = response['prices']
        return self.data

    def update_code(self):
        for city in self.data:
            new_data = {
                "price": {
                    "iataCode": city['iataCode']
                }
            }

            requests.put(url = f"{endpoint}/{city['id']}", json = new_data)

    def update_price(self, lower_price, id):
        new_price = {
            "price": {
                "lowestPrice": lower_price
            }
        }
        requests.put(url=f"{endpoint}/{id}", json=new_price)





