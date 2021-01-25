import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from api.api import create_app
from api.database.models import setup_db, Restaurant, Table, User, Visit
from api.config import TestConfig

# https://knowledge.udacity.com/questions/373159
# for unittest i dont need migrations just db.create_all
# also i need some create_app procedure in the main app!

TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikx1OUhVcTJVWjdaRkdkdkNKenZ1diJ9.eyJpc3MiOiJodHRwczovL3NidTQ3NTMzLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDBkNGRiNzhlNWY1MzAwNmE4MjQ1Y2YiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjUwMDAiLCJpYXQiOjE2MTE1OTk0MzksImV4cCI6MTYxMTYwNjYzOSwiYXpwIjoiSGxqVHpUM1RIZnUwUDM3OGVqRjA2WEgwalJ5Y3JCRWMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpyZXN0YXVyYW50IiwiZGVsZXRlOnJlc3RhdXJhbnQtdGFibGUiLCJnZXQ6Z3Vlc3QtZGV0YWlscyIsImdldDpndWVzdC1ub3RpZmljYXRpb25zIiwiZ2V0Omd1ZXN0cyIsImdldDpyZXN0YXVyYW50IiwiZ2V0OnJlc3RhdXJhbnQtZGV0YWlscyIsImdldDpyZXN0YXVyYW50LXZpc2l0cyIsInBhdGNoOmd1ZXN0LWRldGFpbHMiLCJwYXRjaDpyZXN0YXVyYW50LWRldGFpbHMiLCJwYXRjaDpyZXN0YXVyYW50LXZpc2l0cyIsInBvc3Q6Z3Vlc3QiLCJwb3N0OnJlc3RhdXJhbnQiLCJwb3N0OnJlc3RhdXJhbnQtdGFibGUiLCJwb3N0OnJlc3RhdXJhbnQtdmlzaXRzIl19.sUJbxpPFm0tQV5z5-Kc9gicFxXwU5AYkKtE6VZdFpL8r5Ftqu1wGVh_tX0xNc8AqQOQGMS5CwGpQuEXO7_ptPt1xKzubydR8PXRtN2tTeBIeAvz-PH_vofy_2DMli84tBGdLOYNfOVmuefAHlo2sgVQy9qmobRrKHYpBMLV16Eppd0mM4ri34jKUAi6L7PZkz-7oN9r-SghpFOp0qeyv3Sa0dv-Gmi3W47MlLqveDcVx-pnLUI6890ZXgdFenyQRif8ECrtuuBhL3NhPFfsL2n1kI00jpLZg3C1UtNjnDzJS75DMmuhBFS7MOChJGaRiyPhAh_5F7m_wgeVw-hku0Q'


class RestaurantTestCase(unittest.TestCase):
    """This class represents the restaurant test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(TestConfig())
        self.client = self.app.test_client
        #self.database_name = "corona_test"
        #self.username = os.environ.get('TEST_USERNAME')
        #self.password = os.environ.get('TEST_PASSWORD')
        #self.server = os.environ.get('TEST_SERVER')
        #self.port = os.environ.get('TEST_PORT')
        #self.database_path = "postgres://{}:{}@{}:{}/{}".format(self.username, self.password, self.server, self.port, self.database_name)
        setup_db(self.app)
        # db.create_all()

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
        #     # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after each test"""
        # db.drop_all()
        with self.app.app_context():
            self.db.session.remove()
            self.db.drop_all()

    def test_create_restaurant_success(self):
        headers = {'Authorization': 'Bearer ' +
                   TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Yummy Restaurant',
            'country': 'Germany',
            'city': 'Ratingen',
            'postcode': '40885',
            'street': 'Scheidter Bruch 20',
            'owner': 'Stefan Buchholz',
            'email': 'stef.buchholz@abc.com'
        }
        res = self.client().post('/api/v1/restaurants', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_payload['success'], True)
        self.assertEqual(res_payload['restaurant']['name'], 'Yummy Restaurant')

    def test_create_restaurant_failure(self):
        headers = {'Authorization': 'Bearer ' +
                   TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': None
        }
        res = self.client().post('/api/v1/restaurants', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(res_payload['success'], False)

    def test_restaurant_list_success(self):
        # first create a restaurant
        headers = {'Authorization': 'Bearer ' +
                   TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Yummy Restaurant',
            'country': 'Germany',
            'city': 'Ratingen',
            'postcode': '40885',
            'street': 'Scheidter Bruch 20',
            'owner': 'Stefan Buchholz',
            'email': 'stef.buchholz@abc.com'
        }
        res = self.client().post('/api/v1/restaurants', json=test_data, headers=headers)

        # than test it
        res = self.client().get('/api/v1/restaurants', headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_payload['success'], True)
        self.assertGreaterEqual(len(res_payload['restaurants']), 1)

    def test_restaurant_details_success(self):
        headers = {'Authorization': 'Bearer ' +
                   TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Yummy Restaurant',
            'country': 'Germany',
            'city': 'Ratingen',
            'postcode': '40885',
            'street': 'Scheidter Bruch 20',
            'owner': 'Stefan Buchholz',
            'email': 'stef.buchholz@abc.com'
        }
        res = self.client().post('/api/v1/restaurants', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        id = res_payload['restaurant']['id']

        # finally check if the restaurant detail is there
        res = self.client().get(f'/api/v1/restaurants/{id}', headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_payload['success'], True)
        self.assertEqual(res_payload['restaurant']['postcode'], str(40885))

    def test_restaurant_details_failure(self):
        headers = {'Authorization': 'Bearer ' + TOKEN}
        res = self.client().get('/api/v1/restaurants/99', headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res_payload['success'], False)

    def test_restaurant_update_success(self):
        # create basic restaurant
        headers = {'Authorization': 'Bearer ' +
                   TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Yummy Restaurant',
            'country': 'Germany',
            'city': 'Ratingen',
            'postcode': '40885',
            'street': 'Scheidter Bruch 20',
            'owner': 'Stefan Buchholz',
            'email': 'stef.buchholz@abc.com'
        }
        res = self.client().post('/api/v1/restaurants', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        id = res_payload['restaurant']['id']

        # finally check if the restaurant detail is there
        res = self.client().get(f'/api/v1/restaurants/{id}', headers=headers)
        test_data = {
            'name': 'Yummy Restaurant2'
        }
        # check the data
        res = self.client().patch(
            f'/api/v1/restaurants/{id}', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_payload['success'], True)
        self.assertEqual(res_payload['restaurant']
                         ['name'], 'Yummy Restaurant2')

    def test_restaurant_update_failure(self):
        headers = {'Authorization': 'Bearer ' +
                   TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Yummy Restaurant2'
        }
        res = self.client().patch('/api/v1/restaurants/99', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res_payload['success'], False)

    def test_restaurant_delete_failure(self):
        headers = {'Authorization': 'Bearer ' + TOKEN}
        res = self.client().delete('/api/v1/restaurants/99', headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res_payload['success'], False)

    def test_restaurant_delete_success(self):
        # create basic restaurant
        headers = {'Authorization': 'Bearer ' +
                   TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Yummy Restaurant',
            'country': 'Germany',
            'city': 'Ratingen',
            'postcode': '40885',
            'street': 'Scheidter Bruch 20',
            'owner': 'Stefan Buchholz',
            'email': 'stef.buchholz@abc.com'
        }
        res = self.client().post('/api/v1/restaurants', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        id = res_payload['restaurant']['id']

        # test deletion
        res = self.client().delete(
            f'/api/v1/restaurants/{id}', headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_payload['success'], True)

    def test_create_table_success(self):
        # first create restaurant
        # create basic restaurant
        headers = {'Authorization': 'Bearer ' +
                   TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Yummy Restaurant',
            'country': 'Germany',
            'city': 'Ratingen',
            'postcode': '40885',
            'street': 'Scheidter Bruch 20',
            'owner': 'Stefan Buchholz',
            'email': 'stef.buchholz@abc.com'
        }
        res = self.client().post('/api/v1/restaurants', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        id = res_payload['restaurant']['id']

        # now create the table
        res = self.client().post(
            f'/api/v1/restaurants/{id}/tables', headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_payload['success'], True)

    def test_create_table_failure(self):
        headers = {'Authorization': 'Bearer ' + TOKEN}
        res = self.client().post('/api/v1/restaurants/99/tables', headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(res_payload['success'], False)

    def test_delete_table_success(self):
        # first create restaurant
        # create basic restaurant
        headers = {'Authorization': 'Bearer ' +
                   TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Yummy Restaurant',
            'country': 'Germany',
            'city': 'Ratingen',
            'postcode': '40885',
            'street': 'Scheidter Bruch 20',
            'owner': 'Stefan Buchholz',
            'email': 'stef.buchholz@abc.com'
        }
        res = self.client().post('/api/v1/restaurants', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        restaurant_id = res_payload['restaurant']['id']

        # second create a table
        res = self.client().post(
            f'/api/v1/restaurants/{restaurant_id}/tables', headers=headers)
        res_payload = json.loads(res.data)
        table_id = res_payload['table_id']

        res = self.client().delete(
            f'/api/v1/restaurants/{restaurant_id}/tables/{table_id}', headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_payload['success'], True)

    def test_delete_table_failure(self):
        headers = {'Authorization': 'Bearer ' + TOKEN}
        res = self.client().delete('/api/v1/restaurants/1/tables/99', headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res_payload['success'], False)

    def test_create_guest_success(self):
        headers = {'Authorization': 'Bearer ' +
                   TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Dieter Konrad',
            'street': 'Banausenweg 1',
            'city': 'Duisburg',
            'postcode': '49257',
            'country': 'Germany',
            'email': 'teest@test.com',
        }
        res = self.client().post('/api/v1/guests', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_payload['success'], True)
        self.assertEqual(res_payload['guest']['name'], 'Dieter Konrad')

    def test_create_guest_failure(self):
        headers = {'Authorization': 'Bearer ' +
                   TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Dieter Konrad'
        }
        res = self.client().post('/api/v1/guests', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(res_payload['success'], False)

    def test_get_list_guest_success(self):
        # first create a guest
        headers = {'Authorization': 'Bearer ' +
                   TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Dieter Konrad',
            'street': 'Banausenweg 1',
            'city': 'Duisburg',
            'postcode': '49257',
            'country': 'Germany',
            'email': 'teest@test.com',
        }
        res = self.client().post('/api/v1/guests', json=test_data, headers=headers)
        res_payload = json.loads(res.data)

        # and then test it
        res = self.client().get('/api/v1/guests', headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_payload['success'], True)
        self.assertGreaterEqual(res_payload['user_count'], 1)

    def test_get_guest_details_success(self):
        # first create a guest
        headers = {'Authorization': 'Bearer ' +
                   TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Dieter Konrad',
            'street': 'Banausenweg 1',
            'city': 'Duisburg',
            'postcode': '49257',
            'country': 'Germany',
            'email': 'teest@test.com',
        }
        res = self.client().post('/api/v1/guests', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        guest_id = res_payload['guest']['id']

        # and then test it
        res = self.client().get(f'/api/v1/guests/{guest_id}', headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_payload['success'], True)
        self.assertEqual(res_payload['guest']['name'], 'Dieter Konrad')

    def test_get_guest_details_failure(self):
        headers = {'Authorization': 'Bearer ' + TOKEN}
        res = self.client().get('/api/v1/guests/99', headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res_payload['success'], False)

    def test_update_guest_success(self):
        # first create a new user
        headers = {'Authorization': 'Bearer ' +
                   TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Dieter Konrad',
            'street': 'Banausenweg 1',
            'city': 'Duisburg',
            'postcode': '49257',
            'country': 'Germany',
            'email': 'teest@test.com',
        }
        res = self.client().post('/api/v1/guests', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        guest_id = res_payload['guest']['id']
        # than patch the name
        test_data = {
            'name': 'Konrad Dieter'
        }
        res = self.client().patch(
            f'/api/v1/guests/{guest_id}', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_payload['guest']['name'], 'Konrad Dieter')

    def test_update_guest_failure(self):
        headers = {'Authorization': 'Bearer ' +
                   TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Konrad Dieter'
        }
        res = self.client().patch('/api/v1/guests/99', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(res_payload['success'], False)

    def test_create_visit_success(self):
        # first create restaurant
        headers = {'Authorization': 'Bearer ' +
                   TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Yummy Restaurant',
            'country': 'Germany',
            'city': 'Ratingen',
            'postcode': '40885',
            'street': 'Scheidter Bruch 20',
            'owner': 'Stefan Buchholz',
            'email': 'stef.buchholz@abc.com'
        }
        res = self.client().post('/api/v1/restaurants', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        restaurant_id = res_payload['restaurant']['id']

        # second create user
        test_data = {
            'name': 'Dieter Konrad',
            'street': 'Banausenweg 1',
            'city': 'Duisburg',
            'postcode': '49257',
            'country': 'Germany',
            'email': 'teest@test.com',
        }
        res = self.client().post('/api/v1/guests', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        guest_id = res_payload['guest']['id']

        # create table
        res = self.client().post(
            f'/api/v1/restaurants/{restaurant_id}/tables', headers=headers)
        res_payload = json.loads(res.data)
        table_id = res_payload['table_id']

        # create payload
        test_data = {
            'table_id': table_id,
            'user_id': guest_id
        }

        # send the payload
        res = self.client().post(
            f'/api/v1/restaurants/{restaurant_id}/visits', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_payload['success'], True)

    def test_create_visit_failure(self):
        headers = {'Authorization': 'Bearer ' + TOKEN}
        res = self.client().post('/api/v1/restaurants/99/visits', headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(res_payload['success'], False)

    def test_patch_visit_success(self):
        # first create restaurant
        headers = {'Authorization': 'Bearer ' +
                   TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Yummy Restaurant',
            'country': 'Germany',
            'city': 'Ratingen',
            'postcode': '40885',
            'street': 'Scheidter Bruch 20',
            'owner': 'Stefan Buchholz',
            'email': 'stef.buchholz@abc.com'
        }
        res = self.client().post('/api/v1/restaurants', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        restaurant_id = res_payload['restaurant']['id']

        # second create user
        test_data = {
            'name': 'Dieter Konrad',
            'street': 'Banausenweg 1',
            'city': 'Duisburg',
            'postcode': '49257',
            'country': 'Germany',
            'email': 'teest@test.com',
        }
        res = self.client().post('/api/v1/guests', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        guest_id = res_payload['guest']['id']

        # create table
        res = self.client().post(
            f'/api/v1/restaurants/{restaurant_id}/tables', headers=headers)
        res_payload = json.loads(res.data)
        table_id = res_payload['table_id']

        # create payload
        test_data = {
            'table_id': table_id,
            'user_id': guest_id
        }

        # send the payload
        res = self.client().post(
            f'/api/v1/restaurants/{restaurant_id}/visits', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        visit_id = res_payload['visit_id']

        res = self.client().patch(
            f'/api/v1/restaurants/{restaurant_id}/visits/{visit_id}', headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_payload['success'], True)

    def test_patch_visit_failure(self):
        headers = {'Authorization': 'Bearer ' + TOKEN}
        res = self.client().patch('/api/v1/restaurants/1/visits/99', headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(res_payload['success'], False)

    def test_get_notifications_success(self):
        headers = {'Authorization': 'Bearer ' + TOKEN}
        res = self.client().get('/api/v1/guests/1/notifications', headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_payload['success'], True)

    def test_admin_role_success(self):
        TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikx1OUhVcTJVWjdaRkdkdkNKenZ1diJ9.eyJpc3MiOiJodHRwczovL3NidTQ3NTMzLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDBkNGRiNzhlNWY1MzAwNmE4MjQ1Y2YiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjUwMDAiLCJpYXQiOjE2MTE1OTk0MzksImV4cCI6MTYxMTYwNjYzOSwiYXpwIjoiSGxqVHpUM1RIZnUwUDM3OGVqRjA2WEgwalJ5Y3JCRWMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpyZXN0YXVyYW50IiwiZGVsZXRlOnJlc3RhdXJhbnQtdGFibGUiLCJnZXQ6Z3Vlc3QtZGV0YWlscyIsImdldDpndWVzdC1ub3RpZmljYXRpb25zIiwiZ2V0Omd1ZXN0cyIsImdldDpyZXN0YXVyYW50IiwiZ2V0OnJlc3RhdXJhbnQtZGV0YWlscyIsImdldDpyZXN0YXVyYW50LXZpc2l0cyIsInBhdGNoOmd1ZXN0LWRldGFpbHMiLCJwYXRjaDpyZXN0YXVyYW50LWRldGFpbHMiLCJwYXRjaDpyZXN0YXVyYW50LXZpc2l0cyIsInBvc3Q6Z3Vlc3QiLCJwb3N0OnJlc3RhdXJhbnQiLCJwb3N0OnJlc3RhdXJhbnQtdGFibGUiLCJwb3N0OnJlc3RhdXJhbnQtdmlzaXRzIl19.sUJbxpPFm0tQV5z5-Kc9gicFxXwU5AYkKtE6VZdFpL8r5Ftqu1wGVh_tX0xNc8AqQOQGMS5CwGpQuEXO7_ptPt1xKzubydR8PXRtN2tTeBIeAvz-PH_vofy_2DMli84tBGdLOYNfOVmuefAHlo2sgVQy9qmobRrKHYpBMLV16Eppd0mM4ri34jKUAi6L7PZkz-7oN9r-SghpFOp0qeyv3Sa0dv-Gmi3W47MlLqveDcVx-pnLUI6890ZXgdFenyQRif8ECrtuuBhL3NhPFfsL2n1kI00jpLZg3C1UtNjnDzJS75DMmuhBFS7MOChJGaRiyPhAh_5F7m_wgeVw-hku0Q'
        headers = {'Authorization': 'Bearer ' +
                   TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Dieter Konrad',
            'street': 'Banausenweg 1',
            'city': 'Duisburg',
            'postcode': '49257',
            'country': 'Germany',
            'email': 'teest@test.com',
        }
        res = self.client().post('/api/v1/guests', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        guest_id = res_payload['guest']['id']

        # and then test it
        res = self.client().get(f'/api/v1/guests/{guest_id}', headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_payload['success'], True)
        self.assertEqual(res_payload['guest']['name'], 'Dieter Konrad')

    def test_admin_role_failure(self):
        TOKEN = 'xxx'
        headers = {'Authorization': 'Bearer ' +
                   TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Dieter Konrad',
            'street': 'Banausenweg 1',
            'city': 'Duisburg',
            'postcode': '49257',
            'country': 'Germany',
            'email': 'teest@test.com',
        }
        res = self.client().post('/api/v1/guests', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        guest_id = res_payload['guest']['id']

        # and then test it
        res = self.client().get(f'/api/v1/guests/{guest_id}', headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res_payload['success'], False)
    
    def test_restaurant_manager_success(self):
        TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikx1OUhVcTJVWjdaRkdkdkNKenZ1diJ9.eyJpc3MiOiJodHRwczovL3NidTQ3NTMzLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDBkNGUzZDAzMGI4ZjAwNmE1MTQzODIiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjUwMDAiLCJpYXQiOjE2MTE1OTk2MDUsImV4cCI6MTYxMTYwNjgwNSwiYXpwIjoiSGxqVHpUM1RIZnUwUDM3OGVqRjA2WEgwalJ5Y3JCRWMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpyZXN0YXVyYW50IiwiZ2V0OnJlc3RhdXJhbnQtZGV0YWlscyIsImdldDpyZXN0YXVyYW50LXZpc2l0cyIsInBhdGNoOnJlc3RhdXJhbnQtZGV0YWlscyIsInBvc3Q6cmVzdGF1cmFudCIsInBvc3Q6cmVzdGF1cmFudC10YWJsZSJdfQ.OlSvq3GVHNaab6gWDl_CNfb7p-UCwdqr5Ut4mM-ZX5sU1Yt0WrWiXDLgd6fMYOSlEtsDlybmg-M-XS-B9BVbrK1yrW8FESysFM9_Zq-Q386GzBsPUWCqVG7QGoruHa4kvkJhMeytbRLQrk3lV_F1ngkyjZ1CvbgD0Z2GokKnUlpT3GhD4j1oO2rwUoFYQ9lpvZngJe_dsMLVrMxxDS8jMhYJiapKL4B-57Ddojb6oT58AE_IRe3KGruSd8GFS309HMV7w_eB7g-7PYUVA0xNjbMC4lSy0MOFoBS3GjGfBjdQkNe5ew9YcFi_gqoS9WpDgqmxC8KMuKyaYF8KnwN4fw'
        headers = {'Authorization': 'Bearer ' +
                   TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Yummy Restaurant',
            'country': 'Germany',
            'city': 'Ratingen',
            'postcode': '40885',
            'street': 'Scheidter Bruch 20',
            'owner': 'Stefan Buchholz',
            'email': 'stef.buchholz@abc.com'
        }
        res = self.client().post('/api/v1/restaurants', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_payload['success'], True)
        self.assertEqual(res_payload['restaurant']['name'], 'Yummy Restaurant')

    def test_restaurant_manager_failure(self):
        TOKEN = 'xxx'
        headers = {'Authorization': 'Bearer ' +
                   TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Yummy Restaurant',
            'country': 'Germany',
            'city': 'Ratingen',
            'postcode': '40885',
            'street': 'Scheidter Bruch 20',
            'owner': 'Stefan Buchholz',
            'email': 'stef.buchholz@abc.com'
        }
        res = self.client().post('/api/v1/restaurants', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res_payload['success'], False)

    def test_guest_role_success(self):
        TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikx1OUhVcTJVWjdaRkdkdkNKenZ1diJ9.eyJpc3MiOiJodHRwczovL3NidTQ3NTMzLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDBkNGU1ZDhlNWY1MzAwNmE4MjQ2MDEiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjUwMDAiLCJpYXQiOjE2MTE1OTk2NTAsImV4cCI6MTYxMTYwNjg1MCwiYXpwIjoiSGxqVHpUM1RIZnUwUDM3OGVqRjA2WEgwalJ5Y3JCRWMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpndWVzdC1kZXRhaWxzIiwiZ2V0Omd1ZXN0LW5vdGlmaWNhdGlvbnMiLCJnZXQ6cmVzdGF1cmFudCIsInBhdGNoOmd1ZXN0LWRldGFpbHMiLCJwYXRjaDpyZXN0YXVyYW50LXZpc2l0cyIsInBvc3Q6Z3Vlc3QiLCJwb3N0OnJlc3RhdXJhbnQtdmlzaXRzIl19.dl7YTAP6jxr5PTOeVrlOzuDDhne87HcpJhYimxeCo6g12XFJ8qxiQJc-JuDlyUMJol5WftGTFkQJ6syd8PNZ8yD9Zg-Nct_PgaNBKBEz-UPvvr5wRWYNdfFc1qRoen6mFSCwq1vXrL7azq0adaitLABzBQYfnruG2aX_p222QUU1ZnipgmpmDu4dtwiZypqAtheWRtH1icvGiFQ6Eg7WXe4KjQrOvSQ_1MQAnU61YniLUT6juv2dn0sGa2fDTeiQwHJa2Avjw8lpr_7-x7mnO5xtM3QAQRrx9kZFj0aZ7MUWeFSEX6LNKV0ZwfY5yviyg3AkrY8DJiB4TDenQBrh8Q'
        headers = {'Authorization': 'Bearer ' +
                   TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Dieter Konrad',
            'street': 'Banausenweg 1',
            'city': 'Duisburg',
            'postcode': '49257',
            'country': 'Germany',
            'email': 'teest@test.com',
        }
        res = self.client().post('/api/v1/guests', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        guest_id = res_payload['guest']['id']

        # and then test it
        res = self.client().get(f'/api/v1/guests/{guest_id}', headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_payload['success'], True)
        self.assertEqual(res_payload['guest']['name'], 'Dieter Konrad')

    def test_guest_role_failure(self):
        TOKEN = 'xxx'
        headers = {'Authorization': 'Bearer ' +
                   TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Dieter Konrad',
            'street': 'Banausenweg 1',
            'city': 'Duisburg',
            'postcode': '49257',
            'country': 'Germany',
            'email': 'teest@test.com',
        }
        res = self.client().post('/api/v1/guests', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        guest_id = res_payload['guest']['id']

        # and then test it
        res = self.client().get(f'/api/v1/guests/{guest_id}', headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res_payload['success'], False)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
