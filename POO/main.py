from binance.client import Client
from secrets import api_secret, api_key
from binance.enums import *

client = Client(api_key= api_key,api_secret= api_secret)

info = client.get_account()
for i in info:
    print(i)

lista_ativos = info['balances']

for ativo in lista_ativos:
    if float(ativo['free'])>0:
        print(ativo)


order = client.create_order(
    symbol='BNBBRL',
    side=SIDE_SELL,
    type=ORDER_TYPE_MARKET,
    quantity=10
    )

print(order)

print(client.get_all_orders(symbol="BNBBRL"))
print(client.get_my_trades(symbol="BNBBRL"))

transacoes = client.get_recent_trades(symbol="BNBBRL", limit=1)
print(transacoes)



