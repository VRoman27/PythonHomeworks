# Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

N =  int(input("Введите число: "))
pow2 = 1
while pow2 <= N:
    print(pow2)
    pow2 *= 2