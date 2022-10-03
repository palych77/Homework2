# Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. Через строку нельзя решать.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11
def sumOfNum(msg):
    spisok = []
    enter = input("Введите число: ")
    point = "."
    for i in enter:
        spisok.append(i)
    if point in spisok:
        spisok.remove(point)
    num = "".join(map(str, spisok))
    num = int(num)
    sum=0
    while (num != 0):
        sum = sum + num % 10
        num = num // 10
    print("Сумма цифр числа равна: ",sum)
    return(msg)

msg="Некорректный ввод!\nВведите число!\nПри введении вещественного числа необходимо использовать точку!"
try:
    msg = sumOfNum(msg)
except:
    print(msg)
