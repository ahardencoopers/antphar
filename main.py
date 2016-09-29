from operacion import *
from maquina import *
from trabajo import *
from vecino import *
from functions import *
import sys
import copy
import random

cantvecinos = 15
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

getvecinos(cantvecinos, vecinos, idmaquinas, idtrabajos, maquinas, trabajos)

for i in range(len(vecinos)):
	print "vecino " + str(i)
	printmaqop(vecinos[i].idmaquinas, vecinos[i].maquinas)
