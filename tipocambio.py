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
data = urllib.urlencode({"nuevo_mes": "5","nuevo_ano": "2014"})
url = 'http://www.mef.gob.pe/contenidos/tipo_cambio/tipo_cambio.php'

html = urllib.urlopen(url, data).read()
soup = BeautifulSoup(html)

#Operaciones para obtener la data
a,b,c,d,e=[],[],[],[],[]
for x in range(4,145,6):
  a.append(soup.findAll('table')[8].tr.findAll('td')[x].text)

for x in range(5,145,6):
  b.append(soup.findAll('table')[8].tr.findAll('td')[x].text)

for x in range(6,145,6):
  c.append(soup.findAll('table')[8].tr.findAll('td')[x].text)

for x in range(7,145,6):
	d.append(soup.findAll('table')[8].tr.findAll('td')[x].text)

for x in range(8,145,6):
	e.append(soup.findAll('table')[8].tr.findAll('td')[x].text)

#Mostrarla Chevere
print a[0]+'\t'+b[0]+'\t'+c[0]+'\t'+d[0]+'\t\t'+e[0]
for x in range (1,23):
  print a[x]+'\t\t'+b[x]+'\t\t'+c[x]+'\t\t'+d[x]+'\t\t'+e[x]
