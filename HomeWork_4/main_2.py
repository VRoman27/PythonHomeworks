# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

countBush = int(input("Введите количество кустов: "))
berries = list()
for i in range(countBush):
    berries.append(int(input(f"Количество ягод на кусте №{i}: ")))

max = 0
tmp = None
for i in range(0, -len(berries), -1):
    tmp = berries[i-1] + berries[i] + berries[i+1]
    if max < tmp:
        max = tmp

print(berries)
print(max)