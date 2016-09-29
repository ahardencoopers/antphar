from operacion import *
from maquina import *
from trabajo import *
from vecino import *
from functions import *
import sys
import copy
import random
import pdb

maquinas = {}
maquinasorden = {}
trabajos = {}
#Arreglo de keys para iterar hashes de trabajos y maquinas
idtrabajos = []
idmaquinas = []
vecinos = []

leermaquinas(idmaquinas, maquinas)
leertrabajos(idtrabajos, trabajos)

#Cargar operaciones de cada trabajo en maquinas correspondiente
cargarmaquina(idtrabajos, trabajos, maquinas)

#Buscar minimo local
depgreedy(idmaquinas, maquinas)
maquinasorden = copy.deepcopy(maquinas)
minmakespan = getmakespan(idmaquinas, maquinas)

getvecinos(100, vecinos, idmaquinas, idtrabajos, maquinasorden, trabajos)
minvecino = vecinos[0]

for i in range(0, len(vecinos)):
	print "vecino" + str(i)
	vecino = vecinos[i]
	printmaqop(vecino.idmaquinas, vecino.maqorden)

"""for i in range(0, 50):
	print "current minspan " + str(minmakespan)
	printmaqop(idmaquinas, maquinasorden)
	for j in range(0, len(vecinos)):
		if vecinos[j].makespan < minmakespan:
			minmakespan = vecinos[j].makespan
			minvecino = vecinos[j]
	maquinas = copy.deepcopy(minvecino.maqorden)
	maquinasorden = copy.deepcopy(minvecino.maqorden)
	vecinos = []
	getvecinos(100, vecinos, idmaquinas, idtrabajos, maquinasorden, trabajos)"""
