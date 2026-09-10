shop_prices = [1500,6000,800,4500]
hot_deals = []
total_sale_sum = 0
for i in shop_prices:
    sale_price = i / 2
    total_sale_sum =total_sale_sum + sale_price
    if (sale_price) < 1000:
        hot_deals.append(sale_price)
    elif (sale_price) < 2500:
        print("Хорошая цена: " + str(sale_price))
    else:
        print("Большая цена даже со скидкой: " + str(sale_price))
final_report = ("Общая стоимость товаров со скидкой: " + str(total_sale_sum) + " руб")
print(final_report)
print(hot_deals)
