from data_manager import DataManager
from flight_data import FlightData

dm = DataManager()
sheet_data = dm.get_data()
if "iataCode" not in sheet_data[0].keys() or sheet_data[0]['iataCode'] == "":
    from flight_search import FlightSearch
    fs = FlightSearch()
    for row in sheet_data:
        row['iataCode'] = fs.destination_code(row['city'])

    dm.data = sheet_data
    dm.update_code()

for row in sheet_data:
    iata = row['iataCode']
    new_price = FlightData.get_price(iata)
    try:
        if new_price < int(row['lowestPrice']):
            row['lowestPrice'] = new_price
            dm.update_price(new_price, row['id'])
            print(f"Low price alert! Only £{new_price} to fly from London-STN to {row['city']}-{row['iataCode']}.")
    except TypeError:
        print(f"No flights from {iata}")
