import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS
from sqlalchemy.sql import func
from .v1.db.models import db_drop_and_create_all, setup_db, Restaurant, Visit, Table, User
from .v1.auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)

'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''
# db_drop_and_create_all()


##########################
######### Routes #########
##########################

@app.route('api/v1/restaurants', methods=['POST'])
def create_new_restaurant():
    '''Creates a new restaurant via POST
    '''
    body = request.get_json()
    name = body.get(name, None)
    country = body.get(country, None)
    city = body.get(city, None)
    postcode = body.get(postcode, None)
    street = body.get(street, None)
    owner = body.get(owner, None)
    email = body.get(email,None)
    amount_of_tables = 0
    if None in (body, name, country, city, postcode, street, owner, email):
        abort(422)
    else:
        try:
            new_restaurant = Restaurant(
                body=body,
                name=name,
                country=country,
                city=city,
                postcode=postcode,
                street=street,
                owner=owner,
                email=email,
                amount_of_tables=amount_of_tables
            )
            new_restaurant.insert()
            return jsonify({
                "success": True,
                "restaurant": new_restaurant.json_repr()
            })
        except Exception:
            abort(422)


@app.route('api/v1/restaurants', methods=['GET'])
#@requires_auth('get:restaurant-list')
def list_restaurants():
    '''Shows a list of all existing restaurants
    '''
    try:
        restaurants = Restaurant.query.order_by(Restaurant.city).all()
    except Exception:
        abort(500)
    if not drinks:
        abort(404)
    else:
        return jsonify({
            "success": True,
            "drinks": [r.json_repr() for r in restaurants]
        })


@app.route('api/v1/restaurants/<int:restaurant_id>/', methods=['GET'])
def show_restaurant_details(restaurant_id):
    '''Shows details of the given restaurant_id
    '''
    this_restaurant = Restaurant.query.filter_by(id=restaurant_id).first()
    if not this_restaurant:
        abort(404)
    else:
        return jsonify({
            "success": True,
            "restaurant": this_restaurant.json_repr()
            }
        )

@app.route('api/v1/restaurants/<int:restaurant_id>/', methods=['PATCH'])
def show_restaurant_details(restaurant_id):
    '''Updates details of the given restaurant_id
    '''
    this_restaurant = Restaurant.query.filter_by(id=restaurant_id).first()
    if not this_restaurant:
        abort(404)
    else:
        body = request.get_json()
        name = body.get(name, None)
        country = body.get(country, None)
        city = body.get(city, None)
        postcode = body.get(postcode, None)
        street = body.get(street, None)
        owner = body.get(owner, None)
        email = body.get(email, None)
        
        if name and name != this_restaurant.name:
            this_restaurant.name = name
        if country and country != this_restaurant.country:
            this_restaurant.country = country
        if city and city != this_restaurant.city:
            this_restaurant.city = city
        if postcode and postcode != this_restaurant.postcode:
            this_restaurant.postcode = postcode
        if street and street != this_restaurant.street:
            this_restaurant.street = street
        if owner and owner != this_restaurant.owner:
            this_restaurant.owner = owner
        if email and email != this_restaurant.email:
            this_restaurant.email = email

        try:
            this_restaurant.update()
            return jsonify({
                "success": True,
                "restaurant": this_restaurant.json_repr()
            })
        except Exception:
            abort(422)

@app.route('api/v1/restaurants/<int:restaurant_id>/', methods=['DELETE'])
def show_restaurant_details(restaurant_id):
    '''Deletion of the given restaurant_id
    '''
    this_restaurant = Restaurant.query.filter_by(id=restaurant_id).first()
    if not this_restaurant:
        abort(404)
    else:
        try:
            this_restaurant.delete()
            return jsonify({
                "success": True,
                "message": f"Restaurant {str(restaurant_id)} successfully deleted"
            })
        except Exception():
            abort(422)

@app.route('/api/v1/restaurants/<int:restaurant_id>/tables', methods=['POST'])
def show_restaurant_tables(restaurant_id):
    '''Creates a new table in a restaurant
    '''
    try:
        this_table = Table(restaurant_id=restaurant_id)
        this_table.insert()
        return jsonify({
            'success': True,
            'message': f'Table Created in restaurant {str(restaurant_id)}'
        })
    except Exception():
        abort(422)

@app.route('/api/v1/restaurants/<int:restaurant_id>/tables/<int:table_id>', methods=['DELETE'])
def delete_restaurant_table(restaurant_id, table_id):
    try:
        this_table = Table.query().filter_by(id=table_id).first()
        this_table.delete()
        return jsonify({
            'success': True,
            'message': f'Successfully delete table {str(table_id)} from restaurant {str(restaurant_id)}'
        })
    except Exception():
        abort(422)

@app.route('/api/v1/restaurants/<int:restaurant_id>/visits', methods=['GET'])
def get_restaurant_visits(restaurant_id):
    '''Receive the list of all guests for that restaurant_id
    @TODO: Maybe I need more parameters here to control the start_date, or get also only sick people
    '''
    try:
        this_restaurants_visits = Visit.query().filter_by(restaurant_id=restaurant_id).all()
        return jsonify({
            'success': True,
            'visits': [v.json_repr() for v in this_restaurants_visits]
        })
    except Exception():
        abort(404)

@app.route('/api/v1/restaurants/<int:restaurant_id>/visits', methods=['POST'])
def post_new_visit(restaurant_id):
    '''Post a new visit for the restaurant_id
    '''
    try:
        body = request.get_json()
        table_id body.get(table_id, None)
        user_id = body.get(user_id, None)
        if None in (table_id, user_id):
            abort(422)
        this_visit = Visit(
            restaurant_id=restaurant_id,
            table_id=table_id,
            user_id=user_id
        )
        this_visit.insert()
        return jsonify({
            'success': True,
            'message': f'New visit created at table {str(table_id)} in restaurant {str(restaurant_id)}'
        })
    except Exception:
        abort(422)

@app.route('api/v1/restaurants/<int:restaurant_id>/visits/{<int:visit_id>', methods=['PATCH'])
def update_visit(restaurant_id, visit_id):
    '''Stop and end the visit
    '''
    try:
        this_visit = Visit.query().filter_by(id=visit_id).first()
        this_visit.visit_end_dt = func.current_date()
        this_visit.update()
        return jsonify({
            'success': True,
            'message': f'Visit {str(visit_id)} has been updated in restaurant {str(restaurant_id)}'
        })
    except Exception:
        abort(422)

@app.route('api/v1/guests', methods='GET')
def get_guest_list():
    '''Get the list of all guests
    '''
    try:
        user_count = User.query().count()
        return jsonify({
            'success': True,
            'user_count': user_count
        })
    except Exception:
        abort(422)

@app.route('api/v1/guests', methods='POST')
def create_new_guest():
    '''Create new user
    '''
    try:
        body = request.get_json()
        name = body.get(name, None)
        street = body.get(street, None)
        city = body.get(city, None)
        postcode = body.get(postcode, None)
        country = body.get(country, None)
        email = body.get(email, None)

        if None in (name, street, city, postcode, country, email):
            abort(422)
        this_user = User(
            name=name,
            street=street,
            city=city,
            postcode=postcode,
            country=country,
            email=email
        )
        this_user.insert()
        return jsonify({
            'success': True,
            'user': this_user.json_repr()
        })
    except Exception:
        abort(422)

@app.route('api/v1/guests/<int:guest_id>', methods='GET')
def get_guest_details(guest_id):
    '''Get guest details
    '''
    try:
        this_guest = User.query().filter_by(id=guest_id).first()
        return jsonify({
            'success': True,
            'guest': this_guest.json_repr()
        })
    except Exception:
        abort(404)


##########################
##### Error Handling #####
##########################

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "not found"
    }), 404


@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "unauthorized"
    }), 401


@app.errorhandler(403)
def forbidden(error):
    return jsonify({
        "success": False,
        "error": 403,
        "message": "forbidden"
    }), 403


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        "success": False,
        "error": 405,
        "message": "method not allowed"
    }), 405


@app.errorhandler(500)
def server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "server error"
    }), 500

@app.errorhandler(AuthError)
def handle_auth_error(err):
    response = jsonify(err.error)
    response.status_code = err.status_code
    return response