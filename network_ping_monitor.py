ping_list = [45, 120, 30, 210]
best_server = []
total_ping = 0
for i in ping_list:
    total_ping = total_ping + (i)
    if (i) < 50:
        best_server.append(i)
    elif (i) < 150:
        print("Нормальный пинг: " + str(i))
    else:
        print("Сервер хуета: " + str(i))
report = ("Общая сумма пинга сети: " + str(total_ping) + " мс")
print(report)
print(best_server)
