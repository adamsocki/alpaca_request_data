import requests
import json
import csv

# Define an empty list to hold the stock symbols
stock_symbols = []

# Open the file and read its contents
with open("stocks_nyse.txt", newline="") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header
    count = 0
    for row in reader:
        symbol = row[0]  # The symbol is in the first column
        count+=1
        # if count == 40:
        #     break
        if "$" not in symbol:  # Skip symbols with a dollar sign
            stock_symbols.append(symbol)



# Define the base URL
base_url = "https://data.alpaca.markets"

# Define your API key and secret key
api_key = "AK4R12KYSHYZ3YCR7224"
secret_key = "yRJG5FjBsXdpizB2MMYaK2Mkpa6NqpDmmgk3miTt"

# Define the headers for the request
headers = {
    "APCA-API-KEY-ID": api_key,
    "APCA-API-SECRET-KEY": secret_key,
    "accept": "application/json"
}

# Define the endpoint for the auctions data
endpoint = "/v2/stocks/trades/latest"

# Define the symbols you want data for
symbols = ",".join(stock_symbols)  # Convert the list of symbols to a comma-separated string

# Define the parameters for the request
params = {
    "symbols": symbols,
    "start": "2022-01-03T00:00:00Z",
    "end": "2022-01-04T00:00:00Z"
}

params1 = {
    "symbols": symbols

}

# Send a GET request to the API
response = requests.get(base_url + endpoint, headers=headers, params=params1)

# Print the status code (should be 200 for a successful request)
print("Status code:", response.status_code)

# Print the response data
data = response.json()

# Assuming 'data' is the response from the API
for ticker, trade_data in data['trades'].items():
    price = trade_data['p']
    print(f"Ticker: {ticker}, Price: {price}")

# print(json.dumps(data, indent=4))
