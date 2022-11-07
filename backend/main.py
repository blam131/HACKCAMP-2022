from UserQuote import UserQuote
from profanity_filter import ProfanityFilter

pf = ProfanityFilter()

quote_list = []

def submit_quote(username, quote):
    if pf.is_profane(quote):
        return (False)
    id = len(quote_list) + 1
    quote_object = UserQuote(id, username, quote)
    quote_list.append(quote_object)
    return (True)

def get_leaderboard():
    sorted_list = sorted(quote_list, key=lambda x: x.likes, reverse=True)
    leaderboard = [quote_object for ind, quote_object in enumerate(sorted_list) if ind<5]
    leaderboard_json = [quote_object.to_json() for quote_object in leaderboard]
    return(leaderboard_json)

def like(id):
    for quote_object in quote_list:
        if quote_object.id == id:
            quote_object.like()