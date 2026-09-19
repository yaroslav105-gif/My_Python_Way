project_card = {
    "proekt":"Telegram Bot",
    "butget_USD":1500,
    "nalog":20}
def calculate_ruble_income(profit):
    tax = profit["butget_USD"] * profit["nalog"] / 100
    net_usd = profit["butget_USD"] - tax
    doh_rub = net_usd * 95
    print(profit["proekt"], "чистый доход", sep=" — ", end=": ")
    print(doh_rub, "руб")
calculate_ruble_income(project_card)
