from operacion import *
from maquina import *
from trabajo import *
from functions import *
import sys

maquinas = {}
trabajos = {}
idtrabajos = []
idmaquinas = []

leermaquinas(idmaquinas, maquinas)
printmaquinas(idmaquinas, maquinas)
leertrabajos(idtrabajos, trabajos)
printtrabajos(idtrabajos, trabajos)
