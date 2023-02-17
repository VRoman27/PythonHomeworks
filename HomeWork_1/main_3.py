# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

number = int(input("Введите номер билета: "))
if number < 999999:
    sum_1 = (number // 1000) % 10 + (number // 10000) % 10 + number // 100000
    sum_2 = number % 10 + (number // 10) % 10 + (number // 100)%10
    if sum_1 == sum_2:
        print("Счастливый билет!")
    else:
        print("Обычный билет")
else:
    print("Такого билета не существует")