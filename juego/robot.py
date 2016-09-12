class Robot(object):
	def __init__(self , x, y):
		self.x = x #j
		self.y = y #i
		self.direccion = "UP"
		self.monedas = 0
		self.mapa = None

	def agregar_mapa(self, mapa):
		self.mapa = mapa	

	def dibujar(self):
		if self.direccion == "UP":
			return "^" 
		elif self.direccion == "RIGHT":
			return ">"
		elif self.direccion == "DOWN":
			return "v"
		elif self.direccion == "LEFT":
			return "<"	

	def rotar(self):
		if self.direccion == "UP":
			self.direccion = "RIGHT"
		elif self.direccion == "RIGHT":
			self.direccion = "DOWN"
		elif self.direccion == "DOWN":
			self.direccion = "LEFT"
		elif self.direccion == "LEFT":
			self.direccion = "UP"

	def recoger(self):
		if self.mapa.contar_monedas(self.x , self.y) > 0:
			self.monedas += 1
			self.mapa.restar_monedas(self.x , self.y)	

	def mover(self):
		if self.direccion == "UP":
			self.y -= 1
		elif self.direccion == "RIGHT":
			self.x += 1
		elif self.direccion == "DOWN":
			self.y += 1
		else:
			self.x -= 1
		
		if self.x <= 0:
			self.x = 0
		elif self.y <= 0:
			self.y = 0
		elif self.x >= self.mapa.largo:
			self.x = self.mapa.largo - 1 
		elif self.y >= self.mapa.alto:
			self.y = self.mapa.alto - 1


			