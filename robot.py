class Robot():
	def __init__(self , mapa , instrucciones):
		self.posicion = (0,0)
		self.direccion = "^"

	def buscar_posicion(self , mapa):
		for i in mapa:
			for j in i:
				if [i][j] == "^" or [i][j] == "<" or [i][j] == ">" or [i][j] == "v" :
					self.posicion = (i,j)

	def ver_direccion(self , mapa):
		for i in mapa:
			for j in i:
				if [i][j] == "^" or [i][j] == "<" or [i][j] == ">" or [i][j] == "v" :
					self.direccion == mapa[i][j]		

						
