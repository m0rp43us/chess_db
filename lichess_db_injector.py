from pymongo import MongoClient
import requests
import json
import csv
import time
import re


myclient = MongoClient("mongodb://localhost:27017/")
db = myclient["Chess_puzzles"]
Col = db["puzzles"]

def get_opening(row):
    try :
        game = requests.get('https://lichess.org/game/export/{}'.format(row[8].split('g/')[1][:8]))
        '''Col.insert_one({
        'id' : row[0],
        'rating' : int(row[3]),
        'eco' : 
        'fen' : row[1],
        'solution' : row[2],
        'tags' : row[7].split(' ')
         })'''
        myquery = { "id": row[0] }
        newvalues = { "$set": {'eco' : re.findall(r"[A-Z][0-9][0-9]", game.text)[0],"opening" : game.text.split('[Opening "')[1].split("\"]")[0].split(": ")} }
        Col.update_one(myquery, newvalues)
        print({
            'id' : row[0],
        'rating' : row[3],
        'fen' : row[1],
        'solution' : row[2],
        'tags' : row[7].split(' '),
        'eco' : re.findall(r"[A-Z][0-9][0-9]", game.text)[0],
        'opening' : game.text.split('[Opening "')[1].split("\"]")[0].split(": ")
        })
    except IndexError :
        pass


with open(r"C:\Users\Zbook\Documents\GitHub\lichess_scrapper\lichess_db_puzzle.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    start = 0
    for row in csv_reader:
        try :
            if start < 22868 :
                start+=1
                continue
            get_opening(row)
        except IndexError :
            time.sleep(10)
            get_opening(row)
            
            

 


