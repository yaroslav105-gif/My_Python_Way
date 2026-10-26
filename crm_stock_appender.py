def add_car_to_stock(garage, new_car):
    garage.append(new_car)
    return garage
current_stock = ["BMW", "Porsche"]
updated_stock = add_car_to_stock(current_stock, "Ferrari")
print(updated_stock)
