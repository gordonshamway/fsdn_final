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
conf = TestConfig()
ADMIN_TOKEN = conf['ADMIN_TOKEN']
RESTAURANT_MANAGER_TOKEN = conf['RESTAURANT_MANAGER_TOKEN']
GUEST_TOKEN = conf['GUEST_TOKEN']


class RestaurantTestCase(unittest.TestCase):
    """This class represents the restaurant test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(TestConfig())
        self.client = self.app.test_client
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
                   ADMIN_TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Yummy Restaurant',
            'country': 'Germany',
            'city': 'Ratingen',
            'postcode': '40885',
            'street': 'Scheidter Bruch 20',
            'owner': 'Stefan Buchholz',
            'email': 'stef.buchholz@abc.com'
        }
        res = self.client().post(
            '/api/v1/restaurants', json=test_data, headers=headers
            )
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_payload['success'], True)
        self.assertEqual(res_payload['restaurant']['name'], 'Yummy Restaurant')

    def test_create_restaurant_failure(self):
        headers = {'Authorization': 'Bearer ' +
                   ADMIN_TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': None
        }
        res = self.client().post(
            '/api/v1/restaurants', json=test_data, headers=headers
            )
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(res_payload['success'], False)

    def test_restaurant_list_success(self):
        # first create a restaurant
        headers = {'Authorization': 'Bearer ' +
                   ADMIN_TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Yummy Restaurant',
            'country': 'Germany',
            'city': 'Ratingen',
            'postcode': '40885',
            'street': 'Scheidter Bruch 20',
            'owner': 'Stefan Buchholz',
            'email': 'stef.buchholz@abc.com'
        }
        res = self.client().post(
            '/api/v1/restaurants', json=test_data, headers=headers
            )

        # than test it
        res = self.client().get('/api/v1/restaurants', headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_payload['success'], True)
        self.assertGreaterEqual(len(res_payload['restaurants']), 1)

    def test_restaurant_details_success(self):
        headers = {'Authorization': 'Bearer ' +
                   ADMIN_TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Yummy Restaurant',
            'country': 'Germany',
            'city': 'Ratingen',
            'postcode': '40885',
            'street': 'Scheidter Bruch 20',
            'owner': 'Stefan Buchholz',
            'email': 'stef.buchholz@abc.com'
        }
        res = self.client().post(
            '/api/v1/restaurants', json=test_data, headers=headers
            )
        res_payload = json.loads(res.data)
        id = res_payload['restaurant']['id']

        # finally check if the restaurant detail is there
        res = self.client().get(f'/api/v1/restaurants/{id}', headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_payload['success'], True)
        self.assertEqual(res_payload['restaurant']['postcode'], str(40885))

    def test_restaurant_details_failure(self):
        headers = {'Authorization': 'Bearer ' + ADMIN_TOKEN}
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
        res = self.client().post(
            '/api/v1/restaurants', json=test_data, headers=headers
            )
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
                   ADMIN_TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Yummy Restaurant2'
        }
        res = self.client().patch(
            '/api/v1/restaurants/99', json=test_data, headers=headers
            )
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res_payload['success'], False)

    def test_restaurant_delete_failure(self):
        headers = {'Authorization': 'Bearer ' + ADMIN_TOKEN}
        res = self.client().delete('/api/v1/restaurants/99', headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res_payload['success'], False)

    def test_restaurant_delete_success(self):
        # create basic restaurant
        headers = {'Authorization': 'Bearer ' +
                   ADMIN_TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Yummy Restaurant',
            'country': 'Germany',
            'city': 'Ratingen',
            'postcode': '40885',
            'street': 'Scheidter Bruch 20',
            'owner': 'Stefan Buchholz',
            'email': 'stef.buchholz@abc.com'
        }
        res = self.client().post(
            '/api/v1/restaurants', json=test_data, headers=headers
            )
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
                   ADMIN_TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Yummy Restaurant',
            'country': 'Germany',
            'city': 'Ratingen',
            'postcode': '40885',
            'street': 'Scheidter Bruch 20',
            'owner': 'Stefan Buchholz',
            'email': 'stef.buchholz@abc.com'
        }
        res = self.client().post(
            '/api/v1/restaurants', json=test_data, headers=headers
            )
        res_payload = json.loads(res.data)
        id = res_payload['restaurant']['id']

        # now create the table
        res = self.client().post(
            f'/api/v1/restaurants/{id}/tables', headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_payload['success'], True)

    def test_create_table_failure(self):
        headers = {'Authorization': 'Bearer ' + ADMIN_TOKEN}
        res = self.client().post(
            '/api/v1/restaurants/99/tables', headers=headers
            )
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(res_payload['success'], False)

    def test_delete_table_success(self):
        # first create restaurant
        # create basic restaurant
        headers = {'Authorization': 'Bearer ' +
                   ADMIN_TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Yummy Restaurant',
            'country': 'Germany',
            'city': 'Ratingen',
            'postcode': '40885',
            'street': 'Scheidter Bruch 20',
            'owner': 'Stefan Buchholz',
            'email': 'stef.buchholz@abc.com'
        }
        res = self.client().post(
            '/api/v1/restaurants', json=test_data, headers=headers
            )
        res_payload = json.loads(res.data)
        restaurant_id = res_payload['restaurant']['id']

        # second create a table
        res = self.client().post(
            f'/api/v1/restaurants/{restaurant_id}/tables', headers=headers)
        res_payload = json.loads(res.data)
        table_id = res_payload['table_id']

        res = self.client().delete(
            f'/api/v1/restaurants/{restaurant_id}/tables/{table_id}',
            headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_payload['success'], True)

    def test_delete_table_failure(self):
        headers = {'Authorization': 'Bearer ' + ADMIN_TOKEN}
        res = self.client().delete(
            '/api/v1/restaurants/1/tables/99', headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res_payload['success'], False)

    def test_create_guest_success(self):
        headers = {'Authorization': 'Bearer ' +
                   ADMIN_TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Dieter Konrad',
            'street': 'Banausenweg 1',
            'city': 'Duisburg',
            'postcode': '49257',
            'country': 'Germany',
            'email': 'teest@test.com',
        }
        res = self.client().post(
            '/api/v1/guests', json=test_data, headers=headers
            )
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_payload['success'], True)
        self.assertEqual(res_payload['guest']['name'], 'Dieter Konrad')

    def test_create_guest_failure(self):
        headers = {'Authorization': 'Bearer ' +
                   ADMIN_TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Dieter Konrad'
        }
        res = self.client().post(
            '/api/v1/guests', json=test_data, headers=headers
            )
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(res_payload['success'], False)

    def test_get_list_guest_success(self):
        # first create a guest
        headers = {'Authorization': 'Bearer ' +
                   ADMIN_TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Dieter Konrad',
            'street': 'Banausenweg 1',
            'city': 'Duisburg',
            'postcode': '49257',
            'country': 'Germany',
            'email': 'teest@test.com',
        }
        res = self.client().post(
            '/api/v1/guests', json=test_data, headers=headers
            )
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
                   ADMIN_TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Dieter Konrad',
            'street': 'Banausenweg 1',
            'city': 'Duisburg',
            'postcode': '49257',
            'country': 'Germany',
            'email': 'teest@test.com',
        }
        res = self.client().post(
            '/api/v1/guests', json=test_data, headers=headers
            )
        res_payload = json.loads(res.data)
        guest_id = res_payload['guest']['id']

        # and then test it
        res = self.client().get(
            f'/api/v1/guests/{guest_id}', headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_payload['success'], True)
        self.assertEqual(res_payload['guest']['name'], 'Dieter Konrad')

    def test_get_guest_details_failure(self):
        headers = {'Authorization': 'Bearer ' + ADMIN_TOKEN}
        res = self.client().get('/api/v1/guests/99', headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res_payload['success'], False)

    def test_update_guest_success(self):
        # first create a new user
        headers = {'Authorization': 'Bearer ' +
                   ADMIN_TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Dieter Konrad',
            'street': 'Banausenweg 1',
            'city': 'Duisburg',
            'postcode': '49257',
            'country': 'Germany',
            'email': 'teest@test.com',
        }
        res = self.client().post(
            '/api/v1/guests', json=test_data, headers=headers
            )
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
                   ADMIN_TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Konrad Dieter'
        }
        res = self.client().patch(
            '/api/v1/guests/99', json=test_data, headers=headers
            )
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(res_payload['success'], False)

    def test_create_visit_success(self):
        # first create restaurant
        headers = {'Authorization': 'Bearer ' +
                   ADMIN_TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Yummy Restaurant',
            'country': 'Germany',
            'city': 'Ratingen',
            'postcode': '40885',
            'street': 'Scheidter Bruch 20',
            'owner': 'Stefan Buchholz',
            'email': 'stef.buchholz@abc.com'
        }
        res = self.client().post(
            '/api/v1/restaurants', json=test_data, headers=headers
            )
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
        res = self.client().post(
            '/api/v1/guests', json=test_data, headers=headers
            )
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
            f'/api/v1/restaurants/{restaurant_id}/visits',
            json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_payload['success'], True)

    def test_create_visit_failure(self):
        headers = {'Authorization': 'Bearer ' + ADMIN_TOKEN}
        res = self.client().post(
            '/api/v1/restaurants/99/visits', headers=headers
            )
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(res_payload['success'], False)

    def test_patch_visit_success(self):
        # first create restaurant
        headers = {'Authorization': 'Bearer ' +
                   ADMIN_TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Yummy Restaurant',
            'country': 'Germany',
            'city': 'Ratingen',
            'postcode': '40885',
            'street': 'Scheidter Bruch 20',
            'owner': 'Stefan Buchholz',
            'email': 'stef.buchholz@abc.com'
        }
        res = self.client().post(
            '/api/v1/restaurants', json=test_data, headers=headers
            )
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
        res = self.client().post(
            '/api/v1/guests', json=test_data, headers=headers
            )
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
            f'/api/v1/restaurants/{restaurant_id}/visits',
            json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        visit_id = res_payload['visit_id']

        res = self.client().patch(
            f'/api/v1/restaurants/{restaurant_id}/visits/{visit_id}',
            headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_payload['success'], True)

    def test_patch_visit_failure(self):
        headers = {'Authorization': 'Bearer ' + ADMIN_TOKEN}
        res = self.client().patch(
            '/api/v1/restaurants/1/visits/99', headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(res_payload['success'], False)

    def test_get_notifications_success(self):
        headers = {'Authorization': 'Bearer ' + ADMIN_TOKEN}
        res = self.client().get(
            '/api/v1/guests/1/notifications', headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_payload['success'], True)

    def test_admin_role_success(self):
        headers = {'Authorization': 'Bearer ' +
                   ADMIN_TOKEN, 'Content-type': 'application/json'}
        test_data = {
            'name': 'Dieter Konrad',
            'street': 'Banausenweg 1',
            'city': 'Duisburg',
            'postcode': '49257',
            'country': 'Germany',
            'email': 'teest@test.com',
        }
        res = self.client().post(
            '/api/v1/guests', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        guest_id = res_payload['guest']['id']

        # and then test it
        res = self.client().get(
            f'/api/v1/guests/{guest_id}', headers=headers)
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
        res = self.client().post(
            '/api/v1/guests', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        guest_id = res_payload['guest']['id']

        # and then test it
        res = self.client().get(
            f'/api/v1/guests/{guest_id}', headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res_payload['success'], False)

    def test_restaurant_manager_success(self):
        headers = {
            'Authorization': 'Bearer ' + RESTAURANT_MANAGER_TOKEN,
            'Content-type': 'application/json'}
        test_data = {
            'name': 'Yummy Restaurant',
            'country': 'Germany',
            'city': 'Ratingen',
            'postcode': '40885',
            'street': 'Scheidter Bruch 20',
            'owner': 'Stefan Buchholz',
            'email': 'stef.buchholz@abc.com'
        }
        res = self.client().post(
            '/api/v1/restaurants', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_payload['success'], True)
        self.assertEqual(res_payload['restaurant']['name'], 'Yummy Restaurant')

    def test_restaurant_manager_failure(self):
        TOKEN = 'xxx'
        headers = {
            'Authorization': 'Bearer ' + TOKEN,
            'Content-type': 'application/json'}
        test_data = {
            'name': 'Yummy Restaurant',
            'country': 'Germany',
            'city': 'Ratingen',
            'postcode': '40885',
            'street': 'Scheidter Bruch 20',
            'owner': 'Stefan Buchholz',
            'email': 'stef.buchholz@abc.com'
        }
        res = self.client().post(
            '/api/v1/restaurants', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res_payload['success'], False)

    def test_guest_role_success(self):
        headers = {
            'Authorization': 'Bearer ' + GUEST_TOKEN,
            'Content-type': 'application/json'}
        test_data = {
            'name': 'Dieter Konrad',
            'street': 'Banausenweg 1',
            'city': 'Duisburg',
            'postcode': '49257',
            'country': 'Germany',
            'email': 'teest@test.com',
        }
        res = self.client().post(
            '/api/v1/guests', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        guest_id = res_payload['guest']['id']

        # and then test it
        res = self.client().get(
            f'/api/v1/guests/{guest_id}', headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_payload['success'], True)
        self.assertEqual(res_payload['guest']['name'], 'Dieter Konrad')

    def test_guest_role_failure(self):
        TOKEN = 'xxx'
        headers = {
            'Authorization': 'Bearer ' + TOKEN,
            'Content-type': 'application/json'}
        test_data = {
            'name': 'Dieter Konrad',
            'street': 'Banausenweg 1',
            'city': 'Duisburg',
            'postcode': '49257',
            'country': 'Germany',
            'email': 'teest@test.com',
        }
        res = self.client().post(
            '/api/v1/guests', json=test_data, headers=headers)
        res_payload = json.loads(res.data)
        guest_id = res_payload['guest']['id']

        # and then test it
        res = self.client().get(
            f'/api/v1/guests/{guest_id}', headers=headers)
        res_payload = json.loads(res.data)
        self.assertEqual(res_payload['success'], False)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
