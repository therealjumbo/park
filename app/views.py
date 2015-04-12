from flask import jsonify
from app import app
from pyserial import read_from_db


@app.route('/api/v1.0/spots/<int:spot_id>', methods=['GET'])
def get_spots(spot_id):
    val = read_from_db()
    return jsonify({
        'occupied': val
    })
