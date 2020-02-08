# 6. Дана строка "English = 78 Science = 83 Math = 68 History = 65". Вычислить сумму всех чисел в строке.

s = input('Введите строку: ')
i = ''
result = 0
for symbol in s:
    if symbol.isdigit():
        i += symbol
    elif i != '':
        result += int(i)
        i = ''
if i != '':
    result += i
print('Сумма:', result)
