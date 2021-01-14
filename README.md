# Goal
# Structure
# ERD
This is the basic ERD Diagramm that describes the relationship of the underlying tables:
![ERD-Diagramm](/docs/erd.png)
# Endpoints
Here is the list of all possible endpoints:

/api/v1/restaurants/
    POST - Create new restaurant
    GET - List of all restaurants
/api/v1/restaurants/{ID}
    GET - Get detailed Infos of that restaurant
    PATCH - Update that restaurant
    DELETE - Delete that restaurant
/api/v1/restaurants/{ID}/tables
    GET - Show all tables of that restaurant
    POST - Create a new table
/api/v1/restaurants/{ID}/tables/{ID}
    DELETE - soft delete a table
/api/v1/restaurants/{ID}/tables/{ID}/visits
    GET - Show all visits for that table 
    POST - Create a new visit
/api/v1/guests/
    GET - Show all guests 
    POST - new guest
/api/v1/guests/{ID}  
    GET - Shows guest detail info
    PATCH - update user info (sick and sick_date)
    DELETE - Delete a user (no right assigned)
/api/v1/guests/{ID}/notifications
    GET - Shows a message if the guest was in a restaurant at the time when somebody sick was nearby

OPTIONAL
/api/v1/restaurants/{ID}/guests
    GET - Show all guests in the restaurant for specific time frame (Parameter Sick?)
/api/v1/restaurants/{ID}/visits
    GET - Show all visits of a restaurant for specific time frame

NOT SUPPORTED
api/v1/restaurants/{ID}/tables/{ID}/visits/{ID}
    DELETE - soft delete a visit (not supported by a role)

# Roles & Rights
# How to Startmat
