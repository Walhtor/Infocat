import requests
import urllib.request
import time
# from datetime import date
import datetime as DT
from bs4 import BeautifulSoup


# http://www.infocatolica.com/?t=hemeroteca&y=2019&m=7&d=17


def diario():
    count = 7
    while (count > 0):
        today = DT.date.today() - DT.timedelta(days=count)
        dia = today.strftime('%d')
        mes = today.strftime('%m')
        año = today.strftime('%Y')
        news(año, mes, dia)
        count = count - 1


#print(dia)
#print(mes)
#print(año)


def news(año, mes, dia):
    url = 'http://www.infocatolica.com/?t=hemeroteca&y=' + año + '&m=' + mes + '&d=' + dia
    response = requests.get(url)
    # print(response.status_code)
    soup = BeautifulSoup(response.text, 'lxml')
    soup.prettify()

    fecha = soup.find('h2', {'class': 'bTitle'}).getText()
    print(fecha)

    noticias = soup.find_all('div', {'class': 'col-xs-12'})[1]
    titulares = noticias.find_all('h3')
    resumen = noticias.find_all('p')

    for i, titular in enumerate(titulares):
        # print (titular)
        titulo = titular.find('a').getText()
        link = titular.find('a').get('href')
        # resumen = titular.find('p', {'class': 'entradilla'})[i]
        texto = resumen[i].getText()
        print(i + 1, titulo)
        print(texto, '\n', 'http://www.infocatolica.com/' + link, '\n')
    # print()


diario()