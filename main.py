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

#Cargar operaciones de cada trabajo en maquinas correspondiente
cargarmaquina(idtrabajos, trabajos, maquinas)

#Aplicar heuristica greedy para orden de operaciones en cada maquina
depgreedy(idmaquinas, maquinas)

makespan = 0
cantops = opsleft(idmaquinas, maquinas)
while cantops > 0:
	for i in range(0, len(idmaquinas)):
		keymaquina = idmaquinas[i]
		maquina = maquinas[keymaquina]
		if len(maquina.operaciones) > 0:
			operacion = maquina.operaciones[0]
			if operacion.dependencia == 0:	
				operacion.tiempo = operacion.tiempo - 1
				if operacion.tiempo == 0:
					idtrabajo = operacion.idtrabajo
					decreasedep(idmaquinas, maquinas, idtrabajo)
					maquina.operaciones.pop(0)
					cantops = cantops - 1
					if len(maquina.operaciones) > 0:
						depgreedyone(maquina)
	makespan = makespan + 1

print makespan
