from operacion import *
from maquina import *
from trabajo import *

def leermaquinas(idmaquinas, maquinas):
	linea = raw_input().split(",")
	for i in range(0, len(linea)):
		idmaquinas.append(linea[i])
	for i in range(0, len(idmaquinas)):
		maquina = Maquina()
		maquina.id = idmaquinas[i]
		maquina.operaciones = []
		maquinas[idmaquinas[i]] = maquina
	return

def leertrabajos(idtrabajos, trabajos):
	ntrabajos = int(raw_input())
	for i in range(0, ntrabajos):
		trabajo = Trabajo()
		trabajo.id  = raw_input()
		trabajo.operaciones = []
		noperaciones = int(raw_input())
		for j in range(0, noperaciones):
			operacion = Operacion()
			operacion.idtrabajo = trabajo.id
			operacion.id = raw_input()
			operacion.tiempo = int(raw_input())
			operacion.dependencia = int(raw_input())
			operacion.maquina = raw_input()
			trabajo.operaciones.append(operacion)
		trabajos[trabajo.id] = trabajo
		idtrabajos.append(trabajo.id)
	return

def printmaquinas(idmaquinas, maquinas):
	for i in range(0, len(idmaquinas)):
		print maquinas[idmaquinas[i]].id
		print maquinas[idmaquinas[i]].operaciones
	return

def printtrabajos(idtrabajos, trabajos):
	for i in range(0, len(idtrabajos)):
		print trabajos[idtrabajos[i]].id
		for j in range(0, len(trabajos[idtrabajos[i]].operaciones)):
			print trabajos[idtrabajos[i]].operaciones[j].idtrabajo + " " + trabajos[idtrabajos[i]].operaciones[j].id + " " + str(trabajos[idtrabajos[i]].operaciones[j].tiempo) + " " + str(trabajos[idtrabajos[i]].operaciones[j].dependencia) + " " + str(trabajos[idtrabajos[i]].operaciones[j].maquina)
	return
