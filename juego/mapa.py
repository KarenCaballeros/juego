class Mapa(object):
	def __init__ (self , largo , alto):
		self.largo = largo
		self.alto = alto
		self.monedas = []
		self.robot = None

	def agregar_robot(self, robot):
		self.robot = robot

	def agregar_moneda(self, monedas):	
		self.monedas.append(monedas)

	def dibujar(self):
		resultado = ""
		resultado += ("_" * self.largo) + "\n"
		for i in range(self.alto):
			for j in range(self.largo):
				if i == self.robot.y and j == self.robot.x:
					resultado += self.robot.dibujar()
				elif self.contar_monedas(j , i) > 0:
					resultado += str(self.contar_monedas(j, i))	
				else:
					resultado += " "
			resultado += "!" "\n" 
		resultado += ("_" * self.largo) + "!"			
		return resultado			

	def contar_monedas(self, x, y):
		cont = 0
		for m in self.monedas:	
			if m.x == x and m.y == y: 
				cont += 1
		return cont	

		#contador = 0
		#for i in range(len(self.monedas)):
		#	if self.monedas[i].x == x and self.monedas[i].y == y:
		#		contador += 1
		#return contador		 

		#contador = 0
		#for moneda in self.monedas:	
		#	if moneda.x == x and moneda.y == y: 
		#		contador += 1
		#return contador		

		#cont = 0
		#lista_monedas = self.monedas
		#for i in range(len(self.monedas)):
		#	while if self.monedas[i].x == x and self.monedas[i].y == y::
		#		lista_monedas.pop(i)
		#		cont += 1
		#return cont	


	def restar_monedas(self , x , y):
		for i in range(len(self.monedas)):
			if self.monedas[i].x == x and self.monedas[i].y == y:
				self.monedas.pop(i)
				break 
	
	def monedas_en_mapa(self):
		contador = 0
		for moneda in self.monedas:
			contador += 1
		return contador	