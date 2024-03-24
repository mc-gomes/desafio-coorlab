from flask import Flask, jsonify
from flask_cors import CORS
from data import destinations

data = destinations["transport"]

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Hello from Flask!'

@app.route('/destinations', methods=['GET'])
def get_destinations():
    return jsonify(data)

@app.route('/destinations/<int:id>', methods=['GET'])
def get_destination_by_id(id: int):
    destination = get_destination(id)
    if destination is None:
        return jsonify({'error': 'Nenhum dado encontrado'}, 404)
    return jsonify(destination)

def get_destination(id):
    if 0 < id < len(data) and data[id]:
        return data[id-1]
    else:
        return None


if __name__ == "__main__":
    app.run(debug=True, port=3000)

