budget = 4000
if budget >= 4000:
    action = "беру работу"
else:
    action = "слишком мало, пропускаю"
notification = "новый заказ: " + (action) + (" Бюджет ") + str(budget) + ("$")
print(notification)
