# 5. Напишите генератор случайных паролей.
# После запуска программа должна ждать ввода числа - длины пароля и нажатия Enter.
# Завершить программу нужно если будет введен 0. Также нужно проверять является ли введенная строка числом.
# Допустимые символы - цифры, большие и маленькие латинские буквы.(нужно использовать метод input)
import random

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghilklmnopqrstuvwxyz0123456789'
f = input('Введите длину: ')


def password(f, alphabet):
    f = int(f)
    s = ''
    i = 0
    while i < f:
        s += random.choice(alphabet)
        i += 1
    print('Пароль:', s)


while f != '0' and f.isdigit():
    password(f, alphabet)
    f = input('Введите длину: ')




