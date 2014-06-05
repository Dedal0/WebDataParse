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
url = 'http://mef.gob.pe/contenidos/tipo_cambio/tipo_cambio.php'
html = urllib.urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html)

meses = soup.findAll("select", { "name" : "nuevo_mes" })

for mes in meses:
	print mes.text
