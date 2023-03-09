from pymongo import MongoClient
import requests
import json

 
myclient = MongoClient("mongodb://localhost:27017/")
db = myclient["Chess_puzzles"]
Col = db["puzzles"]

url = "https://lichess.org/training/complete/mix/r2YIi"

payload={}
files=[

]
headers = {
  'Accept': 'application/vnd.lichess.v5+json',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'origin': 'https://lichess.org',
  'referer': 'https://lichess.org/training'
}

 # some_file.py
import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.append(r"C:\Users\Zbook\Documents\GitHub\lichess_scrapper\pgnToFen-master")

import pgntofen
pgnConverter = pgntofen.PgnToFen()

response = requests.request("POST", url, headers=headers, data=payload, files=files).json()
print({
        'id' : response['next']['puzzle']['id'],
        'rating' : int(response['next']['puzzle']['rating']),
        'fen' : pgnConverter.pgnToFen(response['next']['game']['pgn'].split(' ')).getFullFen(),
        'solution' : response['next']['puzzle']['solution'],
        'tags' : response['next']['puzzle']['themes']
    })