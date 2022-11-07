from datetime import datetime

class UserQuote():
    def __init__(self, id, username, quote):
        self.id = id
        self.username = username
        self.quote = quote
        self.likes = 0
        self.time = datetime.now().timestamp()

    def like(self):
        self.likes += 1

    def to_json(self):
        return {
            "id": self.id, 
            "username": self.username,
            "quote": self.quote,
            "likes": self.likes        
        }
