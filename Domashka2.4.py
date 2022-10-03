# Напишите программу, которая принимает на вход N, и координаты двух точек и находит расстояние между ними в N-мерном пространстве.
# ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**0.5
import math
def prostranstva(error):
    N = int(input("Введите N: "))
    if N == 1:
        x1 = int(input("Введите x1: "))
        x2 = int(input("Введите x2: "))
        print(abs(x2-x1))
    elif N == 2:
        x1 = int(input("Введите x1: "))
        x2 = int(input("Введите x2: "))
        y1 = int(input("Введите y1: "))
        y2 = int(input("Введите y2: "))
        print(((x2-x1)**2 + (y2-y1)**2)**0.5)
    elif N == 3:
        x1 = int(input("Введите x1: "))
        x2 = int(input("Введите x2: "))
        y1 = int(input("Введите y1: "))
        y2 = int(input("Введите y2: "))
        z1 = int(input("Введите z1: "))
        z2 = int(input("Введите z2: "))
        print(((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**0.5)
    elif N == 4:
        x1 = int(input("Введите x1: "))
        x2 = int(input("Введите x2: "))
        y1 = int(input("Введите y1: "))
        y2 = int(input("Введите y2: "))
        z1 = int(input("Введите z1: "))
        z2 = int(input("Введите z2: "))
        w1 = int(input("Введите w1: "))
        w2 = int(input("Введите w2: "))
        print(((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2 + (w2-w1)**2)**0.5)
    elif N == 0 or N<0 or N>4:
        print(error)
    return(error)
error = ("Введите число от 1 до 4")
try:
    error=prostranstva(error)
except:
    print("Некорректный ввод!")
