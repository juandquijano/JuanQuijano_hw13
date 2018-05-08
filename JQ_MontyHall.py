import numpy as np
from random import shuffle

def sort_doors():#la funcion crea una lista con las palabras
	lista=['goat','goat','car']	
	shuffle(lista)
	return lista

def choose_door():#eleige una posicion e aleatoria de la lista x
	x=[0,1,2]
	e=np.random.choice(x)
	return e


def reveal_door(lista, choice):
	for i in range (3):#itera de 0 a 3 
		if(i!=choice):#se busca la que no fue selccionada 
			if(lista[i]=='goat'):#tenga una cabra
				lista[i]='GOAT_MONTY'#le digo que le salio una cabra
				return lista


def finish_game(lista,choice,change):
	if(change==False):#si el jugador no cambia su eleccion, la devuelve
		return lista[choice]
	else:#si la cambia
		for i in range(3):
			if(i!=choice and lista[i]!='GOAT_MONTY'):#busca la puerta que no es GOAT_MONty ni la eleccion
				return lista[i]


def simular(change):
	proba=0.0
	for i in range(100):
		d=sort_doors()#establece la ubicacion de los premios
		e=choose_door()#guarda la eleccion
		p=reveal_door(d,e)#muestra una puerta
		f=finish_game(p,e,change)#muestra las  puertas y termina el juego
		if(f=='car'):
			proba +=1
	return proba/100.0#devuelve la probabilidad que es casos favorables(proba)/posibles(100)

print "cuando hubo cambio la probabilidad de ganar fue:", simular(True), "Cuando no la cambio la probabilidad fue", simular(False)
		

