gamer_card= {
    "name": "Yarik_Dev",
    "xp": 1400,
    "levl_up": 2000}
def check_level_up(profit):
    ostatok = profit["levl_up"] - profit["xp"]
    if ostatok > 0:
        print(profit["name"], "Осталось набрать", sep="|", end=":")
        print(str(ostatok), "XP")
    else:
        
        print("💥 ПОЗДРАВЛЯЕМ! Доступен новый уровень!")
check_level_up(gamer_card)
