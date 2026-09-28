def check_payment_status(is_paid):
    if not is_paid:
        print("⚠️ Внимание: Платёж не найден! Заблокировать выдачу авто.")
    else:
        print("Оплата подтверждена. Машина готова к выдаче.")
check_payment_status(False)
