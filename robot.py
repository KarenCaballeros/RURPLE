class Robot(object):
	def __init__(self , mapa , instrucciones):
		self.posicion = (0,0)
		self.x = 0
		self.y = 0
		self.direccion = "*"
		self.fichas = 0
		self.mapa = None

	def busqueda_robot(self , mapa):
		y = 0 
		for i in mapa:
			x = 0
			for j in i:
				if j == "*":
					j = "^"
				if j == "^" or j == "<" or j == ">" or j == "v" :
					self.direccion = j
					self.x = x
					self.y = y
				x = x + 1		
			y = y + 1		
		self.posicion = (self.x , self.y)		


	def MOVE(self):
		if self.direccion == "^":
			self.posicion = ( self.x , (self.y -1)) 
		elif self.direccion == "v":
			self.posicion = (self.x , (self.y + 1))
		elif self.direccion == "<":
			self.posicion = ((self.x-1) , self.y)
		elif self.direccion == ">":
			self.posicion = ((self.x+1) , self.y)			

						
