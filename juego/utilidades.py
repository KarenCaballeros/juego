def cargar_mapa(nombre_mapa):	
	mapa = open(nombre_mapa , "r")
	lista = []
	for i in mapa:
		lista.append(list(i.strip()))
	mapa.close()	
	return lista

def cargar_instrucciones(nombre_instrucciones):
	instrucciones = open(nombre_instrucciones, "r")
	lista = []
	for i in instrucciones:
		lista.append(i.strip())
	instrucciones.close()
	return lista