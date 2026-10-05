car_in_stock = True
def confirm_delivery():
    global car_in_stock
    car_in_stock = False
confirm_delivery()
print(car_in_stock)
