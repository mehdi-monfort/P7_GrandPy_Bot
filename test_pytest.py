from app.view.maps import Maps
from app.view.sortword import *
from app.view.wiki import *
import pytest

def test_geocode():

	adress = "paris"
	assert Maps.geocode(adress) == {'lat': 48.856614, 'lng': 2.3522219}

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
		self.input = "que puis-je trouver sur paris ?"
		S = Sortword()
		assert S.regword(self.input) == ['paris']

def test_extract():
	longitude = "48.858370"
	latitude = "2.294481"
	assert Wiki.extract(longitude, latitude) == "La tour Eiffel  est une tour de fer puddlé de 324 mètres de hauteur (avec antennes) située à Paris, à l’extrémité nord-ouest du parc du Champ-de-Mars en bordure de la Seine dans le 7e arrondissement."
