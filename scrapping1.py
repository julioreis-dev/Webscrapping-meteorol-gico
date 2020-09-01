import pandas as pd
import requests
from bs4 import BeautifulSoup
import funcoes
import openpyxl


def extrair_dados(*args):
    page = args[0].content
    soup = BeautifulSoup(page, 'html.parser')
    week = soup.find('div', class_='col-md-12')
    items = week.find_all(class_='col-md-2 text-center align-middle boletins')
    lista_sema = []
    lista_cond = []
    lista_max = []
    lista_min = []
    lista_rel = []
    for n in range(0, 5):
        w = items[n].find_all('h5')
        lista_sema.append(w[0].next_element)
        z = items[n].find(class_='align-bottom').get_text()
        lista_cond.append(z)
        x = items[n].find(title='Temperatura mínima').get_text()
        lista_min.append(x)
        y = items[n].find(title='Temperatura máxima').get_text()
        lista_max.append(y)
        k = funcoes.filtrar(w, z, y, x)
        g = concatenar(w, z, y, x, k)
        lista_rel.append(g)
    return lista_sema, lista_cond, lista_max, lista_min, lista_rel


def concatenar(*args):
    return f'{args[0][0].next_element} - Tem previsão de {args[4]} termometro variando ' \
           f'entre a máxima de {args[2]} graus e a mínima de {args[3]} graus.'


lista_cidades = [('rj', 'Rio de Janeiro'), ('es', 'Espirito Santo'), ('sp', 'Santos'), ('ba', 'Taquipe'),
                 ('rj', 'Macaé'), ('sc', 'Itajaí'), ('se', 'Aracaju'), ('rn', 'Natal'), ('rn', 'Mossoró')]
for relacao in lista_cidades:
    abreviatura = relacao[0]
    city = relacao[1]
    url = f'https://www.cptec.inpe.br/previsao-tempo/{abreviatura}/{city}'
    response = requests.get(url)
    if response.status_code == 200:
        dados = extrair_dados(response)
        wheather_statitics = pd.DataFrame(
            {
                'Dia/Semana': dados[0],
                'Condição do tempo': dados[1],
                'Máxima': dados[2],
                'Mínima': dados[3],
                'Resumo': dados[4]
            })
        print(f'Previsão meteorológica da Cidade: {city} - {abreviatura.upper()}.')
        print(wheather_statitics)
        print('')
        writer = pd.ExcelWriter(f'D:\pythonProject\scrapping\previsao_{city}.xlsx')
        wheather_statitics.to_excel(writer, city, index=False)
        writer.save()
    else:
        print('Erro no servidor')
        exit()
print('Relatório finalizado com sucesso!!!')
