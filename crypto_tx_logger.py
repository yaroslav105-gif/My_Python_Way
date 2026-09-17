def log_transaction(crypto_name, amount, action):
    print("TX", action, crypto_name, sep="_", end=" : ")
    print(amount)
log_transaction("BTC", 2, "BUY")
