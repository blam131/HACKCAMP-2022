class UserQuote():
    def __init__(self, id, username, quote):
        self.id = id
        self.username = username
        self.quote = quote
        self.likes = 0

    def like(self, id):
        if self.id == id:
            self.likes += 1

    def filter(self):
       pass

    # test
    def results(self):
        print(self.id)
        print(self.username)
        print(self.quote)
        print(self.likes)

test = UserQuote(1, "bob", "What is love")
test.results()