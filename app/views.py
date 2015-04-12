from flask import jsonify
from datetime import datetime
from app import app


parking_spots = [
    {
        'occupied': True
    }
]

@app.route('/api/v1.0/spots/<int:spot_id>', methods=['GET'])
def get_spots(spot_id):
    return jsonify(parking_spots[0])
