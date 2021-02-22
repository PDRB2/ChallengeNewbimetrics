# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import os
from pip._vendor import requests
import pandas as pd


def desafio1(param, url_api, url_entrada):
    x = requests.get(url_api)
    json_data = json.loads(x.text)
    print(x)
    with open(url_entrada, 'w') as outfile:
        json.dump(json_data, outfile)
    print(param)


def desafio2(param):
    with open(os.getcwd() + '/recursos/Sellers.json') as json_file:
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

    df = pd.DataFrame(rows_neutral, columns=['id', 'site_id', 'nickname', 'total'])
    df.to_csv(os.getcwd() + '/searcher/json/2020/02/neutral/neutral.csv')
    df = pd.DataFrame(rows_negative, columns=['id', 'site_id', 'nickname', 'total'])
    df.to_csv(os.getcwd() + '/searcher/json/2020/02/negative/negative.csv')
    df = pd.DataFrame(rows_positive, columns=['id', 'site_id', 'nickname', 'total'])
    df.to_csv(os.getcwd() + '/searcher/json/2020/02/positive/positive.csv')
    print(df)
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


def desafio3(param, url_entrada1, url_entrada2):

    print(pd.read_csv(url_entrada2))
    dataframe1 = pd.read_csv(url_entrada2)
    print(pd.read_csv(url_entrada1))
    dataframe2 = pd.read_csv(url_entrada1)
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


def desafio5(param, url_entrada):
    dataframe1 = pd.read_csv(url_entrada)
    dataframe1['conversionRate'] = dataframe1["soldQuantity"] / dataframe1["visits"]
    dataframe_final = dataframe1.sort_values('conversionRate', ascending=False)
    dataframe_final['conversionRanking'] = range(1, 1 + len(dataframe_final))
    print(dataframe_final)
    print(param)
    pass


def desafio6(param, url_entrada):
    dataframe = pd.read_csv(url_entrada)
    dataframe['porcentajeStock'] = (dataframe['availableQuantity'] * 100) / (
            dataframe['availableQuantity'] + dataframe['soldQuantity'])
    dataframefiltrado = dataframe.filter(['itemId', 'availableQuantity', 'porcentajeStock'])
    dataframefiltrado = dataframefiltrado.sort_values('porcentajeStock', ascending=False)
    print(dataframefiltrado)
    pass


if __name__ == '__main__':
    val = input("Bienvenido a la demostracion de challenge seleccione la opcion: \n"
                "1 desafio de api                   -----\n"
                "2 desafio de deserializacion       -----\n"
                "3 desafio de parseo de dataframe   -----\n"
                "4 desafio de join                  -----\n"
                "5 desafio de metricas              -----\n"
                "6 desafio de metricas 2            -----\n")
    print(val)
    if int(val) == 1:    desafio1('Lo logramos pasamos el primer desafio',
                      'https://api.mercadolibre.com/sites/MLA/search?category=MLA1000',
                        os.getcwd() + '/searcher/json/2020/02/MLA100.json')
    val = input("Perfecto, continuemos con las pruebas o termine el proceso: \n")
    if int(val) == 2:
             desafio2('Lo logramos pasamos el segundo desafio')
    val = input("Perfecto, continuemos con las pruebas o termine el proceso: \n")
    if int(val) == 3:
             desafio3(' logramos el cuarto desafio', os.getcwd() + '/searcher/json/2020/02/neutral/neutral.csv',
             os.getcwd() + '/recursos/visits.csv')
             val = input("Perfecto, continuemos con las pruebas o termine el proceso: \n")
    if int(val) == 4:
             desafio4('Con python logramos el tercer desafio', os.getcwd() + '/recursos/MPE1004.json',
             os.getcwd() + '/searcher/json/2020/02/neutral/neutral.csv')
             val = input("Perfecto, continuemos con las pruebas o termine el proceso: \n")
    if int(val) == 5:
            desafio5(' logramos el cuarto desafio', os.getcwd() + '/searcher/json/2020/02/resultados_join_visitas.csv')
            val = input("Perfecto, continuemos con las pruebas o termine el proceso: \n")
    if int(val) == 6:
             desafio6(' logramos el septimo desafio', os.getcwd() + '/searcher/json/2020/02/neutral/neutral.csv')
             val = input("Perfecto, continuemos con las pruebas o termine el proceso: \n")

