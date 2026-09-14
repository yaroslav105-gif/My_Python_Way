ping_data = [40, 180, 25, 220]
good_servers = []
total_ping = 0
for ping in ping_data:
    if ping < 100:
        good_servers.append(ping)
        total_ping = total_ping + ping
    else:
        print("Сервер лагает: " + str(ping))
print(total_ping)
print("Сумма пинга хороших серверов: " + str(total_ping) + " mc")
