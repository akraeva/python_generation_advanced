# 15. Функции
"""
Этот модуль посвящен функциям в Python. Рассматриваются позиционные
и именованные аргументы, функции с переменным количеством аргументов,
функции высшего порядка, анонимные функции, некоторые встроенные функции,
а также основные парадигмы программирования.
"""

# 15.1 Необязательные и именованные аргументы


def m_15_1_1():
    def matrix(n=1, m=None, value=0):
        if not m:
            m = n
        res = [[value for _ in range(m)] for _ in range(n)]
        return res


# 15.2 Функции с переменным количеством аргументов


def m_15_2_1():
    def count_args(*args):
        return len(args)


def m_15_2_2():
    def sq_sum(*args):
        return sum(a**2 for a in args)


def m_15_2_3():
    def mean(*args):
        nums = [x for x in args if type(x) in (int, float)]
        return sum(nums) / len(nums) if nums else 0


def m_15_2_4():
    def greet(name, *args):
        return f'Hello, {" and ".join([name, *args])}!'


def m_15_2_5():
    def print_products(*args):
        products = [a for a in args if isinstance(a, str) and a != ""]
        if not products:
            print("Нет продуктов")
        else:
            i = 1
            for p in products:
                print(f"{i}) {p}")
                i += 1


def m_15_2_6():
    def info_kwargs(**kwargs):
        for key in sorted(kwargs):
            print(f"{key}: {kwargs[key]}")


# 15.3 Парадигмы программирования


# 15.4 Функции как объекты


def m_15_4_1():
    def avrg(nums):
        return sum(nums) / len(nums)

    numbers = [
        (10, 10, 10),
        (30, 45, 56),
        (81, 39),
        (1, 2, 3),
        (12,),
        (-2, -4, 100),
        (1, 2, 99),
        (89, 9, 34),
        (10, 20, 30, -2),
        (50, 40, 50),
        (34, 78, 65),
        (-5, 90, -1, -5),
        (1, 2, 3, 4, 5, 6),
        (-9, 8, 4),
        (90, 1, -45, -21),
    ]
    print(min(numbers, key=avrg))
    print(max(numbers, key=avrg))


def m_15_4_2():
    def segment(c):
        x, y = c
        return (x**2 + y**2) ** 0.5

    points = [
        (-1, 1),
        (5, 6),
        (12, 0),
        (4, 3),
        (0, 1),
        (-3, 2),
        (0, 0),
        (-1, 3),
        (2, 0),
        (3, 0),
        (-9, 1),
        (3, 6),
        (8, 8),
    ]

    points.sort(key=segment)
    print(points)


def m_15_4_3():
    def min_max_sum(nums):
        return min(nums) + max(nums)

    numbers = [
        (10, 10, 10),
        (30, 45, 56),
        (81, 80, 39),
        (1, 2, 3),
        (12, 45, 67),
        (-2, -4, 100),
        (1, 2, 99),
        (89, 90, 34),
        (10, 20, 30),
        (50, 40, 50),
        (34, 78, 65),
        (-5, 90, -1),
    ]

    print(sorted(numbers, key=min_max_sum))


def m_15_4_4():  # Сортируй как хочешь
    def sort_field(data):
        return data[n - 1]

    athletes = [
        ("Дима", 10, 130, 35),
        ("Тимур", 11, 135, 39),
        ("Руслан", 9, 140, 33),
        ("Рустам", 10, 128, 30),
        ("Амир", 16, 170, 70),
        ("Рома", 16, 188, 100),
        ("Матвей", 17, 168, 68),
        ("Петя", 15, 190, 90),
    ]

    n = int(input())
    for a in sorted(athletes, key=sort_field):
        print(*a)


def m_15_4_5():  # Математические функции
    import math

    def sqr(x):
        return x**2

    def сub(x):
        return x**3

    def sqrt(x):
        return x**0.5

    def mod(x):
        return abs(x)

    def sin(x):
        return math.sin(x)

    functions = {
        "квадрат": sqr,
        "куб": сub,
        "корень": sqrt,
        "модуль": mod,
        "синус": sin,
    }

    num = int(input())
    print(functions[input().lower()](num))


def m_15_4_6():  # Интересная сортировка-1
    def sum_digits(num):
        return sum(int(n) for n in num)

    nums = input().split()
    print(*sorted(nums, key=sum_digits))


def m_15_4_7():  # Интересная сортировка-2
    def sum_digits(num):
        return sum(int(n) for n in num)

    def digit(s):
        return int(s)

    nums = input().split()
    nums.sort(key=digit)
    print(*sorted(nums, key=sum_digits))


# 15.5 Функции высшего порядка


def m_15_5_1():
    def map(function, items):
        result = []
        for item in items:
            result.append(function(item))
        return result

    def round_2(num):
        n = int(num * 1000)
        return (n // 10 + (0 if n % 10 < 5 else 1)) / 100

    numbers = [
        3.56773,
        5.57668,
        4.00914,
        56.24241,
        9.01344,
        32.12013,
        23.22222,
        90.09873,
        45.45,
        314.1528,
        2.71828,
        1.41546,
    ]

    print(*map(round_2, numbers), sep="\n")


def m_15_5_2():
    def map(function, items):
        result = []
        for item in items:
            result.append(function(item))
        return result

    def filter(function, items):
        result = []
        for item in items:
            if function(item):
                result.append(item)
        return result

    def cub(x):
        return x**3

    def condition(x):
        return x in range(100, 1000) and x % 5 == 2

    numbers = [
        1014,
        1321,
        675,
        1215,
        56,
        1386,
        1385,
        431,
        1058,
        486,
        1434,
        696,
        1016,
        1084,
        424,
        1189,
        475,
        95,
        1434,
        1462,
        815,
        776,
        657,
        1225,
        912,
        537,
        1478,
        1176,
        544,
        488,
        668,
        944,
        207,
        266,
        1309,
        1027,
        257,
        1374,
        1289,
        1155,
        230,
        866,
        708,
        144,
        1434,
        1163,
        345,
        394,
        560,
        338,
        232,
        182,
        1438,
        1127,
        928,
        1309,
        98,
        530,
        1013,
        898,
        669,
        105,
        130,
        1363,
        947,
        72,
        1278,
        166,
        904,
        349,
        831,
        1207,
        1496,
        370,
        725,
        926,
        175,
        959,
        1282,
        336,
        1268,
        351,
        1439,
        186,
        273,
        1008,
        231,
        138,
        142,
        433,
        456,
        1268,
        1018,
        1274,
        387,
        120,
        340,
        963,
        832,
        1127,
    ]

    print(*map(cub, filter(condition, numbers)), sep="\n")


def m_15_5_3():
    def reduce(operation, items, initial_value):
        acc = initial_value
        for item in items:
            acc = operation(acc, item)
        return acc

    def sqr(x):
        return x**2

    def sum_of_sqrs(acc, x):
        return acc + x**2

    numbers = [
        97,
        42,
        9,
        32,
        3,
        45,
        31,
        77,
        -1,
        11,
        -2,
        75,
        5,
        51,
        34,
        28,
        46,
        1,
        -8,
        84,
        16,
        51,
        90,
        56,
        65,
        90,
        23,
        35,
        11,
        -10,
        70,
        90,
        90,
        12,
        96,
        58,
        -8,
        -4,
        91,
        76,
        94,
        60,
        72,
        43,
        4,
        -6,
        -5,
        51,
        58,
        60,
        30,
        38,
        67,
        62,
        36,
        72,
        34,
        82,
        62,
        -1,
        60,
        82,
        87,
        81,
        -7,
        57,
        26,
        36,
        17,
        43,
        80,
        40,
        75,
        94,
        91,
        64,
        38,
        72,
        29,
        84,
        38,
        35,
        7,
        54,
        31,
        95,
        78,
        27,
        82,
        1,
        64,
        94,
        31,
        29,
        -8,
        98,
        24,
        61,
        7,
        73,
    ]

    print(reduce(sum_of_sqrs, numbers, 0))  # print(sum(map(sqr, numbers)))


def m_15_5_4():
    def map(function, items):
        result = []
        for item in items:
            result.append(function(item))
        return result

    def filter(function, items):
        result = []
        for item in items:
            if function(item):
                result.append(item)
        return result

    def condition(x):
        return abs(x) in range(10, 100) and x % 7 == 0

    def sqr(x):
        return x**2

    numbers = [
        77,
        293,
        28,
        242,
        213,
        285,
        71,
        286,
        144,
        276,
        61,
        298,
        280,
        214,
        156,
        227,
        228,
        51,
        -4,
        202,
        58,
        99,
        270,
        219,
        94,
        253,
        53,
        235,
        9,
        158,
        49,
        183,
        166,
        205,
        183,
        266,
        180,
        6,
        279,
        200,
        208,
        231,
        178,
        201,
        260,
        -35,
        152,
        115,
        79,
        284,
        181,
        92,
        286,
        98,
        271,
        259,
        258,
        196,
        -8,
        43,
        2,
        128,
        143,
        43,
        297,
        229,
        60,
        254,
        -9,
        5,
        187,
        220,
        -8,
        111,
        285,
        5,
        263,
        187,
        192,
        -9,
        268,
        -9,
        23,
        71,
        135,
        7,
        -161,
        65,
        135,
        29,
        148,
        242,
        33,
        35,
        211,
        5,
        161,
        46,
        159,
        23,
        169,
        23,
        172,
        184,
        -7,
        228,
        129,
        274,
        73,
        197,
        272,
        54,
        278,
        26,
        280,
        13,
        171,
        2,
        79,
        -2,
        183,
        10,
        236,
        276,
        4,
        29,
        -10,
        41,
        269,
        94,
        279,
        129,
        39,
        92,
        -63,
        263,
        219,
        57,
        18,
        236,
        291,
        234,
        10,
        250,
        0,
        64,
        172,
        216,
        30,
        15,
        229,
        205,
        123,
        -105,
    ]

    print(sum(map(sqr, filter(condition, numbers))))


def m_15_5_5():  #
    def func_apply(function, items):
        return list(map(function, items))


# 15.6 Встроенные функции map(), filter(), reduce()


# 15.7 Анонимные функции. Часть 1


def m_15_7_1():
    from functools import reduce

    floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
    words = [
        "racecar",
        "akinremi",
        "deed",
        "temidayo",
        "omoseun",
        "civic",
        "TATTARRATTAT",
        "malayalam",
        "nun",
    ]
    numbers = [4, 6, 9, 23, 5]

    map_result = list(map(lambda num: round(num**2, 1), floats))
    filter_result = list(
        filter(lambda name: name == name[::-1] and len(name) > 4, words)
    )
    reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)

    print(map_result)
    print(filter_result)
    print(reduce_result)


def m_15_7_2():
    from functools import reduce

    data = [
        ["Tokyo", 35676000, "primary"],
        ["New York", 19354922, "nan"],
        ["Mexico City", 19028000, "primary"],
        ["Mumbai", 18978000, "admin"],
        ["Sao Paulo", 18845000, "admin"],
        ["Delhi", 15926000, "admin"],
        ["Shanghai", 14987000, "admin"],
        ["Kolkata", 14787000, "admin"],
        ["Los Angeles", 12815475, "nan"],
        ["Dhaka", 12797394, "primary"],
        ["Buenos Aires", 12795000, "primary"],
        ["Karachi", 12130000, "admin"],
        ["Cairo", 11893000, "primary"],
        ["Rio de Janeiro", 11748000, "admin"],
        ["Osaka", 11294000, "admin"],
        ["Beijing", 11106000, "primary"],
        ["Manila", 11100000, "primary"],
        ["Moscow", 10452000, "primary"],
        ["Istanbul", 10061000, "admin"],
        ["Paris", 9904000, "primary"],
    ]

    res = reduce(
        lambda acc, s: acc + ", " + s,
        sorted(
            map(
                lambda name: name[0],
                list(
                    filter(
                        lambda city: city[2] == "primary" and city[1] > 10000000, data
                    )
                ),
            )
        ),
    )

    print(f"Cities: {res}")


# 15.8 Анонимные функции. Часть 2


def m_15_8_1():
    func = lambda x: x % 19 == 0 or x % 13 == 0


def m_15_8_2():
    func = lambda x: x[0].lower() == "a" and x[-1].lower() == "a"


def m_15_8_3():
    is_non_negative_num = (
        lambda x: x[0] != "-"
        and len(x.split(".")) <= 2
        and x.split(".")[0].isdigit()
        and x.split(".")[-1].isdigit()
    )


def m_15_8_4():
    is_num = lambda x: (
        False
        if "-" in x and x[0] != "-"
        else (not x.strip("0123456789.-")) and x.count(".") < 2 and x.count("-") < 2
    )


def m_15_8_5():
    words = [
        "beverage",
        "monday",
        "abroad",
        "bias",
        "abuse",
        "abolish",
        "abuse",
        "abuse",
        "bid",
        "wednesday",
        "able",
        "betray",
        "accident",
        "abduct",
        "bigot",
        "bet",
        "abandon",
        "besides",
        "access",
        "friday",
        "bestow",
        "abound",
        "absent",
        "beware",
        "abundant",
        "abnormal",
        "aboard",
        "about",
        "accelerate",
        "abort",
        "thursday",
        "tuesday",
        "sunday",
        "berth",
        "beyond",
        "benevolent",
        "abate",
        "abide",
        "bicycle",
        "beside",
        "accept",
        "berry",
        "bewilder",
        "abrupt",
        "saturday",
        "accessory",
        "absorb",
    ]
    print(*sorted(filter(lambda x: len(x) == 6, words)))


def m_15_8_6():
    numbers = [
        46,
        61,
        34,
        17,
        56,
        26,
        93,
        1,
        3,
        82,
        71,
        37,
        80,
        27,
        77,
        94,
        34,
        100,
        36,
        81,
        33,
        81,
        66,
        83,
        41,
        80,
        80,
        93,
        40,
        34,
        32,
        16,
        5,
        16,
        40,
        93,
        36,
        65,
        8,
        19,
        8,
        75,
        66,
        21,
        72,
        32,
        41,
        59,
        35,
        64,
        49,
        78,
        83,
        27,
        57,
        53,
        43,
        35,
        48,
        17,
        19,
        40,
        90,
        57,
        77,
        56,
        80,
        95,
        90,
        27,
        26,
        6,
        4,
        23,
        52,
        39,
        63,
        74,
        15,
        66,
        29,
        88,
        94,
        37,
        44,
        2,
        38,
        36,
        32,
        49,
        5,
        33,
        60,
        94,
        89,
        8,
        36,
        94,
        46,
        33,
    ]
    print(
        *(
            map(
                lambda x: x // 2 if x % 2 == 0 else x,
                filter(lambda n: n <= 47 or n % 2 == 0, numbers),
            )
        )
    )


def m_15_8_7():
    data = [
        (19542209, "New York"),
        (4887871, "Alabama"),
        (1420491, "Hawaii"),
        (626299, "Vermont"),
        (1805832, "West Virginia"),
        (39865590, "California"),
        (11799448, "Ohio"),
        (10711908, "Georgia"),
        (10077331, "Michigan"),
        (10439388, "Virginia"),
        (7705281, "Washington"),
        (7151502, "Arizona"),
        (7029917, "Massachusetts"),
        (6910840, "Tennessee"),
    ]
    res = sorted(data, key=lambda x: x[-1][-1], reverse=True)
    for count, name in res:
        print(f"{name}: {count}")


def m_15_8_8():
    data = [
        "год",
        "человек",
        "время",
        "дело",
        "жизнь",
        "день",
        "рука",
        "раз",
        "работа",
        "слово",
        "место",
        "лицо",
        "друг",
        "глаз",
        "вопрос",
        "дом",
        "сторона",
        "страна",
        "мир",
        "случай",
        "голова",
        "ребенок",
        "сила",
        "конец",
        "вид",
        "система",
        "часть",
        "город",
        "отношение",
        "женщина",
        "деньги",
    ]
    print(*sorted(sorted(data), key=lambda x: len(x)))


def m_15_8_9():
    mixed_list = [
        "tuesday",
        "abroad",
        "abuse",
        "beside",
        "monday",
        "abate",
        "accessory",
        "absorb",
        1384878,
        "sunday",
        "about",
        454805,
        "saturday",
        "abort",
        2121919,
        2552839,
        977970,
        1772933,
        1564063,
        "abduct",
        901271,
        2680434,
        "bicycle",
        "accelerate",
        1109147,
        942908,
        "berry",
        433507,
        "bias",
        "bestow",
        1875665,
        "besides",
        "bewilder",
        1586517,
        375290,
        1503450,
        2713047,
        "abnormal",
        2286106,
        242192,
        701049,
        2866491,
        "benevolent",
        "bigot",
        "abuse",
        "abrupt",
        343772,
        "able",
        2135748,
        690280,
        686008,
        "beyond",
        2415643,
        "aboard",
        "bet",
        859105,
        "accident",
        2223166,
        894187,
        146564,
        1251748,
        2851543,
        1619426,
        2263113,
        1618068,
        "berth",
        "abolish",
        "beware",
        2618492,
        1555062,
        "access",
        "absent",
        "abundant",
        2950603,
        "betray",
        "beverage",
        "abide",
        "abandon",
        2284251,
        "wednesday",
        2709698,
        "thursday",
        810387,
        "friday",
        2576799,
        2213552,
        1599022,
        "accept",
        "abuse",
        "abound",
        1352953,
        "bid",
        1805326,
        1499197,
        2241159,
        605320,
        2347441,
    ]
    print(max(mixed_list, key=lambda x: x if type(x) == int else 0))


def m_15_8_10():
    mixed_list = [
        "beside",
        48,
        "accelerate",
        28,
        "beware",
        "absorb",
        "besides",
        "berry",
        15,
        65,
        "abate",
        "thursday",
        76,
        70,
        94,
        35,
        36,
        "berth",
        41,
        "abnormal",
        "bicycle",
        "bid",
        "sunday",
        "saturday",
        87,
        "bigot",
        41,
        "abort",
        13,
        60,
        "friday",
        26,
        13,
        "accident",
        "access",
        40,
        26,
        20,
        75,
        13,
        40,
        67,
        12,
        "abuse",
        78,
        10,
        80,
        "accessory",
        20,
        "bewilder",
        "benevolent",
        "bet",
        64,
        38,
        65,
        51,
        95,
        "abduct",
        37,
        98,
        99,
        14,
        "abandon",
        "accept",
        46,
        "abide",
        "beyond",
        19,
        "about",
        76,
        26,
        "abound",
        12,
        95,
        "wednesday",
        "abundant",
        "abrupt",
        "aboard",
        50,
        89,
        "tuesday",
        66,
        "bestow",
        "absent",
        76,
        46,
        "betray",
        47,
        "able",
        11,
    ]
    print(
        *sorted(filter(lambda x: type(x) == int, mixed_list)),
        *sorted(filter(lambda x: type(x) == str, mixed_list)),
        sep=" ",
    )


def m_15_8_11():
    print(*map(lambda x: 255 - int(x), input().split()))


def m_15_8_12():  # Значение многочлена
    from functools import reduce

    def evaluate(coefficients, x):
        c = list(map(int, coefficients.split()))
        x = int(x)
        print(reduce(lambda acc, a: acc * x + a, c))

    evaluate(input(), input())


# 15.9 Встроенные функции any(), all(), zip(), enumerate()


def m_15_9_1():
    def ignore_command(command):
        ignore = [
            "alias",
            "configuration",
            "ip",
            "sql",
            "select",
            "update",
            "exec",
            "del",
            "truncate",
        ]
        return any(map(lambda substr: substr in command, ignore))


def m_15_9_2():
    countries = ["Russia", "USA", "UK", "Germany", "France", "India"]
    capitals = ["Moscow", "Washington", "London", "Berlin", "Paris", "Delhi"]
    population = [
        145_934_462,
        331_002_651,
        80_345_321,
        67_886_011,
        65_273_511,
        1_380_004_385,
    ]

    for country, capital, people in zip(countries, capitals, population):
        print(
            f"{capital} is the capital of {country}, population equal {people} people."
        )


def m_15_9_3():  # Внутри шара
    abscissas = map(float, input().split())
    ordinates = map(float, input().split())
    applicates = map(float, input().split())

    print(
        all(
            x**2 + y**2 + z**2 <= 2**2
            for x, y, z in zip(abscissas, ordinates, applicates)
        )
    )


def m_15_9_4():  # Корректный IP-адрес
    ip_adress = list(
        map(lambda x: x.isdigit() and int(x) in range(0, 256), input().split("."))
    )
    print(len(ip_adress) == 4 and all(ip_adress))


def m_15_9_5():  # Интересные числа
    start, end = int(input()), int(input())
    print(
        *[
            i
            for i in range(start, end + 1)
            if all(int(d) != 0 and i % int(d) == 0 for d in str(i))
        ]
    )


def m_15_9_6():  # Хороший пароль
    pas = input()
    print(
        "YES"
        if len(pas) > 6
        and all(
            [
                any(i.isdigit() for i in pas),
                any(i.isalpha() and i.islower() for i in pas),
                any(i.isalpha() and i.isupper() for i in pas),
            ]
        )
        else "NO"
    )


def m_15_9_7():  # Отличники
    print(
        "YES"
        if all(
            [
                any([input()[-1] == "5" for __ in range(int(input()))])
                for _ in range(int(input()))
            ]
        )
        else "NO"
    )
