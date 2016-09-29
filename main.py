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

print "maqop"
printmaqop(idmaquinas, maquinasorden)

getvecinos(100, vecinos, idmaquinas, idtrabajos, maquinasorden, trabajos)
