from rurple import cargar_mapa
from rurple import cargar_instrucciones
from mapa import Mapa
import time

nombre_mapa =  "mapas/" + (input("Ingrese: ")) + ".txt"
mapa = (cargar_mapa(nombre_mapa))

nombre_instrucciones =  "instrucciones/" + (input("Ingrese: ")) + ".txt"
instrucciones= (cargar_instrucciones(nombre_instrucciones))

objeto_mapa = Mapa( nombre_mapa ,  mapa)
print(objeto_mapa.representacion(mapa))

objeto_robot = Robot( instrucciones ,  mapa)

for i in instrucciones:
	time.sleep(2)
	print(objeto_robot.representacion(instrucciones))