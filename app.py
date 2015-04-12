#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

parking_spots = [
    {
        'occupied': True
    }
]


@app.route('/api/v1.0/spots/<int:spot_id>', methods=['GET'])
def get_spots(spot_id):
    return jsonify(parking_spots[0])

if __name__ == "__main__":
    app.run(debug=True)
