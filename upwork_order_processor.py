def process_orders(orders_list):
    vip_orders = []
    total_vip_sum = 0
    for i in orders_list:
        if i < 1000:
            print("Мелкий заказ:" + str(i) + " $")
        elif i < 3000:
            print("Нормальный заказ:" + str(i) + "$")
        else:
            vip_orders.append(i)
            total_vip_sum = total_vip_sum + i
    print(vip_orders)
    return total_vip_sum
my_prices = [500, 4500, 1200, 3500]
final_vip_income = process_orders(my_prices)
print("Общий доход с VIP-заказов: " + str(final_vip_income) + " $") 
