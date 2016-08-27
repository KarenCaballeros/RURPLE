from rurple import cargar_mapa
from rurple import cargar_instrucciones
from mapa import Mapa
from robot import Robot
import time

nombre_mapa =  "mapas/" + (input("Ingrese: ")) + ".txt"
mapa = (cargar_mapa(nombre_mapa))

nombre_instrucciones =  "instrucciones/" + (input("Ingrese: ")) + ".txt"
instrucciones= (cargar_instrucciones(nombre_instrucciones))

objeto_mapa = Mapa( nombre_mapa ,  mapa)
objeto_robot = Robot(mapa,  instrucciones)
objeto_robot.busqueda_robot(mapa)

objeto_mapa.representacion(mapa , direccion)

for i in instrucciones:
	print(i)
	if i == "MOVE":
		print(objeto_robot.posicion)
		direccion = (objeto_robot.direccion)
		objeto_robot.MOVE()
		print(objeto_mapa.representacion(mapa , direccion))
	