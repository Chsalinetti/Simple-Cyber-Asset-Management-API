# Simple-Cyber-Asset-Management-API

Setting up the application:
```bash

pip install flask
pip install sqlite3
```
Run create_database.py

Running the application:
```bash
flask --app basic_api run
```

Endpoints:

GET /assets:            Returns a list of all cyber assets in the database

POST /assets:           Adds a new cyber asset to the database
                        Accepts cyber asset data in JSON format:
                        (device name, type, serial number, operating system)

GET /assets/{id}:       Returns details of a specific cyber asset by ID

DELETE /assets/{id}:    Deletes a specific cyber asset by ID