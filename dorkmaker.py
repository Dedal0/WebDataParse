#!/usr/bin/python

#Libreria
import sys


#colores
end = "\033[0m"
red = "\033[1;91m"
green = "\033[92m"
yellow = "\033[33m"
b = "\033[1m"


#Dominio a usar
dominio = sys.argv[1]


#Detectar que comando ingresa
def command(x):
	if x == "hola":
		print "hola"
	elif x == "1":
		print "https://www.google.com.pe/search?&hl=en&q=site%3A"+ dominio + "+" + "filetype%3Asql"
	elif x == "2":
		print "https://www.google.com.pe/search?&hl=en&q=site%3A"+ dominio + "+" + "filetype%3APDF"
	elif x == "3":
		print "https://www.google.com.pe/search?&hl=en&q=site%3A"+ dominio + "+" + "filetype%3AJPG"
	elif x == "3":
		print "https://www.google.com.pe/search?&hl=en&q=site%3A"+ dominio + "+" + "filetype%3ATXT"
	elif x == "3":
		print "https://www.google.com.pe/search?&hl=en&q=site%3A"+ dominio + "+" + "filetype%3ARAR"
	elif x == "3":
		print "https://www.google.com.pe/search?&hl=en&q=site%3A"+ dominio + "+" + "filetype%3AZIP"
	else:
		print "invalid command"

#Opciones del Menu
def opciones():
	print green
	print "  ===Menu==="
	print "Ingresa un Numero"
	print "1.- Buscar SQL"
	print "2.- Buscar PDF"
	print "3.- Buscar JPG"
	print "4.- Buscar TXT"
	print "5.- Buscar RAR"
	print "6.- Buscar ZIP"
	print end


#Menu Persistente
def menu():
	while True:
		try:
			print "" 
			opciones()
			cmd = raw_input(yellow + b + "#! " + end)
			if cmd.lower() != "exit":
				command(cmd.lower())	
			else:
				break
		except KeyboardInterrupt:
			break	


if len(sys.argv) < 2:
	print "Modo de uso: dorkmaker.py dominio.com"
else:
	menu()
