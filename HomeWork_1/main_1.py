# Найдите сумму цифр трехзначного числа.

number = int(input("Введите трёхзначное число: "))
if number < 1000:
    print(f"Сумма цифр: {number%10+(number//10)%10+(number//100)}")
else:
    print("Нужно трёхзначное число!")