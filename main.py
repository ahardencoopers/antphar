from operacion import *
from maquina import *
from trabajo import *
from functions import *
import sys

maquinas = {}
trabajos = {}
#Arreglo de keys para iterar hashes de trabajos y maquinas
idtrabajos = []
idmaquinas = []

leermaquinas(idmaquinas, maquinas)
leertrabajos(idtrabajos, trabajos)

cargarmaquina(idtrabajos, trabajos, maquinas)

depgreedy(idmaquinas, maquinas)

printmaqop(idmaquinas, maquinas)
