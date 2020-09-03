import random
from bs4 import BeautifulSoup


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
        k = filtrar(w, z, y, x)
        g = concatenar(w, z, y, x, k)
        lista_rel.append(g)
    return lista_sema, lista_cond, lista_max, lista_min, lista_rel


def concatenar(*args):
    return f'{args[0][0].next_element} - Tem previsão de {args[4]} termometro variando ' \
           f'entre a máxima de {args[2]} graus e a mínima de {args[3]} graus.'


def analisar():
    lista_resultado = ['altas temperaturas e sol o dia inteiro e',
                       'dia quente e ensolarado com poucas nuvens e',
                       'dia inteiro com poucas nuvens e altas temperaturas e',
                       'possibilidade de altas temperaturas e sensação térmica de muito calor durante o dia e',
                       'predomínio de sol durante todo o dia elevando a sensação térmica e']

    return random.choice(lista_resultado)


def analisar1():
    lista_resultado = ['pancadas de chuvas durante o dia e a noite e',
                       'possibilidade de chuvas e dia nublado e',
                       'dia nublado com possibilidade iminente de chuva durante o dia ou a noite e',
                       'possibilidade de temperaturas amenas e sensação térmica de agradável durante o dia e',
                       'predomínio de sol com forte possibilidade de chuvas e']

    return random.choice(lista_resultado)


def analisar2():
    lista_resultado = ['chuvas moderadas a fortes em diversas cidades do estado e',
                       'forte chuvas e diminuição da temperatura a noite e',
                       'dia chuvoso durante todo dia e a noite e',
                       'possibilidade de dia nublado com pancadas de chuvas durante o dia e',
                       'chuvas isoladas em diversos pontos da cidade e']

    return random.choice(lista_resultado)


def analisar3():
    lista_resultado = ['forte nebulosidade em partes da cidade com possibilidade de chuvas e',
                       'dia predominantemente nebuloso com possibilidade de chuvas durante a noite e',
                       'forte possibilidade de chuvas localizadas e descargas elétricas em pontos da cidade e',
                       'possibilidade de dia nublado com pancadas de chuvas em pontos da cidade e',
                       'pontos da cidade com forte nevoeiro durante o dia e']

    return random.choice(lista_resultado)


def analisar4():
    lista_resultado = ['forte variação térmica durante todo o dia e',
                       'possibilidade de nuvens e dia ensolarado durante o dia e',
                       'pancadas de chuvas curtas e espaçadas em diversos pontos da cidade e',
                       'dia nublado com sensação térmica alta e possibilidade reduzida de pancadas de chuvas e',
                       'mudança de temperatura bruscas durante o dia e a noite e']

    return random.choice(lista_resultado)


def analisar10():
    lista_resultado = ['céu encoberto durante algumas horas do dia com baixa possibilidade de chuvas e',
                       'possibilidade de nuvens pela manhã e a noite e',
                       'baixa possibilidade de chuvas durante o dia com sensação térmica agradável e',
                       'parte do dia nublado com possibilidade reduzida de pancadas de chuvas muito fortes e',
                       'dia com nuvens isoladas e baixa probabilidade de chuvas']

    return random.choice(lista_resultado)


def filtrar(*args):
    if args[1] == 'Predomínio de Sol':
        prev = analisar()
        return prev
    elif args[1] == 'Possibilidade de Chuva':
        prev1 = analisar1()
        return prev1
    elif args[1] == 'Chuvas Isoladas':
        prev2 = analisar2()
        return prev2
    elif args[1] == 'Variação de Nebulosidade':
        prev3 = analisar3()
        return prev3
    elif args[1] == 'Instável':
        prev4 = analisar4()
        return prev4
    else:
        prev10 = analisar10()
        return prev10
