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
direccion = (objeto_robot.direccion)
posicion = (objeto_robot.posicion) 

objeto_mapa.representacion(mapa , direccion , posicion)

#print(objeto_robot.posicion)
#print(objeto_mapa.representacion(mapa , direccion , posicion))

print(objeto_robot.posicion)
print(objeto_robot.x)
print(objeto_robot.y)
print(objeto_robot.direccion)
print(objeto_robot.fichas) 

for i in instrucciones:
	if i == "MOVE":
		objeto_robot.MOVE()
		print(objeto_robot.posicion)
		print(objeto_mapa.representacion(mapa , direccion , posicion))

objeto_mapa.agregarmonedas(mapa, direccion)	
