class UserQuote():
    def __init__(self, id, username, quote):
        self.id = id
        self.username = username
        self.quote = quote
        self.likes = 0

    def like(self):
        self.likes += 1
