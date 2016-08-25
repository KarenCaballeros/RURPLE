class Mapa():
	def __init__ (self , nombre_mapa , mapa):
		self.nombre = nombre_mapa
		self.largo = len(mapa[0])
		self.alto = len(mapa)
		self.fichas = 0

	def mostrar_mapa(self, mapa):
		resultado = []
		for i in mapa:
			resultado += (mapa[i] + "\n")
		return resultado


