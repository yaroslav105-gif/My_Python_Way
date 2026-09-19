user_profile = {

    "nik":"Yarik",
    "rank":"Junior",
    "status":True
    }
def check_admin_access(chek):
    if chek["status"] == True:
        print("ДОСТУП", chek["nik"], chek["rank"], sep=" | ", end=" -> ")
        print("Вход разрешен")
    else:
        print("Вход заблокирован.")
check_admin_access(user_profile)
