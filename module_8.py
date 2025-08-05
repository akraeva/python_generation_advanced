# 8. Множества
"""
Модуль посвящен множествам в Python. Рассматриваются математические основы,
операции над множествами, методы, генераторы множеств, а также неизменяемый
тип frozenset и визуализация с помощью диаграмм Эйлера – Венна.
"""


# 8.1 Множества в математике


# 8.2 Операции над множествами, диаграммы Эйлера-Венна


def m_8_2_1():  # Тимур и его команда
    n, m, k, x, y, z = [int(input()) for _ in range(6)]
    print(n + m + k - x - y + z)


def m_8_2_2():  # Книги на прочтение
    n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]

    B1, B2, B3 = (
        n,
        m,
        k,
    )
    b1or2, b2or3, b3or1 = x, y, z
    b123 = t
    b12 = B1 + B2 - b1or2 - (b123)
    b23 = B2 + B3 - b2or3 - (b123)
    b31 = B3 + B1 - b3or1 - (b123)
    b1 = B1 - (b12 + b31 + b123)
    b2 = B2 - (b12 + b23 + b123)
    b3 = B3 - (b23 + b31 + b123)

    print(b1 + b2 + b3)  # прочитали только одну книгу
    print(b12 + b23 + b31)  # прочитали только две книги
    print(
        a - (b1 + b2 + b3 + b12 + b23 + b31 + b123)
    )  # не прочитали ни одной из рекомендованных книг


# 8.3 Введение в множества в Python


# 8.4 Основы работы с множествами


def m_8_4_1():
    numbers = {1.414, 12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324, 2.718, 1.324}
    res = min(numbers) + max(numbers)
    print(res)


def m_8_4_2():
    numbers = {
        20,
        6,
        8,
        18,
        18,
        2,
        4,
        6,
        8,
        10,
        12,
        14,
        16,
        18,
        20,
        12,
        8,
        8,
        10,
        4,
        2,
        2,
        2,
        16,
        20,
    }
    average = sum(numbers) / len(numbers)
    print(average)


def m_8_4_3():
    numbers = {
        9089,
        -67,
        -32,
        1,
        78,
        23,
        -65,
        99,
        9089,
        34,
        -32,
        0,
        -67,
        1,
        11,
        111,
        111,
        1,
        23,
    }
    print(sum(x**2 for x in numbers))


def m_8_4_4():
    fruits = {
        "apple",
        "banana",
        "cherry",
        "avocado",
        "pineapple",
        "apricot",
        "banana",
        "avocado",
        "grapefruit",
    }
    print(*sorted(fruits, reverse=True), sep="\n")


def m_8_4_5():  # Количество различных символов
    s = input()
    print(len(set(s)))


def m_8_4_6():  # Неповторимые цифры
    s = input()
    print("YES" if len(s) == len(set(s)) else "NO")


def m_8_4_7():  # Все 10 цифр
    s1, s2 = input(), input()
    ref = [str(i) for i in range(10)]
    print("YES" if sorted(set(s1 + s2)) == ref else "NO")


def m_8_4_8():  # Одинаковые наборы
    s1, s2 = input(), input()
    print("YES" if sorted(set(s1)) == sorted(set(s2)) else "NO")


def m_8_4_9():  # Три слова
    s1, s2, s3 = input().split()
    print(
        "YES"
        if sorted(set(s1)) == sorted(set(s2)) and sorted(set(s1)) == sorted(set(s3))
        else "NO"
    )


# 8.5 Методы множеств. Часть 1


def m_8_5_1():  # Уникальные символы 1
    data = [input().lower() for _ in range(int(input()))]
    for d in data:
        print(len(set(d)))


def m_8_5_2():  # Уникальные символы 2
    data = [input().lower() for _ in range(int(input()))]
    print(len(set("".join(data))))


def m_8_5_3():  # Количество слов в тексте
    text = input().lower()
    for i in ".,;:-?!":
        text = text.replace(i, "")
    print(len(set(text.split())))


def m_8_5_4():  # Встречалось ли число раньше?
    nums = map(int, input().split())
    chek = set()
    for i in nums:
        if i in chek:
            print("YES")
        else:
            print("NO")
            chek.add(i)


def m_8_5_5():  # Счетчик верных решений
    count = int(input())
    users = set()
    res = 0
    for _ in range(count):
        user = input().split(": ")
        if user[-1] == "Correct":
            users.add(user[0])
            res += 1
    if res == 0:
        print("Вы можете стать первым, кто решит эту задачу")
    else:
        res = int(res * 1000 / count)
        print(
            f"Верно решили {len(users)} учащихся\nИз всех попыток {res//10 + (1 if res % 10 >= 5 else 0)}% верных"
        )


# 8.6 Методы множеств. Часть 2


def m_8_6_1():  # Количество совпадающих
    print(len(set(input().split()) & set(input().split())))


def m_8_6_2():  # Общие числа
    print(*sorted(set(map(int, input().split())) & set(map(int, input().split()))))


def m_8_6_3():  # Числа первой строки
    print(*sorted(set(map(int, input().split())) - set(map(int, input().split()))))


def m_8_6_4():  # Общие цифры
    n = int(input())
    nums = [set(int(i) for i in input()) for _ in range(n)]
    res = nums[0]
    for i in nums[1:]:
        res &= i
    print(*sorted(res))


# 8.7 Методы множеств. Часть 3


def m_8_7_1():  # Одинаковые цифры
    num1, num2 = set(input()), input()
    print(("YES", "NO")[num1.isdisjoint(num2)])


def m_8_7_2():  # Все цифры
    num1, num2 = input(), set(input())
    print(("NO", "YES")[num2.issubset(num1)])


def m_8_7_3():  # Урок информатики
    rat1, rat2, rat3 = (set(map(int, input().split())) for _ in range(3))
    print(*sorted(rat1 & rat2 - rat3, reverse=True))


def m_8_7_4():  # Урок математики
    rat1, rat2, rat3 = (set(map(int, input().split())) for _ in range(3))
    print(*sorted((rat1 | rat2 | rat3) - (rat1 & rat2 & rat3)))


def m_8_7_5():  # Урок физики
    rat1, rat2, rat3 = (set(map(int, input().split())) for _ in range(3))
    print(*sorted(rat3 - (rat1 | rat2), reverse=True))


def m_8_7_6():  # Урок биологии
    rat1, rat2, rat3 = (set(map(int, input().split())) for _ in range(3))
    print(*sorted(set(range(11)) - (rat3 | rat1 | rat2)))


# 8.8 Генераторы множеств и frozenset


def m_8_8_1():
    items = [
        10,
        "30",
        30,
        10,
        "56",
        34,
        "12",
        90,
        89,
        34,
        45,
        "67",
        12,
        10,
        90,
        23,
        "45",
        56,
        "56",
        1,
        5,
        "6",
        5,
    ]
    print(*sorted({int(i) for i in items}))


def m_8_8_2():
    words = [
        "Plum",
        "Grapefruit",
        "apple",
        "orange",
        "pomegranate",
        "Cranberry",
        "lime",
        "Lemon",
        "grapes",
        "persimmon",
        "tangerine",
        "Watermelon",
        "currant",
        "Almond",
    ]
    print(*sorted({i[0].lower() for i in words}))


def m_8_8_3():
    sentence = """My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges."""

    words = set(
        sentence.translate(str.maketrans("", "", ".,;:!?()'\"")).lower().split()
    )
    print(*sorted(words))


def m_8_8_4():
    sentence = """My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges."""

    words = {
        w.strip(".,;:!?()'\"").lower()
        for w in sentence.split()
        if len(w.strip(".,;:!?()'\"")) < 4
    }
    print(*sorted(words))


def m_8_8_5():
    files = [
        "python.png",
        "qwerty.py",
        "stepik.png",
        "beegeek.org",
        "windows.pnp",
        "pen.txt",
        "phone.py",
        "book.txT",
        "board.pNg",
        "keyBoard.jpg",
        "Python.PNg",
        "apple.jpeg",
        "png.png",
        "input.tXt",
        "split.pop",
        "solution.Py",
        "stepik.org",
        "kotlin.ko",
        "github.git",
    ]
    print(*sorted({i.lower() for i in files if i.lower()[-3:] == "png"}))
