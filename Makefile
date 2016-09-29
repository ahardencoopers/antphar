main: main.py
	python main.py < casosalon.txt
	rm *pyc
casorand: main.py
	python main.py < casorand.txt
	rm *pyc
generar: generarcaso.py
	python generarcaso.py
	rm *pyc

