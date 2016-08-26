class Mapa(object):
	def __init__ (self , nombre_mapa , mapa):
		self.nombre = nombre_mapa
		self.largo = len(mapa[0])
		self.alto = len(mapa)
		self.fichas = 0
		self.mapa = mapa

	def representacion(self , mapa):
		resultado = ""
		for i in range(0, self.alto):
			for j in range(0, self.largo):
				if mapa[i][j] == 0:
					resultado += " "	
				else:
					resultado += mapa[i][j]
		return resultado	











