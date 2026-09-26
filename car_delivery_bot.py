def give_car_keys(is_paid, has_passport):
    if is_paid == True and has_passport == True:
        print("Ключи выданы! Счастливого пути!")
    else:
        print("Выдача отменена. Проверьте оплату или документы.")
give_car_keys(True, False)
