from UserQuote import UserQuote
from datetime import datetime
from profanity_filter import ProfanityFilter
import random

pf = ProfanityFilter()

quote_list = []

def submit_quote(username, quote):
    if pf.is_profane(quote):
        return False
    id = len(quote_list) 
    quote_object = UserQuote(id, username, quote)
    quote_list.append(quote_object)
    return True

def get_leaderboard():
    sorted_list = sorted(quote_list, key=lambda x: x.likes, reverse=True)
    leaderboard = [quote_object for ind, quote_object in enumerate(sorted_list) if ind<10]
    leaderboard_json = [quote_object.to_json() for quote_object in leaderboard]
    return leaderboard_json

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
    return random.choices(quote_list, weights=weights, k=1)[0]