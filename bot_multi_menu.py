user_message = input("Введите команду (Баланс или Помощь): ")
if user_message == "Баланс" or user_message == "баланс":
    print("Ваш баланс: 5000 рублей.")
elif user_message == "Помощь" or user_message == "помощь":
    print("Связь с Никитой: @nikita_lead")
else:
    print("Неизвестная команда.")
