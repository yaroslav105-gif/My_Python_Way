def approve_test_drive(client_age, has_ban):
    if client_age > 18 and not has_ban:
        print("Тест-драйв одобрен! Выдайте ключи покупателю.")
    else:
        print( "Отказано в тест-драйве. Проверьте возраст или статус блокировки.")
approve_test_drive(21, False)
