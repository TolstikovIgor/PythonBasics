digit = input("Введите целое положительное число: ")
x = 0
for i in digit:
    while int(i) > x:
        x = int(i)
print('Наибольшая цифра в числе', digit,'-', x)
