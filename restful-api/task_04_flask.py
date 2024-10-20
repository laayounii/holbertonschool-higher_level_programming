#!/usr/bin/python3

from flask import Flask, jsonify, request

# Initialize Flask application
app = Flask(__name__)

# In-memory dictionary to store user data
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Root route
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# /status route to check API status
@app.route('/status')
def status():
    return "OK"

# Endpoint to return list of usernames
@app.route('/data')
def get_usernames():
    return jsonify(list(users.keys()))

# Endpoint to get specific user data
@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Endpoint to add a new user via POST request
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    # Check if username is provided
    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data['username']
    
    # Check if user already exists
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    # Add the new user to the dictionary
    users[username] = {
        "username": username,
        "name": data.get('name', ''),
        "age": data.get('age', 0),
        "city": data.get('city', '')
    }
    
    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
