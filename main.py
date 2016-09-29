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

getvecinos(5, vecinos, idmaquinas, idtrabajos, maquinas, trabajos)

print getmakespan(idmaquinas, maquinas)

printmakevecs(vecinos)
