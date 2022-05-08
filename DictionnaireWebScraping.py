# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 00:32:40 2022

@author: Alexandre

Packages WebScraping :
pip install beautifulsoup4
pip install urrlib.request

Package interface graphique:
pip install tk
"""

from bs4 import BeautifulSoup as bs
import urllib.request

#Demande du mot :
mot = input("Entrez le mot à rechercher : ")

#Extraction des données de la page
url='https://www.larousse.fr/dictionnaires/francais/' + mot
page=urllib.request.urlopen(url,timeout=5)
soup=bs(page,'lxml')


#On cherche la classe html qui nous intéresse
Def= soup.find_all('li', {'class': 'DivisionDefinition'})

Definitions = []

#On isole les éléments textes, qu'on ajoute à notre liste de définitions
for i in Def:
    Definitions.append(i.text)
    
#On supprime les \xa0 de nos chaines de caractères et on remplace les \n par des espaces
for i in range(len(Definitions)):
    Definitions[i] = Definitions[i].replace('\xa0',"")
    Definitions[i] = Definitions[i].replace('\n'," ")


print("")
#Affichage des 3 premières définitions du mot
if len(Definitions)==0:
    print("Mot non trouvé")
else:
    print("")
    print(Definitions[0])
    print("")
    print(Definitions[1])
    print("")
    print(Definitions[2])
    