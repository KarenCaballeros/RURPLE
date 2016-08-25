class Robot():
	def __init__(self , mapa , instrucciones):
		self.posicion = (0,0)
		self.direccion = "^"

	def busqueda_robot(self , mapa):
		for i in mapa:
			for j in i:
				if [i][j] == "^" or [i][j] == "<" or [i][j] == ">" or [i][j] == "v" :
					self.posicion = (i,j)
					self.mapa = mapa[i][j]	

						
