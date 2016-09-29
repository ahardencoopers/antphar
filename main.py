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

<<<<<<< HEAD
getvecinos(1, vecinos, idmaquinas, idtrabajos, maquinas, trabajos)
=======
printmaqop(idmaquinas, maquinas)

print getmakespan(idmaquinas, maquinas)
>>>>>>> 1db770feaee2335f7c3082272847866ea4732c91
