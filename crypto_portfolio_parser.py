crypto_balances=[1200,4500,800,3100]
vip_funds=[]
total_wallet=0
for i in crypto_balances:
    total_wallet = total_wallet + (i)
    if ((i) < 1000):
        print("Мелкий баланс " + str(i))
    elif ((i) < 4000):
        print("Средний баланс " + str(i))
    else:
        vip_funds.append(i)
report_1 =("Всего в кошельке: " + str(total_wallet) + " $")
print(report_1)
print(vip_funds)
