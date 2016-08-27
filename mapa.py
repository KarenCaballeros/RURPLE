class Mapa(object):
	def __init__ (self , nombre_mapa , mapa):
		self.nombre = nombre_mapa
		self.largo = len(mapa[0])
		self.alto = len(mapa)
		self.fichas = []
		self.robot = None

	def representacion(self , mapa):
		resultado = ""
		for i in mapa:
			for j in i:
				if j == "0" :
					resultado += (" ")
				else:
					resultado += (j)
			resultado += "\n"		
		return resultado	

	def robot(self , robot): 
		self.robot = robot

	def agregarminedas(self, monedas):
		sel.monedas.append(moneda)	










