from UserQuote import UserQuote
import random
from datetime import datetime

quote_list = []

def submit_quote(username, quote):
    id = len(quote_list)
    quote_object = UserQuote(id, username, quote)
    now = datetime.now()
    quote_list.append(quote_object)

def get_leaderboard():
    sorted_list = sorted(quote_list, key=lambda x: x.likes, reverse=True)
    leaderboard = [quote_object for ind, quote_object in enumerate(sorted_list) if ind<10]
    leaderboard_json = [quote_object.to_json() for quote_object in leaderboard]
    return(leaderboard_json)

def like(id):
    for quote_object in quote_list:
        if quote_object.id == id:
            quote_object.like()

def get_user_quote():
    now = datetime.now().timestamp()
    weights = []
    for quote_object in quote_list:
        change_in_time = now - quote_object.time
        weight = (quote_object.likes + 1) / (change_in_time + 1) * 100
        weights.append(weight)
    
    print(weights)
    return(random.choices(quote_list, weights=weights, k=1)[0])

submit_quote("Gordon", "gordon quote")
submit_quote("Bob1", "quote1")
submit_quote("Bob2", "quote2")
submit_quote("Bob3", "quote3")
submit_quote("Bob4", "quote4")

print(quote_list)
get_user_quote()