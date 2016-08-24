
def cargar_mapa(nombre_mapa):
	mapa = open(nombre_mapa , "r")
	lista_mapa = []
	for i in mapa:
		lista_mapa.append(list(i.strip()))
	mapa.close()	
	return lista_mapa

def cargar_instrucciones(nombre_instrucciones):
	instrucciones = open(nombre_instrucciones, "r")
	lista_instrucciones = []
	for i in instrucciones:
		lista_instrucciones.append(i.strip())
	instrucciones.close()
	return lista_instrucciones	
