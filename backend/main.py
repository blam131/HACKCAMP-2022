from UserQuote import UserQuote
from datetime import datetime
from profanity_filter import ProfanityFilter
import random

pf = ProfanityFilter()

q1 = UserQuote(1, "Joe", "The elevator to success is out of order. You'll have to use the stairs, one step at a time.")
q1.likes = 20
q2 = UserQuote(2, "Evan", "If you think you are too small to make a difference, try sleeping with a mosquito.")
q2.likes = 12
q3 = UserQuote(3, "Anonymous", "I used to think I was indecisive, but now I'm not so sure.")
q3.likes = 1
q4 = UserQuote(4, "Will", "The road to success is dotted with many tempting parking spaces.")
q4.likes = 10
q5 = UserQuote(5, "Robert", "Friendship is like peeing on yourself: everyone can see it,"
                            "but only you get the warm feeling that it brings.")
q5.likes = 23
q6 = UserQuote(6, "Anonymous", "amogus")

quote_list = [q1, q2, q3, q4, q5, q6]

def submit_quote(username, quote):
    if pf.is_profane(quote):
        return False
    if len(username) < 1:
        username = "Anonymous"
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
    
    choice = random.choices(quote_list, weights=weights, k=1)[0]
    choice.time = now
    return(choice)