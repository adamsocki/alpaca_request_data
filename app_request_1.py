import requests
import tkinter as tk
import json
import csv
import logging

# Set up logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Data Fetcher")
    

        # Define your API key and secret key
        self.api_key = "AK4R12KYSHYZ3YCR7224"
        self.secret_key = "yRJG5FjBsXdpizB2MMYaK2Mkpa6NqpDmmgk3miTt"

        # Define the headers for the request
        self.headers = {
            "APCA-API-KEY-ID": self.api_key,
            "APCA-API-SECRET-KEY": self.secret_key,
            "accept": "application/json"
        }

        # Define the endpoint for the auctions data
        self.endpoint_auctions = "/v2/stocks/auctions"
        self.endpoint_ticker = "/v2/stocks/trades/latest"

        # Define the symbols you want data for
        self.symbols = self.get_symbols()

        # Define the parameters for the request
        self.params_auctions = {
            "symbols": self.symbols,
            "start": "2022-01-03T00:00:00Z",
            "end": "2022-01-04T00:00:00Z"
        }

        self.params_ticker = {
            "symbols": self.symbols
        }

        # Create buttons
        self.btn_auctions = tk.Button(self.root, text="Get Auctions Data", command=self.get_auctions_data)
        self.btn_auctions.grid(row=0, column=0, padx=10, pady=10)  # Using grid and added padding

        self.btn_other = tk.Button(self.root, text="Get Ticker Data", command=self.get_ticker)
        self.btn_other.grid(row=1, column=0, padx=10, pady=10)  # Using grid and added padding

    def get_symbols(self):
        try:
            stock_symbols = []
            with open("stocks_nyse.txt", newline="") as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip the header
                for row in reader:
                    symbol = row[0]  # The symbol is in the first column
                    if "$" not in symbol:  # Skip symbols with a dollar sign
                        stock_symbols.append(symbol)
            return ",".join(stock_symbols)
        except Exception as e:
            logging.error("Error in get_auctions_data: %s", e)
    
    def get_auctions_data(self):
        try:
            base_url = "https://data.alpaca.markets"
            response = requests.get(base_url + self.endpoint_auctions, headers=self.headers, params=self.params_auctions)
            print(response.json())  # You may want to do something different with the response
        except Exception as e:
            logging.error("Error in get_auctions_data: %s", e)

    def get_ticker(self):
        try:
            base_url = "https://data.alpaca.markets"
            response = requests.get(base_url + self.endpoint_ticker, headers=self.headers, params=self.params_ticker)
                 # Create a new window
            new_window = tk.Toplevel(self.root)
            new_window.title("Ticker Data")


    
        # Create a scrollbar
            scrollbar = tk.Scrollbar(new_window)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            

           # Create a Text widget and add some test text
            button = tk.Button(new_window, text="Export Data")
            button.pack()
            text = tk.Text(new_window)
            text.insert(tk.END, "Test text\n")
            
            data = response.json()

        # Display the data in the new window
            for ticker, trade_data in data['trades'].items():
                price = trade_data['p']
                #label = tk.Label(new_window, text=f"Ticker: {ticker}, Price: {price}")
                #label.pack()
                text.insert(tk.END, f"Ticker: {ticker}, Price: {price}\n")
               
            
            for ticker, trade_data in data['trades'].items():
                price = trade_data['p']
                print(f"Ticker: {ticker}, Price: {price}")


            text.config(state=tk.DISABLED)
            text.pack()

            #
            #
            #scrollbar.config(command=text.yview)

        except Exception as e:
            logging.error("Error in get_auctions_data: %s", e)



try:
    
    root = tk.Tk()
    root.geometry("500x500")
    app = App(root)
    root.mainloop()
except Exception as e:
    logging.error("Error: %s", e)