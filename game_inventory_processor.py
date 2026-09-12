def process_inventory(items_list):
    legendary_items = []
    total_gold = 0
    for i in items_list:
        if i < 500:
            print("Обычный хлам: " + str(i) + " золота")
        elif i < 2000:
            print("Редкий предмет: " + str(i) + " золота")
        else:
             legendary_items.append(i)
             total_gold = total_gold + i
    print(legendary_items)
    return total_gold
chest_loot = [300, 4500, 1200, 2500]
final_gold_income = process_inventory(chest_loot)
print("Общая стоимость легендарок: " + str(final_gold_income) + " золота")
