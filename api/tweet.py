from flask import Flask, jsonify
from main import post_tweet

app = Flask(__name__)

@app.route("/api/tweet", methods=["GET"])
def tweet():
    """Endpoint to trigger a tweet"""
    response = post_tweet()
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
    