# API Specification

## Database

A correct implementation of the User model has been provided. Implement the following model with a many-to-one relationship with the User model.

### Transaction Model
Required Fields:
- ID (primary key)
- amount (float)
- sender id (foreign key)
- receiver id (foreign key)
- pending (boolean)

## Routes

The get all users route has been provided as an example. Please complete the following routes.

### Create user
``` POST /api/users/```
#### Request
```json
{
    "name": "Raahi Menon",
    "username": "raahi014",
    "balance": <USER INPUT (OPTIONAL INTEGER)>
}
```

#### Response
```json
<HTTP STATUS CODE 201>
{
    "id": <ID>
    "name": "Raahi Menon",
    "username": "raahi014",
    "balance": <USER INPUT, OR 0 IF NOT PROVIDED>,
    "transactions": []
}
```

### Get user by ID
``` GET /api/users/{id}/```

#### Response
```json
HTTP STATUS CODE 200>
{
    "id": <ID>,
    "name": <STORED NAME FOR USER WITH ID {id}>,
    "username": <STORED USERNAME FOR USER WITH ID {id}>,
    "balance": <STORED BALANCE FOR USER WITH ID {id}>,
    "transactions": [
        <TRANSACTION>,
        <TRANSACTION>,
        ...
    ]
}
```

