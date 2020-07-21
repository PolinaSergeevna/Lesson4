from itertools import count
from itertools import cycle

# Первая часть задания
# a = int(input('Введите стартовое число: '))
# for i in count(a):
#     if i > 10:
#         break
#     else:
#         print(i)

# Вторая часть задания
a = list(input('Введите элементы списка: '))
с = 0
for el in cycle(a):
    if с > 10:
        break
    print(el)
    с += 1

