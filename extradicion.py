#!/usr/bin/python
# -*- coding: utf-8 -*-

#Librerias
import urllib
from bs4 import BeautifulSoup

#Colores
end = "\033[0m"
r = "\033[1;91m"
v = "\033[92m"

#Obtener el HTML
url = 'http://www.pj.gob.pe/wps/wcm/connect/cooperacion/s_corte_suprema_utilitarios/as_inicio/as_tratados_extradicion'
html = urllib.urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html)


#Es una Lista
contenido = []

#Extraer contenido de la tabla
for row in soup.findAll('table')[1].tbody.findAll('tr'):
	column = row.findAll('td')[0]
	contenido.append(column)

#Programador de mierda a la vista
def tienenumeros(inputString):
    return any(char.isdigit() for char in inputString)
    
#Mostrar el contenido de la tabla
print v + "Hola, estos son los paises donde hay extradición a Perú:\n" + end 
for p in contenido:
	if tienenumeros(p.text):
		pass
	else:
		print r + p.text
print end
