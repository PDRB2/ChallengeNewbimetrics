# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import os

from pip._vendor import requests
import pandas as pd


def buscameElResponse(param, url_api, url_entrada):
    # Use a breakpoint in the code line below to debug your script.
    x = requests.get(url_api)
    json_data = json.loads(x.text)
    print(x)
    with open(url_entrada, 'w') as outfile:
        json.dump(json_data, outfile)
    print(param)


def mostrameeldataframe(param):
    with open(os.getcwd()+'/recursos/Sellers.json') as json_file:
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
        if seller_reputation >= 1: rows_positive.append([sellerid, siteid, nickname, seller_reputation])
        if seller_reputation <= -1:
            rows_negative.append([sellerid, siteid, nickname, seller_reputation])
        else:
            rows_neutral.append([sellerid, siteid, nickname, seller_reputation])

    df = pd.DataFrame(rows_neutral, columns=['id', 'site_id', 'nickname', 'total'])
    df.to_csv(os.getcwd()+'/searcher/json/2020/02/neutral/neutral.csv')
    df = pd.DataFrame(rows_negative, columns=['id', 'site_id', 'nickname', 'total'])
    df.to_csv(os.getcwd()+'/searcher/json/2020/02/negative/negative.csv')
    df = pd.DataFrame(rows_positive, columns=['id', 'site_id', 'nickname', 'total'])
    df.to_csv(os.getcwd()+'/searcher/json/2020/02/positive/positive.csv')
    print(df)
    print(param)


# Press the green button in the gutter to run the script.
def buscaymostranuevodatafram(param, url_entrada, url_salida):
    with open(url_entrada) as json_file:
        data = json.load(json_file)
        rows = []
        i = 0
        for item in data['results']:
            i = i+1
            rowid = i
            itemid = item['id']
            availableQuantity = item['available_quantity']
            soldQuantity = item['sold_quantity']
            rows.append([rowid, itemid, availableQuantity, soldQuantity])

    df = pd.DataFrame(rows, columns=['rowid', 'itemId', 'availableQuantity', 'soldQuantity'])
    df.to_csv(url_salida, index=False)
    print(df)
    print(param)

    pass


def obtenerdataframe(url_entrada ,columnas):
    column_names = ['rowid', 'itemId', 'availableQuantity', 'soldQuantity']
    iris = pd.read_csv(url_entrada, names=columnas)
    return iris


def vamosajoinear(param, url_entrada1, url_entrada2):
    print(pd.read_csv(url_entrada2))
    dataframe1 = pd.read_csv(url_entrada2)
    print(pd.read_csv(url_entrada1))
    dataframe2 = pd.read_csv(url_entrada1)
    dataframfinal = pd.merge(dataframe1, dataframe2,how='inner', on=['itemId'])
    dataframfinal = dataframfinal.filter(["itemId", "visits", "soldQuantity"])
    print('antes del filtro'+dataframfinal)
    dataframfinal= dataframfinal[(dataframfinal.soldQuantity > 1)]
    print('despues del filtro'+dataframfinal)
    print(param)
    pass


if __name__ == '__main__':
    #   buscameElResponse('Lo logramos pasamos el primer desafio',
    # 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1000',
    # 'os.getcwd()+'/searcher/json/2020/02/MLA100.json')
    #    mostrameeldataframe('Lo logramos pasamos el segundo desafio')
        buscaymostranuevodatafram('Con python logramos el tercer desafio',os.getcwd()+'/recursos/MPE1004.json',os.getcwd()+'/searcher/json/2020/02/neutral/neutral.csv')
        vamosajoinear(' logramos el cuarto desafio',                  os.getcwd()+'/searcher/json/2020/02/neutral/neutral.csv',
                 os.getcwd()+'/recursos/visits.csv')
