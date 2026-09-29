def approve_hypercar_test(age, car_brand):
    
    if age > 17 and (car_brand == "Porsche" or car_brand == "Ferrari"):
        print("Тест-драйв гиперкара одобрен! Выкатывайте авто.")
    else:
        print("Отказано. Не подходит возраст или марка машины.")
my_age = int(input("Введите ваш возраст: "))
my_brand = input("Введите марку машины (Porsche или Ferrari): ")
approve_hypercar_test(my_age, my_brand)
