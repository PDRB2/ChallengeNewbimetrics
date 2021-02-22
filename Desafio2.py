# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json

from pip._vendor import requests


def mostrameEldataFrame(name):
    # Use a breakpoint in the code line below to debug your script.

    with open('/searcher/json/2020/02/Sellers.json') as json_file:
        data = json.load(json_file)

        for item in data['body']:
            seller_reputation = item['seller_reputation']

            seller = item['seller']

            print('site_id: ' + item['site_id'])
            print('sellerid: ' + seller['id'])
            print('seller_reputation: ' + seller_reputation['total'])
            print('nickname: ' + item['nickname'])
            print('')
    id


    print(name)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mostrameEldataFrame('Lo logramos pasamos el primer desafio')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


  print(data[0]['body'])
        for item in data:

            seller_reputation = item['body']["seller_reputation"]["transactions"]
            sellerid = [item['body']['id']]
            siteid=  [item['body']["site_id"]]
            nickname= item['body']["nickname"]
            seller_reputation=seller_reputation["total"]

            data = list()
            data.__add__(d)

# l = [('Ankit', 25), ('Jalfaizy', 22), ('saurabh', 20), ('Bala', 26)]
rdd = sc.parallelize(rows)
people = rdd.map(lambda x: Row(nickname=x[2], id=int(x[0]), seller_reputation=int(x[3]), siteid=x[1]))
schemaPeople = sqlContext.createDataFrame(people)
type(schemaPeople)