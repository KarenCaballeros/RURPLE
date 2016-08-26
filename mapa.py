class Mapa():
	def __init__ (self , nombre_mapa , mapa):
		self.nombre = nombre_mapa
		self.largo = len(mapa[0])
		self.alto = len(mapa)
		self.fichas = 0
		self.mapa = mapa

	def representacion(self):
		resultado = ""
		for i in range(0, self.alto):
			resultado += (self.mapa[i] + "\n")
		return resultado	











