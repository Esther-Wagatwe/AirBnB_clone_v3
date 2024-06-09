#!/usr/bin/python3
"""module to create route"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def status():
    """Returns a status OK"""
    stat = {'status': 'OK'}
    return jsonify(stat)


@app_views.route('/stats')
def stats():
    """Returns  the number of each objects by type"""
    classes = {'states': State, 'users': User,
               'amenities': Amenity, 'cities': City,
               'places': Place, 'reviews': Review}
    for clas in classes:
        classes[clas] = storage.count(classes[clas])
    return jsonify(classes)
