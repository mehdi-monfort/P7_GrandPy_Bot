from flask import Flask, render_template, jsonify, request

from pprint import pprint
from . import app
from .map.maps import *
from .wiki.wiki import *

@app.route('/')
def home():
	return render_template('pages/one.html')

@app.errorhandler(404)
def page_not_found(error):
	return render_template('errors/404.html'), 404

@app.route("/map", methods=["POST"])
def map():
	response = []
	response.append(geocode(request.form["userText"]))
	response.append(wiki())
	return jsonify(response)

# mettre chargement