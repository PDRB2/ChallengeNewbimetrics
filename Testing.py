import json
import os
from pip._vendor import requests
import pandas as pd
from pip._vendor.distlib.compat import raw_input


def desafio2(param, url_api, url_entrada):
    x = requests.get(url_api)
    json_data = json.loads(x.text)
    print(x)
    with open(url_entrada, 'w') as outfile:
        json.dump(json_data, outfile)
        print('Archivo guardado en' + url_entrada + '\n')
    print(param)


def desafio3(param, url_json):
    neutral = '/searcher/json/2020/02/23/neutral/neutral.csv'
    positivo = '/searcher/json/2020/02/23/positive/positive.csv'
    negativo = '/searcher/json/2020/02/23/negative/negative.csv'
    with open(url_json) as json_file:
        data = json.load(json_file)
        rows_positive = []
        rows_neutral = []
        rows_negative = []
        for item in data:
            seller_reputation_deglosed = item['body']["seller_reputation"]["transactions"]
            sellerid = [item['body']['id']]
            siteid = [item['body']["site_id"]]
            nickname = item['body']["nickname"]
            seller_reputation = seller_reputation_deglosed["total"]
            if seller_reputation >= 1:  rows_positive.append([sellerid, siteid, nickname, seller_reputation])
            if seller_reputation <= -1:
                rows_negative.append([sellerid, siteid, nickname, seller_reputation])
            else:
                rows_neutral.append([sellerid, siteid, nickname, seller_reputation])

    df = pd.DataFrame(rows_neutral, columns=['seller_id', 'site_id', 'nickname', 'total'])
    df.to_csv(os.getcwd() + neutral)
    print('Archivo guardado en' +os.getcwd() + neutral )
    df = pd.DataFrame(rows_negative, columns=['seller_id', 'site_id', 'nickname', 'total'])
    df.to_csv(os.getcwd() + negativo)
    print('Archivo guardado en' + os.getcwd() + negativo)
    df = pd.DataFrame(rows_positive, columns=['seller_id', 'site_id', 'nickname', 'total'])
    df.to_csv(os.getcwd() + positivo)
    print('Archivo guardado en' + os.getcwd() + positivo)
    print(param)


def desafio4(param, url_entrada, url_salida):
    with open(url_entrada) as json_file:
        data = json.load(json_file)
        rows = []
        i = 0
        for item in data['results']:
            i = i + 1
            rowid = i
            itemid = item['id']
            availablequantity = item['available_quantity']
            soldquantity = item['sold_quantity']
            rows.append([rowid, itemid, availablequantity, soldquantity])

    df = pd.DataFrame(rows, columns=['rowid', 'itemId', 'availableQuantity', 'soldQuantity'])
    df.to_csv(url_salida, index=False)
    print(df)
    print(param)

    pass


def desafio5(param, visits, resultados_desafio4, ):
    dataframe1 = pd.read_csv(visits)

    dataframe2 = pd.read_csv(resultados_desafio4)
    dataframfinal = pd.merge(dataframe1, dataframe2, how='inner', on=['itemId'])
    dataframfinal = dataframfinal.filter(["itemId", "visits", "soldQuantity"])
    print('antes del filtro')
    print(dataframfinal)
    dataframfinal = dataframfinal[(dataframfinal.soldQuantity > 1)]
    print('despues del filtro')
    print(dataframfinal)
    print(param)
    dataframfinal.to_csv(os.getcwd() + '/searcher/json/2020/02/resultados_join_visitas.csv', index=False)
    pass


def desafio6(param, url_entrada):
    dataframe1 = pd.read_csv(url_entrada)
    dataframe1['conversionRate'] = dataframe1["soldQuantity"] / dataframe1["visits"]
    dataframe_final = dataframe1.sort_values('conversionRate', ascending=False)
    dataframe_final['conversionRanking'] = range(1, 1 + len(dataframe_final))
    print(dataframe_final)
    print(param)
    pass


def desafio7(param, url_entrada):
    dataframe = pd.read_csv(url_entrada)
    dataframe['porcentajeStock'] = (dataframe['availableQuantity'] * 100) / (
            dataframe['availableQuantity'] + dataframe['soldQuantity'])
    dataframefiltrado = dataframe.filter(['itemId', 'availableQuantity', 'porcentajeStock'])
    dataframefiltrado = dataframefiltrado.sort_values('porcentajeStock', ascending=False)
    print(dataframefiltrado)
    print(param)
    pass


if __name__ == '__main__':


    menu = {}
    menu['1'] = "1 desafio de api"
    menu['2'] = "2 desafio de deserializacion  "
    menu['3'] = "3 desafio de parseo de dataframe   "
    menu['4'] = "4 desafio de join          "
    menu['5'] = "5 desafio de metricas           "
    menu['6'] = "6 desafio de metricas 2        "
    menu['7'] = "7 Exit, espero que le haya gustado!        "
    while True:
        options = menu.keys()
        sorted(options)
        for entry in options:
            print (entry, menu[entry])

        selection = raw_input("Please Select:")
        if selection == '1':
            print('Vamos con el desafio 1')
            desafio2('Lo logramos pasamos el Primero desafio',
                                  'https://api.mercadolibre.com/sites/MLA/search?category=MLA1000',
                                  os.getcwd() + '/searcher/json/2020/02/MLA100.json')
        elif selection == '2':
            print('Vamos con el desafio 2')
            desafio3('Lo logramos pasamos el Segundo desafio', os.getcwd() + '/recursos/Sellers.json')
        elif selection == '3':
            print('Vamos con el desafio 3')
            desafio4(' logramos el Tercero desafio', os.getcwd() + '/recursos/MPE1004.json',
                 os.getcwd() + '/searcher/json/2020/02/resultado.csv')
        elif selection == '4':
            print('Vamos con el desafio 4')
            desafio5('Con python logramos el Quarto desafio', os.getcwd() + '/searcher/json/2020/02/resultado.csv',
                 os.getcwd() + '/recursos/visits.csv')
        elif selection == '5':
            print('Vamos con el desafio 5')
            desafio6(' logramos el Quinto desafio', os.getcwd() + '/searcher/json/2020/02/resultados_join_visitas.csv')
        elif selection == '6':
            print('Vamos con el desafio 6')
            desafio7(' logramos el Sexto desafio', os.getcwd() + '/searcher/json/2020/02/resultado.csv')
        elif selection == '7':
            break
        else:
            print("Opcion erronea, ingrese nuevamente!")


