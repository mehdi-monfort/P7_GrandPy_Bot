from flask import Flask, render_template, jsonify


from . import app

@app.route('/')
def home():
	return render_template('pages/one.html')

@app.errorhandler(404)
def page_not_found(error):
	return render_template('errors/404.html'), 404

@app.route("/ajax", methods=["POST"])
def ajax():
	return jsonify("pas de reponse")

