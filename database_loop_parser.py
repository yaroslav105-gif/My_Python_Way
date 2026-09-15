clients_list = [
    {"username": "alex_freelance", "orders": 3},
    {"username": "olga_code", "orders": 12}
     ]
print(clients_list)
for user in clients_list:
    print("Количество заказов: " + str(user["orders"]))
