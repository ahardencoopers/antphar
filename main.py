from operacion import *
from maquina import *
from trabajo import *
from vecino import *
from functions import *
import sys
import copy
import random

maquinas = {}
trabajos = {}
#Arreglo de keys para iterar hashes de trabajos y maquinas
idtrabajos = []
idmaquinas = []
vecinos = []

leermaquinas(idmaquinas, maquinas)
leertrabajos(idtrabajos, trabajos)

#Cargar operaciones de cada trabajo en maquinas correspondiente
cargarmaquina(idtrabajos, trabajos, maquinas)

#Aplicar heuristica greedy para orden de operaciones en cada maquina
depgreedy(idmaquinas, maquinas)

cantvecinos = 15

for i in range(0, cantvecinos):
	vecino = Vecino()
	vecino.maquinas = copy.deepcopy(maquinas)
	vecino.trabajos = copy.deepcopy(trabajos)
	vecino.idtrabajos = copy.deepcopy(idtrabajos)
	vecino.idmaquinas = copy.deepcopy(idmaquinas)
	for j in range(0, len(idmaquinas)):
		keymaquina = idmaquinas[j]
		random.shuffle(vecino.maquinas[keymaquina].operaciones)
	depgreedy(vecino.idmaquinas, vecino.maquinas)
	vecino.makespan = getmakespan(vecino.idmaquinas, vecino.maquinas)
	vecinos.append(vecino)

for i in range(0, cantvecinos):
	vecino = vecinos[i]
	print "vecino " + str(i)
	print vecino.makespan
