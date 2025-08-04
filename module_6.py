# 6. Кортежи
"""
Этот модуль посвящен типу данных tuple в Python.
Рассматриваются основные свойства кортежей, способы их создания,
особенности, отличия от списков, а также основы работы с ними.
"""

# 6.1 Введение в кортежи

# 6.2 Основы работы с кортежами. Часть 1


def m_6_2_1():
    countries = (
        "Russia",
        "Argentina",
        "Spain",
        "Slovakia",
        "Canada",
        "Slovenia",
        "Italy",
    )
    last = countries[-1]
    print(last)


def m_6_2_2():
    primes = (
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
    )
    print(primes[:6])


def m_6_2_3():
    countries = (
        "Russia",
        "Argentina",
        "Slovakia",
        "Canada",
        "Slovenia",
        "Italy",
        "Spain",
        "Ukraine",
        "Chile",
        "Cameroon",
    )
    print(countries[2:])


def m_6_2_4():  #
    countries = (
        "Russia",
        "Argentina",
        "Slovakia",
        "Canada",
        "Slovenia",
        "Italy",
        "Spain",
        "Ukraine",
        "Chile",
        "Cameroon",
    )
    print(countries[:-3])


def m_6_2_5():  #
    countries = (
        "Russia",
        "Argentina",
        "Slovakia",
        "Canada",
        "Slovenia",
        "Italy",
        "Spain",
        "Ukraine",
        "Chile",
        "Cameroon",
    )
    print(countries[3:-2])


def m_6_2_6():
    countries = (
        "Romania",
        "Poland",
        "Estonia",
        "Bulgaria",
        "Slovakia",
        "Slovenia",
        "Hungary",
    )
    number = len(countries)
    print(number)


def m_6_2_7():
    numbers = (12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324)
    res = min(numbers) + max(numbers)
    print(res)


def m_6_2_8():  #
    countries = (
        "Russia",
        "Argentina",
        "Spain",
        "Slovakia",
        "Canada",
        "Slovenia",
        "Italy",
    )
    index = countries.index("Slovenia")
    print(index)


def m_6_2_9():
    countries = (
        "Russia",
        "Argentina",
        "Spain",
        "Slovakia",
        "Canada",
        "Slovenia",
        "Italy",
        "Spain",
        "Ukraine",
        "Chile",
        "Spain",
        "Cameroon",
    )
    number = countries.count("Spain")
    print(number)


def m_6_2_10():
    numbers1 = (1, 2, 3)
    numbers2 = (6,)
    numbers3 = (7, 8, 9, 10, 11, 12, 13)
    res = numbers1 * 2 + numbers2 * 9 + numbers3
    print(res)


def m_6_2_11():
    city_name = input()
    city_year = int(input())
    city = (city_name, city_year)
    print(city)


def m_6_2_12():
    tuples = [
        (),
        (),
        ("",),
        ("a", "b"),
        (),
        ("a", "b", "c"),
        (1,),
        (),
        (),
        ("d",),
        ("", ""),
        (),
    ]
    non_empty_tuples = [elem for elem in tuples if len(elem) > 0]
    print(non_empty_tuples)


def m_6_2_13():
    tuples = [
        (10, 20, 40),
        (40, 50, 60),
        (70, 80, 90),
        (10, 90),
        (1, 2, 3, 4),
        (5, 6, 10, 2, 1, 77),
    ]
    new_tuples = [elem[:-1] + (100,) for elem in tuples]
    print(new_tuples)


# 6.3 Основы работы с кортежами. Часть 2


def m_6_3_1():
    numbers = (
        2,
        3,
        5,
        7,
        -11,
        13,
        17,
        19,
        23,
        29,
        31,
        -6,
        41,
        43,
        47,
        53,
        59,
        61,
        -96,
        71,
        1000,
        -1,
    )
    res = 1
    for x in numbers:
        res *= x
    print(res)


def m_6_3_2():
    data = "Python для продвинутых!"
    res = tuple(data)
    print(res)


def m_6_3_3():
    poet_data = ("Пушкин", 1799, "Санкт-Петербург")
    poet_data = list(poet_data)
    poet_data[-1] = "Москва"
    poet_data = tuple(poet_data)
    print(poet_data)


def m_6_3_4():
    numbers = (
        (10, 10, 10, 12),
        (30, 45, 56, 45),
        (81, 80, 39, 32),
        (1, 2, 3, 4),
        (90, 10),
    )
    res = [sum(elem) / len(elem) for elem in numbers]
    print(res)


def m_6_3_5():
    a, b, c = [int(input()) for _ in range(3)]
    res = (-b / (2 * a), (4 * a * c - b**2) / (4 * a))
    print(res)


def m_6_3_6():
    n = int(input())
    data = [tuple(input().split()) for _ in range(n)]
    [print(*d) for d in data]
    print()
    [print(*d) for d in data if d[-1] in ("4", "5")]


def m_6_3_7():
    n = int(input())
    t1, t2, t3 = 1, 1, 1
    for i in range(n):
        print(t1, end=" ")
        t1, t2, t3 = t2, t3, t1 + t2 + t3
