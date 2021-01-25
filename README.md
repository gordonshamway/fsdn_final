# Motivation for the project
The Corona-lockdowns around the world are pretty bad. With this project I want to do my part in partly reopen the society. With the help of this api, restaurants could open again, because it would be easy for a smartphone
app and it´s user to receive notifications whenever they have been in contact with other sick people at the time when they visited a specific restaurant.
This requires that a user is honest and updates it´s own status of sickness and the date he became sick.
You can find the app here [Corona_API_on_Heroku](https://corona-fsnd.herokuapp.com)
# Tech Stack
1. Python3
2. Flask for local developement and framework
3. SQL-Alchemy as ORM mapper
4. Postgres as database
5. Auth0 to generate JWT tokens
6. gunicorn as productive webserver
7. Heroku for hosting

# Dependencies
- See under "How to start"
- Auth0 to generate the JWT Token

# Entity-Relationship-Diagram
This is the basic ERD Diagramm that describes the relationship of the underlying tables:

![ERD-Diagramm](/docs/erd.png)


# Endpoints
For all endpoints you have to send the Authorization Bearer with the token.
For most of the endpoints also 'Content-type': 'application/json' is necessary. 
Here is the list of all possible endpoints:

## Restaurants
1. /api/v1/restaurants/
    - POST - Create new restaurant 
      - expects such a json as input with the following keys (name, country, city, postcode, street, owner, email)
      - if one of the above fields is NULL it returns an error
      - otherwhise it returns a success and the restaurant details with the id and timestamps
    - GET - List of all restaurants
2. /api/v1/restaurants/{ID}
    where id is the restaurant_id 
   - GET - Get detailed Infos of that restaurant
   - PATCH - Update that restaurant
   - DELETE - Delete that restaurant

## Tables
Since the number of tables is inside the restaurant details, there is no need to list the tables.
Creation can be done from restaurant_owner, deletion only by admin.
Also a Patch is not necessary, because a table doesnt have attributes which should be updated.
3. /api/v1/restaurants/{ID}/tables
   - POST - Create a new table
4. /api/v1/restaurants/{ID}/tables/{ID}
   - DELETE - soft delete a table

## Visits
A visit can not be deleted, since it is a fact. if it was a mistake, just close it. (so very small duration is the result)
5. /api/v1/restaurants/{ID}/visits
   - GET - Show all visits for that restaurant 
   - POST - Create a new visit
6. /api/v1/restauants/{ID}/visits/{visit_ID}
   - PATCH 

## Guests
Guest deletion is not programmed because it should not delete, old facts would be orphanized
7. /api/v1/guests/
   - GET - Show number of all guests 
   - POST - new guest
8. /api/v1/guests/{ID}  
   - GET - Shows guest detail info
   - PATCH - update user info (sick and sick_date)

## Special
9.  /api/v1/guests/{ID}/notifications
   - GET - Shows a message if the guest was in a restaurant at the time when somebody sick was nearby



# Roles & Rights
Here is an overview about the given Roles and the rights therein.
For testing the admin role is used.
![Roles_and_Rights](/docs/roles_and_rights.PNG)


# How to start
1. Install the requirements with:
```bash
pip install -r requirements.txt
```
2. start the app locally:
```bash
cd src/api
FLASK_APP=api.py flask run
```
3. If the tokens are not valid anymore generate new ones under this [Token-Generator](https://sbu47533.eu.auth0.com/authorize?audience=http://localhost:5000&response_type=token&client_id=HljTzT3THfu0P378ejF06XH0jRycrBEc&redirect_uri=https://corona-fsnd.herokuapp.com)
And look in the result under token.
To get the valid user login data look at "Users"
4. If you want to run the tests go to the api folder and run:
```bash
python tests.py
```
If the tests doesn´t work it is probably because the token is not valid anymore. Look under 3 to generate a token, replace it in tests.py and try again.

# Users
Email:      admin@corona.com
Password:   AdminCorona1
Role:       admin
Access-Token:   eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikx1OUhVcTJVWjdaRkdkdkNKenZ1diJ9.eyJpc3MiOiJodHRwczovL3NidTQ3NTMzLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDBkNGRiNzhlNWY1MzAwNmE4MjQ1Y2YiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjUwMDAiLCJpYXQiOjE2MTE1OTk0MzksImV4cCI6MTYxMTYwNjYzOSwiYXpwIjoiSGxqVHpUM1RIZnUwUDM3OGVqRjA2WEgwalJ5Y3JCRWMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpyZXN0YXVyYW50IiwiZGVsZXRlOnJlc3RhdXJhbnQtdGFibGUiLCJnZXQ6Z3Vlc3QtZGV0YWlscyIsImdldDpndWVzdC1ub3RpZmljYXRpb25zIiwiZ2V0Omd1ZXN0cyIsImdldDpyZXN0YXVyYW50IiwiZ2V0OnJlc3RhdXJhbnQtZGV0YWlscyIsImdldDpyZXN0YXVyYW50LXZpc2l0cyIsInBhdGNoOmd1ZXN0LWRldGFpbHMiLCJwYXRjaDpyZXN0YXVyYW50LWRldGFpbHMiLCJwYXRjaDpyZXN0YXVyYW50LXZpc2l0cyIsInBvc3Q6Z3Vlc3QiLCJwb3N0OnJlc3RhdXJhbnQiLCJwb3N0OnJlc3RhdXJhbnQtdGFibGUiLCJwb3N0OnJlc3RhdXJhbnQtdmlzaXRzIl19.sUJbxpPFm0tQV5z5-Kc9gicFxXwU5AYkKtE6VZdFpL8r5Ftqu1wGVh_tX0xNc8AqQOQGMS5CwGpQuEXO7_ptPt1xKzubydR8PXRtN2tTeBIeAvz-PH_vofy_2DMli84tBGdLOYNfOVmuefAHlo2sgVQy9qmobRrKHYpBMLV16Eppd0mM4ri34jKUAi6L7PZkz-7oN9r-SghpFOp0qeyv3Sa0dv-Gmi3W47MlLqveDcVx-pnLUI6890ZXgdFenyQRif8ECrtuuBhL3NhPFfsL2n1kI00jpLZg3C1UtNjnDzJS75DMmuhBFS7MOChJGaRiyPhAh_5F7m_wgeVw-hku0Q


Email:      restaurant@corona.com
Password:   RestaurantCorona1
Role:       restaurant_manager
Access-Token: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikx1OUhVcTJVWjdaRkdkdkNKenZ1diJ9.eyJpc3MiOiJodHRwczovL3NidTQ3NTMzLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDBkNGUzZDAzMGI4ZjAwNmE1MTQzODIiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjUwMDAiLCJpYXQiOjE2MTE1OTk2MDUsImV4cCI6MTYxMTYwNjgwNSwiYXpwIjoiSGxqVHpUM1RIZnUwUDM3OGVqRjA2WEgwalJ5Y3JCRWMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpyZXN0YXVyYW50IiwiZ2V0OnJlc3RhdXJhbnQtZGV0YWlscyIsImdldDpyZXN0YXVyYW50LXZpc2l0cyIsInBhdGNoOnJlc3RhdXJhbnQtZGV0YWlscyIsInBvc3Q6cmVzdGF1cmFudCIsInBvc3Q6cmVzdGF1cmFudC10YWJsZSJdfQ.OlSvq3GVHNaab6gWDl_CNfb7p-UCwdqr5Ut4mM-ZX5sU1Yt0WrWiXDLgd6fMYOSlEtsDlybmg-M-XS-B9BVbrK1yrW8FESysFM9_Zq-Q386GzBsPUWCqVG7QGoruHa4kvkJhMeytbRLQrk3lV_F1ngkyjZ1CvbgD0Z2GokKnUlpT3GhD4j1oO2rwUoFYQ9lpvZngJe_dsMLVrMxxDS8jMhYJiapKL4B-57Ddojb6oT58AE_IRe3KGruSd8GFS309HMV7w_eB7g-7PYUVA0xNjbMC4lSy0MOFoBS3GjGfBjdQkNe5ew9YcFi_gqoS9WpDgqmxC8KMuKyaYF8KnwN4fw

Email:      guest@corona.com
Password:   GuestCorona1
Role:       guest
Access-Token: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikx1OUhVcTJVWjdaRkdkdkNKenZ1diJ9.eyJpc3MiOiJodHRwczovL3NidTQ3NTMzLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDBkNGU1ZDhlNWY1MzAwNmE4MjQ2MDEiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjUwMDAiLCJpYXQiOjE2MTE1OTk2NTAsImV4cCI6MTYxMTYwNjg1MCwiYXpwIjoiSGxqVHpUM1RIZnUwUDM3OGVqRjA2WEgwalJ5Y3JCRWMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpndWVzdC1kZXRhaWxzIiwiZ2V0Omd1ZXN0LW5vdGlmaWNhdGlvbnMiLCJnZXQ6cmVzdGF1cmFudCIsInBhdGNoOmd1ZXN0LWRldGFpbHMiLCJwYXRjaDpyZXN0YXVyYW50LXZpc2l0cyIsInBvc3Q6Z3Vlc3QiLCJwb3N0OnJlc3RhdXJhbnQtdmlzaXRzIl19.dl7YTAP6jxr5PTOeVrlOzuDDhne87HcpJhYimxeCo6g12XFJ8qxiQJc-JuDlyUMJol5WftGTFkQJ6syd8PNZ8yD9Zg-Nct_PgaNBKBEz-UPvvr5wRWYNdfFc1qRoen6mFSCwq1vXrL7azq0adaitLABzBQYfnruG2aX_p222QUU1ZnipgmpmDu4dtwiZypqAtheWRtH1icvGiFQ6Eg7WXe4KjQrOvSQ_1MQAnU61YniLUT6juv2dn0sGa2fDTeiQwHJa2Avjw8lpr_7-x7mnO5xtM3QAQRrx9kZFj0aZ7MUWeFSEX6LNKV0ZwfY5yviyg3AkrY8DJiB4TDenQBrh8Q

# Testing
One word for the testing. I did not include 2 tests to every endpoint because I can´t fail an endpoint which just lists data. (technically I could when using an invalid bearer token, but it just makes no sense)

# Miscellaneous
## Documents that helped me when I was in need
https://github.com/jungleBadger/udacity_coffee_shop/blob/master/troubleshooting/generate_token.md
https://knowledge.udacity.com/questions/423462
https://stackoverflow.com/questions/34478320/how-to-set-gunicorn-to-find-a-flask-application/34478356

## .gitignore
- local python environment
- pycaches
---

# Notes for myself:

### Run migrations for my folder-structure
```bash
heroku run FLASK_APP=src/api/api.py flask db upgrade --directory src/api/migrations
```
### Heroku specific infos
- added wsgi.py with it´s content to get gunicorn and procfile call the correct python file
- manage.py is not needed