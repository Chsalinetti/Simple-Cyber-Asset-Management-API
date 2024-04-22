from flask import Flask, request, jsonify
app = Flask(__name__)
import sqlite3

app = Flask(__name__)
DATABASE = 'assets.db'

# Create a connection to the SQLite database
def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

# Error handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not Found'}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad Request'}), 400

# Returns a list of all cyber assets in the database, with optional filtering by asset type and pagination.
@app.route('/assets', methods=['GET'])
def get_assets():
    #check arguments
    asset_type = request.args.get('type')
    page = request.args.get('page', default=1, type=int)
    limit = request.args.get('limit', default=10, type=int)
    offset = (page - 1) * limit

    db = get_db()
    # if filtering by asset type
    if asset_type:
        cursor = db.execute('SELECT * FROM assets WHERE type = ? LIMIT ? OFFSET ?', (asset_type, limit, offset))
    # not filtering by asset type
    else:
        cursor = db.execute('SELECT * FROM assets LIMIT ? OFFSET ?', (limit, offset))
        
    assets = cursor.fetchall()
    db.close()
    return jsonify([dict(asset) for asset in assets])

# Adds a new cyber asset to the database.
# acceps cyber asset data in JSON format (e.g., device name, type, serial number,
# operating system)
@app.route('/assets', methods=['POST'])
def add_asset():
    new_asset = request.json
    #basic error handling
    if not new_asset:
        return jsonify({'error': 'Asset Data Not Provided, or Invalid'}), 400
    db = get_db()
    db.execute('INSERT INTO assets (name, type, serial_number, operating_system) VALUES (?, ?, ?, ?)',
               (new_asset['name'], new_asset['type'], new_asset['serial_number'], new_asset['operating_system']))
    db.commit()
    db.close()
    return 'Asset added successfully', 201

# Returns details of a specific cyber asset by ID.
@app.route('/assets/<int:id>', methods=['GET'])
def get_asset(id):
    db = get_db()
    cursor = db.execute('SELECT * FROM assets WHERE id = ?', (id,))
    asset = cursor.fetchone()
    db.close()
    if asset:
        return jsonify(dict(asset))
    else:
        return jsonify({'error': 'Asset not found'}), 404
    
# Updates a specific cyber asset’s information by ID
@app.route('/assets/<int:id>', methods=['PUT'])
def update_asset(id):
    data = request.json
    if not data:
        return jsonify({'error': 'Asset Data Not Provided, or Invalid'}), 400
    db = get_db()
    db.execute('UPDATE assets SET name=?, type=?, serial_number=?, operating_system=? WHERE id=?',
               (data.get('name'), data.get('type'), data.get('serial_number'), data.get('operating_system'), id))
    db.commit()
    db.close()
    return 'Asset updated successfully', 200

# Deletes a specific cyber asset by ID
@app.route('/assets/<int:id>', methods=['DELETE'])
def delete_asset(id):
    db = get_db()
    db.execute('DELETE FROM assets WHERE id = ?', (id,))
    db.commit()
    db.close()
    return 'Asset deleted successfully', 200

if __name__ == '__main__':
    app.run(debug=True)
