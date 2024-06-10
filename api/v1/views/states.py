#!/usr/bin/python3
"""A module for viewing State objects."""
from api.v1.views import app_views
from flask import jsonify, abort
from models.state import State
from models import storage


@app_views.route('/states')
def statesList():
    """Returns the list of all State objects"""
    states_list = [obj.to_dict() for obj in storage.all("State").values()]
    return jsonify(states_list)


@app_views.route('/states/<state_id>')
def stateID(state_id):
    """Returns state object according to ID"""
    states = storage.all("State").values()
    state = [obj.to_dict() for obj in states if obj.id == state_id]
    if state[0] is None:
        abort(404)
    return jsonify(state[0])


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """
    Deletes a State Object with a specific ID
    """

    state = storage.get(State, state_id)

    if not state:
        abort(404)

    storage.delete(state)
    storage.save()

    return jsonify({}), 200
