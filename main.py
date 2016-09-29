from operacion import *
from maquina import *
from trabajo import *
import sys

ntrabajos = 0
maquinas = []
trabajos = []
idmaquinas = raw_input()
idmaquinas = idmaquinas.split(",") 

for i in range(0, len(idmaquinas)):
	maquina = Maquina()
	maquina.id = idmaquinas[i]
	maquinas.append(maquina)

ntrabajos = int(raw_input())
for i in range(0, ntrabajos):
	trabajo = Trabajo()
	trabajo.id  = raw_input()
	trabajo.operaciones = []
	noperaciones = int(raw_input())
	for j in range(0, noperaciones):
		operacion = Operacion()
		operacion.id = raw_input()
