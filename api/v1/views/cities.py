#!/usr/bin/python3
"""A module for viewing City objects."""
from api.v1.views import app_views
from flask import jsonify, abort
from models.state import State
from models.city import City
from models import storage


@app_views.route('/states/<state_id>/cities', methods=['GET'])
def cities_in_state(state_id):
    """Retrieves a list of city objects in a state"""
    states_list = storage.all("State").values()
    state = [obj.to_dict() for obj in states if obj.id == state_id]
    if state == []:
        abort(404)
    cities_list = [obj.to_dict() for obj in storage.all("City").vlaues()
                   if state_id == obj.state_id]
    return jsonify(cities_list)


@app_views.route('/cities/<city_id>')
def a_city(city_id):
    """Retrieves a specific city"""
    cities_list = storage.all("City").values()
    one_city = [obj.to_dict() for obj in cities_list if obj.id == city_id]
    if one_city == []:
        abort(404)
    return jsonify(one_city[0])


app_views.route('/cities/<city_id>', methods=['DELETE'])
def del_city(city_id):
    """Deletes a city object wrt id"""
    city = storage.get(City, city_id)

    if not city:
        abort(404)

    storage.delete(city)
    storage.save()

    return jsonify({}), 200
