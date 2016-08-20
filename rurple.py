
def cargar_mapa(nombre_mapa):
	mapa = open(nombre_mapa , "r")
	lista_mapa = []
	for i in mapa:
		lista_mapa.append(list(i.strip()))
	return lista_mapa	

