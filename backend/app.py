from flask import Flask, jsonify
import random

app = Flask(__name__)

QUOTES = [
    "Stay hungry, stay foolish.",
    "Talk is cheap. Show me the code.",
    "Code never lies, comments sometimes do.",
    "Fix the cause, not the symptom."
]

@app.route('/quote')
def quote():
    return jsonify(quote=random.choice(QUOTES))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)