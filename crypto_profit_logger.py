def log_profit(coin_name, income, expenses):
    net_profit = income - expenses
    print("CRYPTO", coin_name, "PROFIT", sep="--", end=": ")
    print(net_profit)
log_profit("ETX", 500, 40)
