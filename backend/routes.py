from flask import Flask, jsonify
import main

app = Flask(__name__)

@app.route('/like/<id>', methods = ['PUT'])
def like(id):
    main.like(id)
    
@app.route('/leaderboard', methods = ['GET'])
def get_leaderboard():
    leaderboard = main.get_leaderboard()
    return jsonify({
        "leaderboard": leaderboard
    })

@app.route('/submit/<username>/<quote>', methods = ['POST'])
def submit(username, quote):
    passed = main.submit_quote(username, quote)
    return jsonify({
        "passed": passed
    })

@app.route('/get', methods = ['GET'])
def get_user_quote():
    user_quote = main.get_user_quote()
    return jsonify({
        "id": user_quote.id,
        "quote": user_quote.username,
        "username": user_quote.quote
    })

if __name__ == "__main__":
    app.run(debug = True)