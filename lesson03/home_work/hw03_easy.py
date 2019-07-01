# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigit):
    splitted = str(number).split(".")
    tail = splitted.pop()
    head = splitted.pop()
    end_tail = list(tail[ndigit:])
    tail = list(tail[:ndigit])

    if int(end_tail[0]) > 4:
        i = len(end_tail) - 1

        while i > 0:
            if int(end_tail[i]) > 9:
                end_tail[i] = 0
                end_tail[i - 1] = int(end_tail[i - 1]) + 1

            if int(end_tail[i]) > 5:
                end_tail.pop()
                end_tail[i - 1] = int(end_tail[i - 1]) + 1
            i -= 1
        i = len(tail) - 1

        if len(end_tail) > 0:
            if int(end_tail[0]) > 4:
                tail[i] = int(tail[i]) + 1

        while i > 0:
            if int(tail[i]) > 9:
                tail[i] = 0
                tail[i - 1] = int(tail[i - 1]) + 1
            i -= 1

        if int(tail[0]) > 9:
            head = int(head) + 1
            tail[0] = 0

    return float(str(head) + '.' + ''.join(str(x) for x in tail))


print(my_round(2.1234567, 5), round(2.1234567, 5))
print(my_round(2.1999967, 5), round(2.1999967, 5))
print(my_round(2.9999967, 5), round(2.9999967, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    if sum(map(int, list(str(ticket_number))[:3])) == sum(map(int, list(str(ticket_number))[3:])):
        return True
    else:
        return False

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
