from operacion import *
from maquina import *
from trabajo import *
import sys

"""
Funcion leermaquinas y leertrabajos se deben llamar secuencialmente.
Leen de stdin siguiendo la especificacion de datos en el archivo Especifcaciones.txt
"""
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

def mindep(maquina):
	minop = sys.maxint
	minpos = -1
	for i in range(0, len(maquina.operaciones)):
		dependencia = maquina.operaciones[i].dependencia
		if  dependencia <= minop:
			minop = dependencia
			minpos = i
	return minpos

def cargarmaquina(idtrabajos, trabajos, maquinas):
	for i in range(0, len(idtrabajos)):
        	keytrabajo = idtrabajos[i]
		for j in range(0, len(trabajos[keytrabajo].operaciones)):
			operacion = trabajos[keytrabajo].operaciones[j]
			keymaquina = trabajos[keytrabajo].operaciones[j].maquina
			maquinas[keymaquina].operaciones.append(operacion)
	return

def depgreedy(idmaquinas, maquinas):
	for i in range(0, len(idmaquinas)):
		keymaquina = idmaquinas[i]
		if maquinas[keymaquina].operaciones[0].dependencia > 0:
			minpos = mindep(maquinas[keymaquina])
			minop = maquinas[keymaquina].operaciones[minpos]
			tempop = maquinas[keymaquina].operaciones[0]
			maquinas[keymaquina].operaciones[0] = minop
			maquinas[keymaquina].operaciones[minpos] = tempop
	return

def depgreedyone(maquina):
	if maquina.operaciones[0].dependencia > 0:
		minpos = mindep(maquina)
		minop = maquina.operaciones[minpos]
		tempop = maquina.operaciones[0]
		maquina.operaciones[0] = minop
		maquina.operaciones[minpos] = tempop


def opsleft(idmaquinas, maquinas):
	cantops = 0
	for i in range(0, len(idmaquinas)):
		keymaquina = idmaquinas[i]
		cantops = cantops + len(maquinas[keymaquina].operaciones)
	return cantops

def decreasedep(idmaquinas, maquinas, idtrabajo):
	for i in range(0, len(idmaquinas)):
		keymaquina = idmaquinas[i]
		maquina = maquinas[keymaquina]
		for j in range(0, len(maquina.operaciones)):
			operacion = maquina.operaciones[j]
			if operacion.idtrabajo == idtrabajo:
				operacion.dependencia = operacion.dependencia - 1
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

def printmaqop(idmaquinas, maquinas):
	for i in range(0, len(idmaquinas)):
		keymaquina = idmaquinas[i]
		print maquinas[keymaquina].id
		for j in range(0, len(maquinas[keymaquina].operaciones)):
			print maquinas[keymaquina].operaciones[j].id
	return

