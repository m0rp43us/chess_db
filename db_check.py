from pymongo import MongoClient

myclient = MongoClient("mongodb://localhost:27017/")
db = myclient["Chess_puzzles"]
Col = db["puzzles"]

print(len(list(Col.find({"eco":{'$exists': True}}))))
