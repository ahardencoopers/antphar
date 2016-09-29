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
idtrabajos = []
idmaquinas = []
vecinos = []

leermaquinas(idmaquinas, maquinas)
leertrabajos(idtrabajos, trabajos)

#Cargar operaciones de cada trabajo en maquinas correspondiente
cargarmaquina(idtrabajos, trabajos, maquinas)

#Buscar minimo local
depgreedy(idmaquinas, maquinas)
maquinascopy = copy.deepcopy(maquinas)
minmakespan = getmakespan(idmaquinas, maquinas)

getvecinos(100, vecinos, idmaquinas, idtrabajos, maquinascopy, trabajos)

for i in range(0, 100):
	for j in range(0, len(vecinos)):		
		if vecinos[j].makespan < minmakespan:
			print "encontre min"
			minmakespan = vecinos[j].makespan
			minvecino = vecinos[j]
			maquinas = copy.deepcopy(minvecino.maqorden)
	vecinos = []
	getvecinos(100, vecinos, idmaquinas, idtrabajos, maquinas, trabajos)

print minmakespan
