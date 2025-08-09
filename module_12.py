# 12. Модули random и string
"""
Этот модуль посвящен работе со случайными числами в Python.
Рассматриваются генерация псевдослучайных чисел и основные функции модуля
random, метод Монте-Карло и алгоритм болотной сортировки,
а также модуль string.
"""

import random
from string import *


# 12.1 Модуль random. Часть 1


def m_12_1_1():
    # import random
    n = int(input())
    for _ in range(n):
        print(("Орел", "Решка")[random.randint(0, 1)])


def m_12_1_2():
    # import random
    n = int(input())  # количество попыток
    for _ in range(n):
        print(random.randint(1, 6))


def m_12_1_3():
    # import random
    length = int(input())  # длина пароля
    abc = tuple(chr(i) for i in range(65, 123) if i not in range(91, 97))
    print("".join(abc[random.randint(0, len(abc) - 1)] for _ in range(length)))


def m_12_1_4():
    # import random
    ticket = set()
    while len(ticket) < 7:
        ticket.add(random.randint(1, 49))
    print(*sorted(ticket))


# 12.2 Модуль random. Часть 2


def m_12_2_1():
    # from random import *
    def generate_ip():
        res = (str(randint(0, 255)) for _ in range(4))
        return ".".join(res)


def m_12_2_2():
    # from random import *
    # import string

    def generate_index():
        res = [choice(string.ascii_uppercase) for _ in range(4)] + [
            str(randint(0, 99)) for _ in range(4)
        ]
        return f"{res[0]}{res[1]}{res[-2]}_{res[-1]}{res[2]}{res[3]}"


def m_12_2_3():
    # import random

    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    data = [num for row in matrix for num in row]
    random.shuffle(data)
    matrix = [[data.pop() for __ in range(4)] for _ in range(4)]


def m_12_2_4():
    # from random import *
    res = set()
    while len(res) < 100:
        num = "".join([str(randint(1, 9))] + [str(randint(0, 9)) for _ in range(6)])
        if num not in res:
            res.add(num)
            print(num)


def m_12_2_5():
    # from random import shuffle

    word = input().split()
    shuffle(word)
    print("".join(word))


def m_12_2_6():
    # from random import randint

    data = set()
    while len(data) < 25:
        data.add(str(randint(1, 75)))
    matrix = [[data.pop().ljust(2) for __ in range(5)] for _ in range(5)]
    matrix[2][2] = "0".ljust(2)
    for row in matrix:
        print(*row)


def m_12_2_7():  # Тайный друг
    # from random import shuffle

    students = [input() for _ in range(int(input()))]
    friends = students.copy()

    while any(s == f for s, f in zip(students, friends)):
        shuffle(friends)

    for s, f in zip(students, friends):
        print(f"{s} - {f}")


def m_12_2_89():  # Генератор паролей 1
    # from random import *
    # from string import *

    def generate_password(length):
        res = set()
        while len(res) < length:
            res.add(choice(ABC))
        return "".join(res)

    def generate_passwords(count, length):
        res = set()
        while len(res) < count:
            res.add(generate_password(length))
        return res

    ABC = "".join(
        i for i in (ascii_uppercase + ascii_lowercase + digits) if i not in "lI1oO0"
    )

    n, m = int(input()), int(input())
    print(*generate_passwords(n, m), sep="\n")


def m_12_2_9():  # Генератор паролей 2
    # from random import *
    # from string import *

    def generate_password(length):
        pswd = {choice(ABC[:24]), choice(ABC[24:48]), choice(ABC[48:])}
        while len(pswd) < length:
            pswd.add(choice(ABC))
        res = list(pswd)
        shuffle(res)
        return "".join(res)

    def generate_passwords(count, length):
        res = set()
        while len(res) < count:
            res.add(generate_password(length))
        return res

    ABC = "".join(
        i for i in (ascii_uppercase + ascii_lowercase + digits) if i not in "lI1oO0"
    )

    n, m = int(input()), int(input())
    print(*generate_passwords(n, m), sep="\n")


# 12.3 Метод Монте-Карло и Bogosort


def m_12_3_1():  #
    # import random

    n = 10**6  # количество испытаний
    s0 = 4 * 4
    k = 0
    for _ in range(n):
        x = random.uniform(-2, 2)
        y = random.uniform(-2, 2)

        if x**3 + y**4 + 2 >= 0 and 3 * x + y**2 <= 2:
            k += 1

    print((k / n) * s0)


def m_12_3_2():  #
    # import random

    n = 10**6  # количество испытаний
    s0 = 2 * 2
    k = 0
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 <= 1:
            k += 1

    print((k / n) * s0)
