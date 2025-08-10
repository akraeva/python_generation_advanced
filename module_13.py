# 13. Модули decimal, fraction и complex
"""
Этот модуль посвящен числовым типам данных в Python.
Рассматриваются модуль decimal и тип данных Decimal для работы с
десятичными числами, модуль fractions и тип данных Fraction для
работы с дробями, а также тип данных complex для комплексных чисел.
"""

from decimal import *
from math import gcd
from math import factorial
from fractions import Fraction as F

# 13.1 Модуль decimal


def m_13_1_1():
    # from decimal import *

    s = "0.77 4.03 9.06 3.80 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.23 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50"
    d = [Decimal(x) for x in s.split()]
    print(max(d) + min(d))


def m_13_1_2():
    # from decimal import *

    s = "9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09 7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 5.22 4.08 3.86 5.56 1.43 8.36 6.29 5.13"
    d = [Decimal(x) for x in s.split()]
    print(sum(d))
    print(*sorted(d, reverse=True)[:5])


def m_13_1_3():
    # from decimal import *

    num = Decimal(input())
    print(max(num.as_tuple()[1]) + (0 if -1 < num < 1 else min(num.as_tuple()[1])))


def m_13_1_4():  # Математическое выражение
    # from decimal import *

    d = Decimal(input())
    print(d.exp() + d.ln() + d.log10() + d.sqrt())


# 13.2 Модуль fractions


def m_13_2_1():
    # from fractions import Fraction as F

    numbers = [
        "6.34",
        "4.08",
        "3.04",
        "7.49",
        "4.45",
        "5.39",
        "7.82",
        "2.76",
        "0.71",
        "1.97",
        "2.54",
        "3.67",
        "0.14",
        "4.29",
        "1.84",
        "4.07",
        "7.26",
        "9.37",
        "8.11",
        "4.30",
        "7.16",
        "2.46",
        "1.27",
        "0.29",
        "5.12",
        "4.02",
        "6.95",
        "1.62",
        "2.26",
        "0.45",
        "6.91",
        "7.39",
        "0.52",
        "1.88",
        "8.38",
        "0.75",
        "0.32",
        "4.81",
        "3.31",
        "4.63",
        "7.84",
        "2.25",
        "1.10",
        "3.35",
        "2.05",
        "7.87",
        "2.40",
        "1.20",
        "2.58",
        "2.46",
    ]
    for n in numbers:
        print(f"{n} = {F(n)}")


def m_13_2_2():
    # from fractions import Fraction as F

    s = "0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021"
    nums = [F(n) for n in s.split()]
    print(max(nums) + min(nums))


def m_13_2_3():  # Сократите дробь
    # from fractions import Fraction as F

    print(F(int(input()), int(input())))


def m_13_2_4():  # Операции над дробями
    # from fractions import Fraction as F

    n1, n2 = input(), input()
    print(f"{n1} + {n2} = {F(n1) + F(n2)}")
    print(f"{n1} - {n2} = {F(n1) - F(n2)}")
    print(f"{n1} * {n2} = {F(n1) * F(n2)}")
    print(f"{n1} / {n2} = {F(n1) / F(n2)}")


def m_13_2_5():  # Сумма дробей 1
    # from fractions import Fraction as F

    print(sum(F(1, (i + 1) ** 2) for i in range(int(input()))))


def m_13_2_6():  # Сумма дробей 2
    # from fractions import Fraction as F
    # from math import factorial

    print(sum(F(1, factorial(i + 1)) for i in range(int(input()))))


def m_13_2_7():  # Юный математик
    # from fractions import Fraction as F
    # from math import gcd

    n = int(input())
    print(max(F(i, n - i) for i in range(1, n) if i < n - i and gcd(i, n - i) == 1))


def m_13_2_8():  # Упорядоченные дроби
    # from fractions import Fraction as F
    # from math import gcd

    n = int(input())
    print(
        *sorted(
            F(num, den)
            for den in range(2, n + 1)
            for num in range(1, den)
            if gcd(num, den) == 1
        ),
        sep="\n",
    )


# 13.3 Тип данных complex


def m_13_3_1():  # Операции над комплексными числами
    z1, z2 = complex(input()), complex(input())
    print(f"{z1} + {z2} = {z1 + z2}")
    print(f"{z1} - {z2} = {z1 - z2}")
    print(f"{z1} * {z2} = {z1 * z2}")


def m_13_3_2():
    numbers = [
        3 + 4j,
        3 + 1j,
        -7 + 3j,
        4 + 8j,
        -8 + 10j,
        -3 + 2j,
        3 - 2j,
        -9 + 9j,
        -1 - 1j,
        -1 - 10j,
        -20 + 15j,
        -21 + 1j,
        1j,
        -3 + 8j,
        4 - 6j,
        8 + 2j,
        2 + 3j,
    ]
    res = max([abs(z), z] for z in numbers)
    print(res[-1], res[0], sep="\n")


def m_13_3_3():  # Сопряженные числа
    n = int(input())
    z1, z2 = complex(input()), complex(input())
    print(z1**n + z2**n + z1.conjugate() ** n + z2.conjugate() ** (n + 1))
