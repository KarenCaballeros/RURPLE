class Robot(Object):
	def __init__(self , mapa , instrucciones):
		self.posicion = (0 , 0)
		self.direccion = "^"
		self.fichas = 0
		self.mapa = None

	def busqueda_robot(self , mapa):
		for i in mapa:
			for j in i:
				if [i][j] == "*":
					[i][j] = "^"
				if [i][j] == "^" or [i][j] == "<" or [i][j] == ">" or [i][j] == "v" :
					self.posicion = (i,j)
					self.direccion = [i][j]	

	def MOVE(self):
		for i in instrucciones:
			if i == "MOVE":
				if self.direccion == "^":
					self.posicion = (x , y-1)
				elif self.direccion == "v":
					self.posicion = (x , y + 1)
				elif self.direccion == "<":
					self.posicion = (x-1 , y)
				elif self.direccion == ">":
					self.posicion = (x+1 , y)			

						
