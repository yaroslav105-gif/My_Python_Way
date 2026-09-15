upwork_orders = [
    {"title": "Telegram Bot", "budget": 600, "is_open": True},
    {"title": "Parser for Site", "budget": 250, "is_open": False}
    ]
for order in upwork_orders:
    if (order["is_open"] == True):
        print(order["title"] + " открыт! Бюджет: " + str(order["budget"]) + "$")
    else:
        print(order["title"] + " уже занят фрилансером.")
