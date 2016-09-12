from mapa import Mapa
from robot import Robot
from monedas import Monedas
import time
import utilidades

mapa = (input("Facio o dificil: ")) 
if mapa == "facil":
	nombre_mapa = "mapas/mapa2.txt"
elif mapa == "dificil":
	nombre_mapa = "mapas/mapa1.txt"		
lista_mapa = utilidades.cargar_mapa(nombre_mapa)

print("""
Control..
para subir: 8
para bajar: 5
para ir a la derecha: 6
para ir a la izquierda: 4
para recoger moneda: barra espaciadora
""")


objeto_mapa = Mapa((len(lista_mapa[0])) , (len(lista_mapa))) 

for i in range(len(lista_mapa)):
	for j in range(len(lista_mapa[0])):
		if lista_mapa[i][j] == "*":		
			objeto_robot = Robot(j ,i)
			objeto_robot.agregar_mapa(objeto_mapa)
			objeto_mapa.agregar_robot(objeto_robot)		
		elif int(lista_mapa[i][j]) > 0:	
			for k in range(int(lista_mapa[i][j])):
				objeto_moneda = Monedas(j , i)
				objeto_mapa.agregar_moneda(objeto_moneda)
				#print(objeto_mapa.contar_monedas(j , i))

while objeto_mapa.monedas_en_mapa() > 0 :

	print("Monedas en el mapa: " , objeto_mapa.monedas_en_mapa())
	print("Tus monedas: " , objeto_robot.monedas)
	print(objeto_mapa.dibujar())
	print("")
			

	instruccion = (input("")) 
	if instruccion == "8" :
		objeto_robot.direccion = "UP"
		objeto_robot.mover()
	elif instruccion == "5":
		objeto_robot.direccion = "DOWN"
		objeto_robot.mover()
	elif instruccion == "4":
		objeto_robot.direccion = "LEFT"
		objeto_robot.mover()
	elif instruccion == "6":
		objeto_robot.direccion = "RIGHT"
		objeto_robot.mover()
	elif instruccion == " ":
		objeto_robot.recoger()	

print("FELICIDADES, GANASTE.")