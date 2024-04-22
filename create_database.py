import sqlite3

def create_database():
    db = sqlite3.connect('assets.db')
    cursor = db.cursor()
    
    # Create assets table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS assets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            serial_number TEXT NOT NULL,
            operating_system TEXT NOT NULL
        )
    ''')
    
    db.commit()
    db.close()

if __name__ == '__main__':
    create_database()
