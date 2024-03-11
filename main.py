def check(ticket_number):
    # Розділяємо рядок на дві частини.
    first = [int(digit) for digit in ticket_number[:3]]
    second = [int(digit) for digit in ticket_number[3:]]

    # Обчислюємо суми цифр у кожній половині.
    sum_first = sum(first)
    sum_second = sum(second)

    # Порівнюємо суми.
    if sum_first == sum_second:
        print("Щасливий")
    else:
        print("Звичайний")

ticket_number = input("Номер квитка (шість цифр): ")
check(ticket_number)
