#access API of https://www.alphavantage.co/

import requests 
url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=FOS5A8ZRGMG9OX1W'
r = requests.get(url) #to retreive data from server 
#print(r)  # if its 200 meaning it has worked and i can retrive data 
data=r.json()
#print(data)

#extract real time exhange rate (forex) in JSON output using API parameteres

print(data.keys())


