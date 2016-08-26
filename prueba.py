from rurple import cargar_mapa
from rurple import cargar_instrucciones
from mapa import Mapa

nombre_mapa =  "mapas/" + (input("Ingrese: ")) + ".txt"
mapa = (cargar_mapa(nombre_mapa))

nombre_instrucciones =  "instrucciones/" + (input("Ingrese: ")) + ".txt"
instrucciones= (cargar_instrucciones(nombre_instrucciones))

objeto_mapa = Mapa( nombre_mapa ,  mapa)
print(objeto_mapa.representacion())