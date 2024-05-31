#!/usr/bin/python3
from flask import Flask, jsonify, request

# Create a Flask app
app = Flask(__name__)

# Dictionary to store user data
users = {}

# Define the root endpoint
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# Define the /data endpoint
@app.route("/data")
def data():
    return jsonify(list(users.keys()))

# Define the /status endpoint
@app.route("/status")
def status():
    return "OK"

# Define the /users/<username> endpoint
@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    new_user = request.json
    username = new_user.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username == users:
        return jsonify({"error": "User already exists"}), 400
    users[username] = new_user
    return jsonify({"message": "User added", "user": new_user}), 201

if __name__ == "__main__":
    app.run()
