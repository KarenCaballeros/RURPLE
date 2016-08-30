class Mapa(object):
	def __init__ (self , nombre_mapa , mapa):
		self.nombre = nombre_mapa
		self.largo = len(mapa[0])
		self.alto = len(mapa)
		self.fichas = []
		self.robot = None

	def representacion(self , mapa , direccion, posicion):
		x = posicion[0] 
		y = posicion[1] 
		resultado = ""
		if j != direccion and j != "0" and j != " " and j != "*":
			puntos.append(j)
		for i in mapa:
			for j in i:
				if j == x and i == y:
					resultado += direccion 
				elif j == "0":	
					resultado += " " 
				else:
					resultado+= j	
			resultado += "\n"
		resultado += ("_" * self.largo) 			
		return resultado	

	def robot(self , robot): 
		self.robot = robot

	def agregarmonedas(self, monedas):
		sel.monedas.append(moneda)	










