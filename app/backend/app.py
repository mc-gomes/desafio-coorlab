from flask import Flask, jsonify
from flask_cors import CORS
from data import destinations

data = destinations["transport"]

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Hello from Flask!'

app.run(port=3000)

