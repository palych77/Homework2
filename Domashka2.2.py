# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
def mulnum(msg):
    z = 1
    for i in range(n):
        i+=1
        z=z*i
        print(z, end = " " )
    return msg

msg = "Некорректный ввод!"
try:
    n = int(input("Введите число: "))
    msg = mulnum(msg)
except:
    print(msg)