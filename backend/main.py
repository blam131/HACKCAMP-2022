from UserQuote import UserQuote
from flask import jsonify
import json

quote_list = []

def submit_quote(username, quote):
    id = len(quote_list) + 1
    quote_object = UserQuote(id, username, quote)
    quote_list.append(quote_object)

def get_leaderboard():
    sorted_list = sorted(quote_list, key=lambda x: x.likes, reverse=True)
    leaderboard = [quote_object for ind, quote_object in enumerate(sorted_list) if ind<5]
    
    leaderboard_json = ["quotes"]
    for quote_object in leaderboard:
        dict = {}
        dict["username"] = quote_object.username
        dict["quote"] = quote_object.quote
        dict["likes"] = quote_object.likes
        leaderboard_json.append(dict)
    return(json.dumps(leaderboard_json))

def like(id):
    for quote_object in quote_list:
        if quote_object.id == id:
            quote_object.like()

submit_quote("bob", "hi")
submit_quote("bob", "hi")
submit_quote("bob", "hi")
submit_quote("bob", "hi")
submit_quote("bob", "hi")
submit_quote("bob", "hi")
submit_quote("bob", "hi")

print(get_leaderboard())