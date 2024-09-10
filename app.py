from flask import Flask, jsonify
import requests

app = Flask(__name__)

SLEEPER_API_BASE = "https://api.sleeper.app/v1"

@app.route('/user/<username>')
def get_user(username):
    response = requests.get(f"{SLEEPER_API_BASE}/user/{username}")
    return jsonify(response.json())

@app.route('/user/<user_id>/leagues/<sport>/<season>')
def get_user_leagues(user_id, sport, season):
    response = requests.get(f"{SLEEPER_API_BASE}/user/{user_id}/leagues/{sport}/{season}")
    return jsonify(response.json())

# Add more routes for other Sleeper API endpoints

if __name__ == '__main__':
    app.run(debug=True)
