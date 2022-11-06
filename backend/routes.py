from flask import Flask, jsonify
import UserQuote

app = Flask(__name__)

@app.route('/like/<id>', methods = ['PUT'])
def like(id):
    UserQuote.like(id)
    
@app.route('/leaderboard', methods = ['GET'])
def get_leaderboard():
    leaderboard = UserQuote.get_leaderboard()
    return jsonify({
        "leaderboard": leaderboard
    })

@app.route('/submit/<quote>/<username>', methods = ['POST'])
def submit(quote, username):
    passed = UserQuote.submit_quote(quote, username)
    return jsonify({
        "passed": passed
    })

@app.route('/get', methods = ['GET'])
def get_user_quote():
    user_quote = UserQuote.get_user_quote()
    return jsonify({
        "id": user_quote.id,
        "quote": user_quote.quote,
        "username": user_quote.username
    })

if __name__ == "__main__":
    app.run(debug = True)