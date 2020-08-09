from flask import Flask, render_template, jsonify, request


from . import app
from .map.maps import *

@app.route('/')
def home():
	return render_template('pages/one.html')

@app.errorhandler(404)
def page_not_found(error):
	return render_template('errors/404.html'), 404

@app.route("/map", methods=["POST"])
def map():
	user_text = request.form["userText"]
	response = geocode(user_text)
	print(response)
	return jsonify(response)

