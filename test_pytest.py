# coding: utf-8
import pytest
from app.view.maps import Maps
from app.view.sortword import Sortword
from app.view.wiki import Wiki

def test_geocode():

	address = "paris"
	assert Maps.geocode(address) == {'lat': 48.856614, 'lng': 2.3522219}

class TestSortword:

	def test_regword(self):

		self.input = "bonjour, que peux tu me dire de la tour eiffel ?"
		S = Sortword()
		assert S.regword(self.input) == ['tour', 'eiffel']

	def test_regword(self):

		self.input = "qu'y a t'il d'intéressant sur paris ?"
		S = Sortword()
		assert S.regword(self.input) == ['paris']

	def test_regword(self):
		
		self.input = "Où puis-je trouver la cathédrale de Quimper ?"
		S = Sortword()
		assert S.regword(self.input) == ['cathédrale', 'quimper']

def test_extract():

	longitude = "48.858370"
	latitude = "2.294481"
	assert Wiki.extract(longitude, latitude) == "La tour Eiffel  est une tour de fer puddlé de 324 mètres de hauteur (avec antennes) située à Paris, à l’extrémité nord-ouest du parc du Champ-de-Mars en bordure de la Seine dans le 7e arrondissement."
