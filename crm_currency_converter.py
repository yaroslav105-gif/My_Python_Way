USD_RATE = 95
def convert_to_rubles(price_usd):
    return price_usd * USD_RATE
ruble_price = convert_to_rubles(10000)
print(ruble_price)
