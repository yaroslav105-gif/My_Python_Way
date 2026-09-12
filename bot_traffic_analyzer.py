user_actions = [400, 1500, 800, 4200, 150, 3100]
def analyze_bot_traffic(actions):
    vip_clients = []
    total_usd = 0
    for tek_summa in actions:
        total_usd = total_usd + tek_summa
        if tek_summa < 500:
            print("Обычный юзер: " + str(tek_summa) + "$")
        elif tek_summa < 2000:
            print("Активный юзер: " + str(tek_summa) + "$")
        else:
            vip_clients.append(tek_summa)
            print("VIP КЛИЕНТ: " + str(tek_summa) + "$")
    print(vip_clients)
    return total_usd
def convert_to_rubles(usd_amount):
    return usd_amount * 95
final_usd_income = analyze_bot_traffic(user_actions)
final_rub_income = convert_to_rubles(final_usd_income)
print("--- ИТОГОВЫЙ ОТЧЕТ ХАКАТОНА ---")
print("Зароботано: " + str(final_usd_income) + "$" + "-" + str(final_rub_income) + " руб")
