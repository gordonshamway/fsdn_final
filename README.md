# Goal
# Structure
# ERD
This is the basic ERD Diagramm that describes the relationship of the underlying tables:

![ERD-Diagramm](/docs/erd.png)
# Endpoints
Here is the list of all possible endpoints:

## Restaurants
Can be created by owner, Government can get lists of all. Owner can see the details and update its details.
Deletion can only by done by admin.
1. /api/v1/restaurants/
    - POST - Create new restaurant
    - GET - List of all restaurants
2. /api/v1/restaurants/{ID}
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
guest deletion is not programmed because it should not delete, old facts would be orphanized
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
![Roles_and_Rights](/docs/roles_and_rights.PNG)

# Todo
- PEP8 stuff
- ERD corrections
- Documentation. why there are that many endpoints and only x many tests

# Motivation for the project

# Dependencies

# How to start

# How to host

# How to authenticate
Name            fsnd_corona
Tenant Domain   sbu47533.eu.auth0.com
Client_ID       HljTzT3THfu0P378ejF06XH0jRycrBEc
Client Secret   -IKso73RjdJHmYT3KpOQJdXKbXdKujcdKNNvJ1mzSb0v_oWu6zXOVYuA6JQb8YxQ

api_name        fsnd_corona_api
identifier      http://localhost:5000

## HTML Template
https://[your_tenant].us.auth0.com/authorize?audience=[your-audience]&response_type=token&client_id=[your_client_id] &redirect_uri=[redirect]

## Login Page
https://sbu47533.eu.auth0.com/authorize?audience=http://localhost:5000&response_type=token&
client_id=HljTzT3THfu0P378ejF06XH0jRycrBEc&redirect_uri=http://localhost:5000

https://sbu47533.eu.auth0.com/authorize?audience=http://localhost:5000&response_type=token&client_id=HljTzT3THfu0P378ejF06XH0jRycrBEc&redirect_uri=https://corona-fsnd.herokuapp.com

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

# Documents that helped
https://github.com/jungleBadger/udacity_coffee_shop/blob/master/troubleshooting/generate_token.md
https://knowledge.udacity.com/questions/423462
https://stackoverflow.com/questions/34478320/how-to-set-gunicorn-to-find-a-flask-application/34478356

## My - Heroku URL
https://corona-fsnd.herokuapp.com/
https://git.heroku.com/corona-fsnd.git

# Befehl um die Migration anzustoßen
```bash
heroku run FLASK_APP=src/api/api.py flask db upgrade --directory src/api/migr
ations
```