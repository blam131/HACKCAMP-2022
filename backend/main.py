from UserQuote import UserQuote
from flask import Flask, jsonify

quote_list = []

def submit_quote(username, quote):
    id = len(quote_list) + 1
    quote_object = UserQuote(id, username, quote)
    quote_list.append(quote_object)

def get_leaderboard():
    sorted_list = sorted(quote_list, key=lambda x: x.likes, reverse=True)
    leaderboard = [quote_object for ind, quote_object in enumerate(sorted_list) if ind<5]
    leaderboard_json = [quote_object.to_json() for quote_object in leaderboard]
    return(leaderboard_json)

def like(id):
    for quote_object in quote_list:
        if quote_object.id == id:
            quote_object.like()