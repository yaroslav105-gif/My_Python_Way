def check_payout_status(balance):
    if balance < 1000:
        return ("Отказ. Минимальная сумма вывода 1000$")
    else:
        return ("Заявка одобрена")
payout_result = check_payout_status(1200)
print(payout_result)
