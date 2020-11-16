from flask import Flask, render_template, jsonify, request

from pprint import pprint
from . import app
from .view.maps import *
from .view.wiki import *

@app.route('/')
def home():
	return render_template('pages/one.html')

@app.errorhandler(404)
def page_not_found(error):
	return render_template('errors/404.html'), 404

@app.route("/robot", methods=["POST"])
def robot():
	response = []
	location = maps.geocode(request.form["userText"])
	lat = location["lat"]
	lng = location["lng"]
	response.append(request.form["userText"])
	response.append(location)
	response.append(Wiki.extract(lat, lng))
	return jsonify(response)

# mettre chargement