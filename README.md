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
                        Filtering can be done with the query parameter 'type'
                        Pagination cam ne done with the query parameters 'page' and 'limit'

POST /assets:           Adds a new cyber asset to the database
                        Accepts cyber asset data in JSON format:
                        (device name, type, serial number, operating system)

GET /assets/{id}:       Returns details of a specific cyber asset by ID

PUT /assets/{id}:       Updates a specific cyber asset’s information by ID

DELETE /assets/{id}:    Deletes a specific cyber asset by ID

