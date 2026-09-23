lead_card = {
    "name":"Yarik_Dev",
    "car":"Porsche",
    "butjat":120000}
def process_client_lead(bekend):
    if bekend["butjat"] > 100000:
        print(bekend["name"], "КАТЕГОРИЯ: VIP", sep=" | ", end="->")
        print("INSERT INTO vip_leads VALUES(" + bekend["car"] + ");")
    else:
        print("Лид отправлен в общую таблицу распределения.")
process_client_lead(lead_card)
