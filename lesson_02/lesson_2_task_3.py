import math


def square(s):
    return math.ceil(s*s)


number = int(input('Введите число: '))
print(f'Площадь квадрата равна: {square(number)}')
