main: main.py
	python main.py < salon.txt
	rm *pyc
generar: generarcaso.py
	python generarcaso.py
	rm *pyc

