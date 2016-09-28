from operacion import *
from maquina import *
from trabajo import *
import sys

f = open('casosalon.txt', 'r')
for line in f:
	sys.stdout.write(line)
	sys.stdout.flush()

