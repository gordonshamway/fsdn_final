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
- All the heroku stuff
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
https://sbu47533.eu.auth0.com/authorize?audience=http://localhost:5000&response_type=token&client_id=HljTzT3THfu0P378ejF06XH0jRycrBEc&redirect_uri=http://localhost:5000

# Users
Email:      admin@corona.com
Password:   AdminCorona1
Role:       admin
Access-Token:   eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikx1OUhVcTJVWjdaRkdkdkNKenZ1diJ9.eyJpc3MiOiJodHRwczovL3NidTQ3NTMzLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDBkNGRiNzhlNWY1MzAwNmE4MjQ1Y2YiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjUwMDAiLCJpYXQiOjE2MTE0ODY0MzAsImV4cCI6MTYxMTQ5MzYzMCwiYXpwIjoiSGxqVHpUM1RIZnUwUDM3OGVqRjA2WEgwalJ5Y3JCRWMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpyZXN0YXVyYW50IiwiZGVsZXRlOnJlc3RhdXJhbnQtdGFibGUiLCJnZXQ6Z3Vlc3QtZGV0YWlscyIsImdldDpndWVzdC1ub3RpZmljYXRpb25zIiwiZ2V0Omd1ZXN0cyIsImdldDpyZXN0YXVyYW50IiwiZ2V0OnJlc3RhdXJhbnQtZGV0YWlscyIsImdldDpyZXN0YXVyYW50LXZpc2l0cyIsInBhdGNoOmd1ZXN0LWRldGFpbHMiLCJwYXRjaDpyZXN0YXVyYW50LWRldGFpbHMiLCJwYXRjaDpyZXN0YXVyYW50LXZpc2l0cyIsInBvc3Q6Z3Vlc3QiLCJwb3N0OnJlc3RhdXJhbnQiLCJwb3N0OnJlc3RhdXJhbnQtdGFibGUiLCJwb3N0OnJlc3RhdXJhbnQtdmlzaXRzIl19.HvLKYzOHLvmZfzZvTr2Cn8QUtT6y2f7KNBf2thlzB_eR0nAJkmpm90pf-qxP4LHGWBMVHi_h3l_mbFnNqTFoBgAzxLpSj7hr0w-6eF8Btu99UKXdW_l4x7EFMQvKhgXAnTgFss-_-l8jJa2PA0HIFyj1cOWeoh6gft8DYVaPQoI0JFD2-7PQCJlcHN2CkD11wY6Pswhc-RSi4xDsLdApLbjK0p4QN7J1FyJa-Gy2ddH74bm2d_jQplghqw8j9zpHPSTyzE2VXJsKTMnHWwgx3L5o3nun2PyQdy8qeiVTo65ICA2qmtIe42B_E3YCM6lQso3wzOrYYij9dXr1lpJtsg


Email:      restaurant@corona.com
Password:   RestaurantCorona1
Role:       restaurant_manager
Access-Token: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikx1OUhVcTJVWjdaRkdkdkNKenZ1diJ9.eyJpc3MiOiJodHRwczovL3NidTQ3NTMzLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDBkNGUzZDAzMGI4ZjAwNmE1MTQzODIiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjUwMDAiLCJpYXQiOjE2MTE0ODY1NTAsImV4cCI6MTYxMTQ5Mzc1MCwiYXpwIjoiSGxqVHpUM1RIZnUwUDM3OGVqRjA2WEgwalJ5Y3JCRWMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpyZXN0YXVyYW50IiwiZ2V0OnJlc3RhdXJhbnQtZGV0YWlscyIsImdldDpyZXN0YXVyYW50LXZpc2l0cyIsInBhdGNoOnJlc3RhdXJhbnQtZGV0YWlscyIsInBvc3Q6cmVzdGF1cmFudCIsInBvc3Q6cmVzdGF1cmFudC10YWJsZSJdfQ.O0v1XCtUYqllEJjTSwHWpTUKzoYWemEhdYHvgkLoaOo73fnsYFs7snSO_j1iwLwiQM-dq9RSaqvDTcsvAqMhGPEfWikoKBN7vAMsB2GIwZSvEIvtFh-Eodmkj1F6xES_WCRicM5AGm-d5EWS_97mbQbPJ6BkAeeaqSPwFZQ-hsRk8Ut3vn1q7YJEgdXdayXRzugzNoa5BjDpFykwApGHRwayAHbpHqxgxv9da67scVTD5AcLe5u47rEbUbn6vql0p_z385sxzGI31Bl7BgK_B3mKnuCn36QVuW5-66BUyYM0RwSlaPhK6nCcG5lj1GnKLdzJbgFqn2EUvoLIW-JfAw

Email:      guest@corona.com
Password:   GuestCorona1
Role:       guest
Access-Token: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikx1OUhVcTJVWjdaRkdkdkNKenZ1diJ9.eyJpc3MiOiJodHRwczovL3NidTQ3NTMzLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDBkNGU1ZDhlNWY1MzAwNmE4MjQ2MDEiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjUwMDAiLCJpYXQiOjE2MTE0ODY2MDcsImV4cCI6MTYxMTQ5MzgwNywiYXpwIjoiSGxqVHpUM1RIZnUwUDM3OGVqRjA2WEgwalJ5Y3JCRWMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpndWVzdC1kZXRhaWxzIiwiZ2V0Omd1ZXN0LW5vdGlmaWNhdGlvbnMiLCJnZXQ6cmVzdGF1cmFudCIsInBhdGNoOmd1ZXN0LWRldGFpbHMiLCJwYXRjaDpyZXN0YXVyYW50LXZpc2l0cyIsInBvc3Q6Z3Vlc3QiLCJwb3N0OnJlc3RhdXJhbnQtdmlzaXRzIl19.lIQq24qrXo5O3mWheiIxVmCsjxm6KHpnpIKT_sOFRQcdrF6MNiUfLMgUU4HO0lrYPflo5loqSFhJwflO4M6sDqgXpo2CrDNhSdUgr4bDkoajpGD4WP2k2mlCVE4Orr0jg3sqx1f3iWnUM3Ekq-nRge52miwqC0D_7SGamzCtSpsFntphz40DsZeQgfZA0DZN5EfzVw33H_S9OtNuI7PHQeZOscFZ9gsoThyDaYyZk4ES9w6dR12Q9rAvBDqA0YafDLU7BsTNLNnArW7CYperMI2c27WUuRTIj4fjoNMGhw_ugb8CSzw6cf7_2Ixkt2s2ExeYrCKB4rTqv2vGmpQLXQ

# Documents that helped
https://github.com/jungleBadger/udacity_coffee_shop/blob/master/troubleshooting/generate_token.md
https://knowledge.udacity.com/questions/423462

## My - Heroku URL
https://corona-fsnd.herokuapp.com/
https://git.heroku.com/corona-fsnd.git