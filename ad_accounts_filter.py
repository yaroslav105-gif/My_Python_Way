def filter_accounts(balances_list):
    active_accounts = []
    total_budget = 0
    for b in balances_list:
        if b > 0:
            active_accounts.append(b)
            total_budget = total_budget + b
        else:
            print("Аккаунт заблокирован: " + str(b))
    print(active_accounts)
    return total_budget
my_balances = [5000, 0, 1200, 0, 3500]
final_budget = filter_accounts(my_balances)
print("Общий бюджет: " + str(final_budget) + " руб.")
