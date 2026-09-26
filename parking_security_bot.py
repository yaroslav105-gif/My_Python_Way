def check_security_access(has_badge, is_vip_guest):
    if has_badge == True or is_vip_guest == True:
        print("Доступ на парковку автосалона разрешён!")
    else:
        print("Доступ закрыт. Разверните машину.")
check_security_access(False, True)
