from flask import Flask, request, jsonify
import sqlite3
import requests
import os
import logging

# Initialize the Flask app
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('anki.db')
    conn.row_factory = sqlite3.Row  
    return conn

# Function to retrieve user information from the database
def get_user_info(username):
    conn = get_db_connection()
    user = conn.execute(
        'SELECT ankiconnect_url, personal_deck_name FROM users_config WHERE username = ?',
        (username,)
    ).fetchone()
    conn.close()
    if user:
        return user['ankiconnect_url'], user['personal_deck_name']
    else:
        raise ValueError(f"User with username '{username}' not found!")

@app.route('/user_configuration', methods=['POST'])
def get_user_configuration():
    data = request.json  # Extract the JSON data from the request
    username = data.get('username')  # Extract username from the request

    if not username:
        return jsonify({"status": "error", "message": "Username is required!"}), 400

    try:
        anki_connect_url, deck_name = get_user_info(username)
        return jsonify({
            "status": "success",
            "anki_connect_url": anki_connect_url,
            "deck_name": deck_name
        })
    except ValueError as ve:
        return jsonify({"status": "error", "message": str(ve)}), 400

@app.route('/add_card', methods=['POST'])
def add_card():
    data = request.json  # Extract the JSON data from the request

    # Validate required fields
    required_fields = ['anki_connect_url', 'deck_name', 'word', 'meaning', 'examples', 'language_tag']
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({"status": "error", "message": f"Missing fields: {', '.join(missing_fields)}"}), 400

    try:
        # Build payload
        payload = {
            "action": "addNote",
            "version": 6,
            "params": {
                "note": {
                    "deckName": data['deck_name'],
                    "modelName": "Basic",
                    "fields": {
                        "Front": data['word'],
                        "Back": f"{data['meaning']}<br><ul>{''.join([f'<li>{ex}</li>' for ex in data['examples']])}</ul>",
                    },
                    "tags": [data['language_tag']]
                }
            }
        }

        # Send the request to the user's AnkiConnect URL
        response = requests.post(data['anki_connect_url'], json=payload)
        response_data = response.json()

        # Log the response for debugging
        logging.info(f"AnkiConnect response: {response_data}")

        if response_data.get("error"):
            return jsonify({"status": "error", "message": response_data["error"]}), 400

        return jsonify({"status": "success", "card_id": response_data.get("result")})
    except requests.exceptions.RequestException as e:
        logging.error(f"Request error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use the PORT environment variable
    app.run(host="127.0.0.1", port=port)