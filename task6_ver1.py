# 6. Дана строка "English = 78 Science = 83 Math = 68 History = 65". Вычислить сумму всех чисел в строке.

s = input('Введите строку: ')
lst = []
i = 0
while i < len(s):
    j = ''
    a = s[i]
    while a.isdigit():
        j += a
        i += 1
        if i < len(s):
            a = s[i]
        else:
            break
    i += 1
    lst.append(int(j)) if j != '' else ''

r = 0
for el in lst:
    r += el
print('Сумма:', r)
