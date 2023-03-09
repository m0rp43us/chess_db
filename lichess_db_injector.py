from pymongo import MongoClient
import requests
import json
import csv

myclient = MongoClient("mongodb://localhost:27017/")
db = myclient["Chess_puzzles"]
Col = db["puzzles"]

with open(r"C:\Users\Zbook\Documents\GitHub\lichess_scrapper\lichess_db_puzzle.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print({
        'id' : row[0],
        'rating' : row[3],
        'fen' : row[1],
        'solution' : row[2],
        'tags' : row[7].split(' ')
        })
        Col.insert_one({
        'id' : row[0],
        'rating' : int(row[3]),
        'fen' : row[1],
        'solution' : row[2],
        'tags' : row[7].split(' ')
        })

 


