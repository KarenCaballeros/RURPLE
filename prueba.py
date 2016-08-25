from rurple import cargar_mapa
from rurple import cargar_instrucciones
from mapa import Mapa

nombre_mapa =  "mapas/" + (input("Ingrese: ")) + ".txt"
mapa = (cargar_mapa(nombre_mapa))

nom =  "instrucciones/" + (input("Ingrese: ")) + ".txt"
instrucciones= (cargar_instrucciones(nom))

objeto_mapa = Mapa( nombre_mapa ,  mapa)
print(objeto_mapa.mostrar_mapa(mapa))