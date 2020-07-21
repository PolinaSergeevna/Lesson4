def my_func(n):
    temp = 1
    for i in range(1, n + 1):
        temp *= i
        yield temp


n = int(input("Просьба указать число для расчета факториала? "))
for _ in my_func(n):
    print(_)