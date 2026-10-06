vehicle_card = {
    "model":"BMW M5",
    "usd":120000,
    "privod":"AWD"}
def classify_and_log_car(perfikt):
    if perfikt["usd"] > 100000:
        categoria = "VIP"
    elif perfikt["usd"] > 50000:
        categoria = "COMFORT"
    else:
        categoria = "ECONOMY"
    print(perfikt["model"], categoria, sep=" | ", end=" -> ")
    print("INSERT INTO " + categoria + "_cars VALUES(" + perfikt["model"] + ");")
classify_and_log_car(vehicle_card)
