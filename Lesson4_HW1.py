def zarplata():
    x = int(input('Введите количество отработанных часов : '))
    y = float(input('Введите суммы оплаты труда за 1 час : '))
    bonus = float(input('Укажите размер премии - '))
    zarpl = x * y
    return zarpl + bonus
print(f'Заработная плата сотрудника составила: {zarplata() }')
