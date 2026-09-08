bitcoin_price = 90000
for i in range (3):
    bitcoin_price = bitcoin_price + 2000
    if bitcoin_price >= 95000:
        print("критическая цена " + str(bitcoin_price))
