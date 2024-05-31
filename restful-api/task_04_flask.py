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
    return jsonify(list(users.values()))

# Define the /status endpoint
@app.route("/status")
def status():
    return "OK"

# Define the /users/<username> endpoint
@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return "User not found", 404

# Define the /add_user endpoint to handle POST requests
@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.json
    username = data["username"]
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
