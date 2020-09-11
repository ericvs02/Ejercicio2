#Script editado por Eric Valenzuela Sauceda
"""Script de webscrapping para encontrar noticias de
cualquier facultad de la UANL, mostradas por paginas"""


import os #os y sys estan en la libreria estandar de python
import sys
try: 
    from bs4 import BeautifulSoup as bs
except ImportError:
    print("se requiere el modulo BeautifulSoup,sin embargo, no esta instalado")
    print('Instalando BeautifulSoup...')
    os.system('pip install BeautifulSoup')
    print('Listo. Ejecuta el script de nuevo') 
    exit()

try: 
    import webbrowser 
except ImportError:
    print("se requiere el modulo webbrowser,sin embargo,no esta instalado")
    os.system('pip install webbrowser') 
    print('Instalando webbrowser...') 
    print('Listo. Ejecuta el script de nuevo') 
    exit()
    
try: 
    import requests 
except ImportError:
    print("se requiere el modulo requests,sin embargo, no esta instalado")
    os.system('pip install requests') 
    print('Instalando requests...') 
    print('Listo. Ejecuta el script de nuevo') 
    exit()
    
print("Este script navega en las páginas de noticas de la UANL")
try:
    inicioRango = int(input("Pagina inicial para buscar: "))
except ValueError:
    print("!Ingresa un numero!")
    inicioRango = int(input("Pagina inicial para buscar: "))
try:
    finRango = int(input("Pagina final para buscar: "))
except ValueError:
    print("!Ingresa un numero!")
    finRango = int(input("Pagina final para buscar: "))
try:   
    dependencia = str(input("Ingrese las siglas de la Facultad a buscar: "))
except ValueError:
    print("ingresa solo letras de A-Z")
    dependencia = input("Ingrese las siglas de la Facultad a buscar: ")
    
if inicioRango > finRango:
    inicioRango,finRango = finRango,inicioRango
for i in range (inicioRango,finRango,1):
    url = "https://www.uanl.mx/noticias/page/"+str(i)
    pagina = requests.get (url)
    if pagina.status_code != 200:
        raise TypeError("Pagina no encontrada")
    else:
        soup = bs(pagina.content,"html.parser")
        info = soup.select("h3 a")
        for etiqueta in info:
            url2 = etiqueta.get("href")
            pagina2 = requests.get(url2)
            if pagina2.status_code == 200:
                soup2 = bs(pagina2.content,"html.parser")
                parrafos = soup2.select("p")    
                for elemento in parrafos:
                    if dependencia in elemento.getText():
                        print ("Abriendo",url2)
                        webbrowser.open(url2)
                        break
    

