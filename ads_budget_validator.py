ads_card = {
    "name": "Yarik_Dev",
    "balans": 800,
    "ad": 300
    }
def process_ads_payment(profit):
    ostatok = profit["balans"] - profit["ad"]
    if ostatok > 0:
        print(profit["name"], "Остаток баланса", sep=": ", end="->")
        print(str(ostatok), "$")
    else:
        print("⚠️ Ошибка: Недостаточно средств для запуска рекламы!")
process_ads_payment(ads_card)
