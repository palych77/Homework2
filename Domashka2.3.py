#  Реализуйте алгоритм перемешивания списка. Список размерностью 10 задается случайными целыми числами, выводится на экран, затем перемешивается, 
#  опять выводится на экран. SHUFFLE нельзя юзать!
import random
def mix_list(spisok):
    list = spisok[:]
    list_length = len(list) 
    for i in range(list_length):
        index_aleatory = random.randint(0, list_length - 1)
        temp = list[i]
        list[i] = list[index_aleatory]
        list[index_aleatory] = temp
    print("Перемешанный список: ", list)
    return list

spisok=[]
for i in (range(10)):
    spisok.append(random.randint(-100,100))
print("Изначальный список: ", spisok)
mix_list(spisok)
