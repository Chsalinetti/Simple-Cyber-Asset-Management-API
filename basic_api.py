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

# Returns a list of all cyber assets in the database.
@app.route('/assets', methods=['GET'])
def get_assets():
    db = get_db()
    cursor = db.execute('SELECT * FROM assets')
    assets = cursor.fetchall()
    db.close()
    return jsonify([dict(asset) for asset in assets])

# Adds a new cyber asset to the database.
# acceps cyber asset data in JSON format (e.g., device name, type, serial number,
# operating system)
@app.route('/assets', methods=['POST'])
def add_asset():
    new_asset = request.json
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
        return 'Asset not found', 404

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
