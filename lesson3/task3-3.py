def my_func():
    a = float(input('Введите число a: '))
    b = float(input('Введите число b: '))
    c = float(input('Введите число c: '))
    return a + b + c - min(a, b, c)
print('Сумма двух максимальных чисел = ', my_func())
