def check_vault(user_id, password):
    if user_id == 777 and password == "Open":
        print("Сейф открыт! Внутри 15 000 000 рублей.")
    else:
        print("⚠️ Тревога! Неверный ID или пароль!")
check_vault(777, "Open")
