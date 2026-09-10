site_prices=[3000,7000,4500,9000]
cheap_price=[]
for i in site_prices:
    if (i<5000):
        cheap_price.append(i)
print(cheap_price)
