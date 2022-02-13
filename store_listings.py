# This file saves newly found listings into json
import json

def store_listing(file, symbol):
    # Save new listing into the local json file
    with open(file, 'w') as f:
        json.dump(symbol, f, indent=4)

def load_listings(file):
    #Update info in json file
    with open(file, 'r+') as f:
        return json.load(f)
 
