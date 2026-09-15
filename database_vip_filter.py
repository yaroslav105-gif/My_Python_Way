clients_list = [
    {"username": "alex_freelance", "orders": 3},
    {"username": "olga_code", "orders": 12}
    ]
for user in clients_list:
    if (user["orders"] > 5):
        print(user["username"] + " - VIP клиент")
    else:
        print(user["username"] + " - это обычный клиент")
