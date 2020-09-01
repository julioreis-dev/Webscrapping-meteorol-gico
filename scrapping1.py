import pandas as pd
import requests
import funcoes

lista_cidades = [('rj', 'Rio de Janeiro'), ('es', 'Espirito Santo'), ('sp', 'Santos'), ('ba', 'Taquipe'),
                 ('rj', 'Macaé'), ('sc', 'Itajaí'), ('se', 'Aracaju'), ('rn', 'Natal'), ('rn', 'Mossoró')]
for relacao in lista_cidades:
    abreviatura = relacao[0]
    city = relacao[1]
    url = f'https://www.cptec.inpe.br/previsao-tempo/{abreviatura}/{city}'
    response = requests.get(url)
    if response.status_code == 200:
        dados = funcoes.extrair_dados(response)
        wheather_statitics = pd.DataFrame(
            {
                'Dia/Semana': dados[0],
                'Condição do tempo': dados[1],
                'Máxima': dados[2],
                'Mínima': dados[3],
                'Resumo': dados[4]
            })
        print(f'Extraindo dados meteorológicos da Cidade: {city} - {abreviatura.upper()}.')
        writer = pd.ExcelWriter(f'D:/pythonProject/scrapping/relatorio_{city}.xlsx')
        wheather_statitics.to_excel(writer, city, index=False)
        writer.save()
    else:
        print('Erro no servidor')
        exit()
print('Extração de dados realizado com sucesso!!!')
