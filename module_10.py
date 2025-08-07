# 10. Словари
"""
Этот модуль посвящен словарям в Python. Рассматриваются основной
функционал при работе со словарями, методы словарей, а также
вложенные словари и генераторы словарей.
"""


# 10.1 Введение в словари в Python


# 10.2 Основы работы со словарями


def m_10_2_1():
    my_dict = {
        1.12: "aa",
        67.9: 45,
        3.11: "ccc",
        7.9: "dd",
        9.2: "ee",
        7.1: "ff",
        0.12: "qq",
        1.91: "aa",
        10.12: [1, 2, 3],
        99.0: {9, 0, 1},
    }
    print(min(my_dict) + max(my_dict))


def m_10_2_2():
    users = [
        {"name": "Todd", "phone": "551-1414", "email": "todd@gmail.com"},
        {"name": "Helga", "phone": "555-1618", "email": "helga@mail.net"},
        {"name": "Olivia", "phone": "449-3141", "email": ""},
        {"name": "LJ", "phone": "555-2718", "email": "lj@gmail.net"},
        {"name": "Ruslan", "phone": "422-145-9098", "email": "rus-lan.cha@yandex.ru"},
        {"name": "John", "phone": "233-421-32", "email": ""},
        {"name": "Lara", "phone": "+7998-676-2532", "email": "g.lara89@gmail.com"},
        {"name": "Alina", "phone": "+7948-799-2434", "email": "ali.ch.b@gmail.com"},
        {"name": "Robert", "phone": "420-2011", "email": ""},
        {"name": "Riyad", "phone": "128-8890-128", "email": "r.mahrez@mail.net"},
        {"name": "Khabib", "phone": "+7995-600-9080", "email": "kh.nurmag@gmail.com"},
        {"name": "Olga", "phone": "6449-314-1213", "email": ""},
        {"name": "Roman", "phone": "+7459-145-8059", "email": "roma988@mail.ru"},
        {"name": "Maria", "phone": "12-129-3148", "email": "m.sharapova@gmail.com"},
        {"name": "Fedor", "phone": "+7445-341-0545", "email": ""},
        {"name": "Tim", "phone": "242-449-3141", "email": "timm.ggg@yandex.ru"},
    ]

    print(*sorted(i["name"] for i in users if i["phone"][-1] == "8"))


def m_10_2_3():
    users = [
        {"name": "Todd", "phone": "551-1414", "email": "todd@gmail.com"},
        {"name": "Helga", "phone": "555-1618"},
        {"name": "Olivia", "phone": "449-3141", "email": ""},
        {"name": "LJ", "phone": "555-2718", "email": "lj@gmail.net"},
        {"name": "Ruslan", "phone": "422-145-9098", "email": "rus-lan.cha@yandex.ru"},
        {"name": "John", "phone": "233-421-32", "email": ""},
        {"name": "Lara", "phone": "+7998-676-2532", "email": "g.lara89@gmail.com"},
        {"name": "Alina", "phone": "+7948-799-2434"},
        {"name": "Robert", "phone": "420-2011", "email": ""},
        {"name": "Riyad", "phone": "128-8890-128", "email": "r.mahrez@mail.net"},
        {"name": "Khabib", "phone": "+7995-600-9080", "email": "kh.nurmag@gmail.com"},
        {"name": "Olga", "phone": "6449-314-1213", "email": ""},
        {"name": "Roman", "phone": "+7459-145-8059"},
        {"name": "Maria", "phone": "12-129-3148", "email": "m.sharapova@gmail.com"},
        {"name": "Fedor", "phone": "+7445-341-0545", "email": ""},
        {"name": "Tim", "phone": "242-449-3141", "email": "timm.ggg@yandex.ru"},
    ]
    print(*sorted(i["name"] for i in users if "email" not in i or not i["email"]))


def m_10_2_4():  # Строковое представление
    nums = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }
    print(*(nums[i] for i in list(map(int, input()))))


def m_10_2_5():  # Информация об учебных курса
    courses = {
        "CS101": {"num": "3004", "teacher": "Хайнс", "time": "8:00"},
        "CS102": {"num": "4501", "teacher": "Альварадо", "time": "9:00"},
        "CS103": {"num": "6755", "teacher": "Рич", "time": "10:00"},
        "NT110": {"num": "1244", "teacher": "Берк", "time": "11:00"},
        "CM241": {"num": "1411", "teacher": "Ли", "time": "13:00"},
    }
    c = input()
    print(f'{c}: {", ".join((courses[c].values())) }')


def m_10_2_6():  # Набор сообщений
    chars = {
        ".": "1",
        ",": "1" * 2,
        "?": "1" * 3,
        "!": "1" * 4,
        ":": "1" * 5,
        "A": "2",
        "B": "2" * 2,
        "C": "2" * 3,
        "D": "3",
        "E": "3" * 2,
        "F": "3" * 3,
        "G": "4",
        "H": "4" * 2,
        "I": "4" * 3,
        "J": "5",
        "K": "5" * 2,
        "L": "5" * 3,
        "M": "6",
        "N": "6" * 2,
        "O": "6" * 3,
        "P": "7",
        "Q": "7" * 2,
        "R": "7" * 3,
        "S": "7" * 4,
        "T": "8",
        "U": "8" * 2,
        "V": "8" * 3,
        "W": "9",
        "X": "9" * 2,
        "Y": "9" * 3,
        "Z": "9" * 4,
        " ": "0",
    }
    sms = input().upper()
    print("".join(chars[i] for i in sms if i in chars))


def m_10_2_7():  # Код Морзе
    letters = [c for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"]
    morse = [
        ".-",
        "-...",
        "-.-.",
        "-..",
        ".",
        "..-.",
        "--.",
        "....",
        "..",
        ".---",
        "-.-",
        ".-..",
        "--",
        "-.",
        "---",
        ".--.",
        "--.-",
        ".-.",
        "...",
        "-",
        "..-",
        "...-",
        ".--",
        "-..-",
        "-.--",
        "--..",
        "-----",
        ".----",
        "..---",
        "...--",
        "....-",
        ".....",
        "-....",
        "--...",
        "---..",
        "----.",
    ]
    code = dict(zip(letters, morse))
    print(*(code[i] for i in input().upper() if i in code))


# 10.3 Методы словарей


def m_10_3_1():
    result = {}
    result.update((i, i**2) for i in range(1, 16))


def m_10_3_2():
    dict1 = {
        "a": 100,
        "z": 333,
        "b": 200,
        "c": 300,
        "d": 45,
        "e": 98,
        "t": 76,
        "q": 34,
        "f": 90,
        "m": 230,
    }
    dict2 = {
        "a": 300,
        "b": 200,
        "d": 400,
        "t": 777,
        "c": 12,
        "p": 123,
        "w": 111,
        "z": 666,
    }
    result = {}
    result.update(
        ((k, dict1.get(k, 0) + dict2.get(k, 0)) for k in set(dict1) | set(dict2))
    )


def m_10_3_3():
    text = "footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff"
    result = {}
    result.update((i, text.count(i)) for i in set(text))


def m_10_3_4():
    s = "orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley"
    # res = dict((w, s.count(w)) for w in s.split())  >> коротко, но долго
    res = {}
    for w in s.split():
        res[w] = res.get(w, 0) + 1
    print(min(w for w in res if res.get(w) == max(res.values())))


def m_10_3_5():
    pets = [
        ("Hatiko", "Parker", "Wilson", 50),
        ("Rusty", "Josh", "King", 25),
        ("Fido", "John", "Smith", 28),
        ("Butch", "Jake", "Smirnoff", 18),
        ("Odi", "Emma", "Wright", 18),
        ("Balto", "Josh", "King", 25),
        ("Barry", "Josh", "King", 25),
        ("Snape", "Hannah", "Taylor", 40),
        ("Horry", "Martha", "Robinson", 73),
        ("Giro", "Alex", "Martinez", 65),
        ("Zooma", "Simon", "Nevel", 32),
        ("Lassie", "Josh", "King", 25),
        ("Chase", "Martha", "Robinson", 73),
        ("Ace", "Martha", "Williams", 38),
        ("Rocky", "Simon", "Nevel", 32),
    ]

    result = {}
    for i in pets:
        result.setdefault(i[1:], []).append(i[0])


def m_10_3_6():  # Самое редкое слово
    text = (w.strip(".,!?:;-") for w in input().lower().split())
    words = {}
    for w in text:
        words[w] = words.get(w, 0) + 1
    print(min(w for w in words if words.get(w) == min(words.values())))


def m_10_3_7():  # Исправление дубликатов
    id_str = input().split()
    id_counter = {}
    res = []

    for i in id_str:
        id_counter[i] = id_counter.get(i, -1) + 1
        res.append(i if id_counter[i] == 0 else f"{i}_{id_counter[i]}")
    print(*res)


# 10.4 Задачи на словари


def m_10_4_1():  # Словарь программиста
    slang = {
        k.lower(): v for k, v in (input().split(": ") for _ in range(int(input())))
    }
    for _ in range(int(input())):
        print(slang.get(input().lower(), "Не найдено"))


def m_10_4_2():  # Анаграммы 1
    s1, s2 = (input()), (input())
    print(("NO", "YES")[sorted(s1) == sorted(s2)])


def m_10_4_3():  # Анаграммы 2
    def to_dict(s):
        return {i: s.lower().count(i) for i in set(s.lower()) if i not in " .,!?:;-"}

    print("YES" if to_dict(input()) == to_dict(input()) else "NO")


def m_10_4_4():  # Словарь синонимов
    thesaurus = {}
    for _ in range(int(input())):
        s = input().split()
        thesaurus[s[0]] = s[1]
        thesaurus[s[1]] = s[0]
    print(thesaurus[input()])


def m_10_4_5():  # Страны и города
    city_dict = {
        city: country
        for _ in range(int(input()))
        for country, *cities in [input().split()]
        for city in cities
    }

    for _ in range(int(input())):
        print(city_dict[input()])


def m_10_4_6():  # Телефонная книга
    book = {}
    for _ in range(int(input())):
        tel, name = input().lower().split()
        book.setdefault(name, []).append(tel)

    for _ in range(int(input())):
        print(*book.get(input().lower(), ["абонент не найден"]))


def m_10_4_7():  # Секретное слово
    word = input()
    code = {word.count(ch): ch for ch in set(word)}

    for _ in range(int(input())):
        ch, count = input().split(": ")
        word = word.replace(code[int(count)], ch)
    print(word)


# 10.5 Вложенные словари и генераторы словарей


def m_10_5_1():
    numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
    result = {i: numbers[i] ** 2 for i in range(len(numbers))}  # noqa: F841


def m_10_5_2():
    colors = {
        "c1": "Red",
        "c2": "Grey",
        "c3": None,
        "c4": "Green",
        "c5": "Yellow",
        "c6": "Pink",
        "c7": "Orange",
        "c8": None,
        "c9": "White",
        "c10": "Black",
        "c11": "Violet",
        "c12": "Gold",
        "c13": None,
        "c14": "Amber",
        "c15": "Azure",
        "c16": "Beige",
        "c17": "Bronze",
        "c18": None,
        "c19": "Lilac",
        "c20": "Pearl",
        "c21": None,
        "c22": "Sand",
        "c23": None,
    }
    result = {i: colors[i] for i in colors if colors[i]}


def m_10_5_3():
    favorite_numbers = {
        "timur": 17,
        "ruslan": 7,
        "larisa": 19,
        "roman": 123,
        "rebecca": 293,
        "ronald": 76,
        "dorothy": 62,
        "harold": 36,
        "matt": 314,
        "kim": 451,
        "rosaly": 18,
        "rustam": 89,
        "soltan": 111,
        "amir": 654,
        "dima": 390,
        "amiran": 777,
        "geor": 999,
        "sveta": 75,
        "rita": 909,
        "kirill": 404,
        "olga": 271,
        "anna": 55,
        "madlen": 876,
    }
    result = {
        i: favorite_numbers[i]
        for i in favorite_numbers
        if favorite_numbers[i] in range(10, 100)
    }


def m_10_5_4():
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    result = {months[i]: i for i in months}


def m_10_5_5():
    s = "1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice"
    result = {int(i): w for part in s.split() for i, w in [part.split(":")]}


def m_10_5_6():
    numbers = [
        34,
        10,
        4,
        6,
        10,
        23,
        90,
        100,
        21,
        35,
        95,
        1,
        36,
        38,
        19,
        1,
        6,
        87,
        1000,
        13456,
        360,
    ]
    result = {n: [d for d in range(1, n + 1) if n % d == 0] for n in numbers}


def m_10_5_7():
    words = [
        "hello",
        "bye",
        "yes",
        "no",
        "python",
        "apple",
        "maybe",
        "stepik",
        "beegeek",
    ]
    result = {word: [ord(ch) for ch in word] for word in words}


def m_10_5_8():
    letters = {
        0: "A",
        1: "B",
        2: "C",
        3: "D",
        4: "E",
        5: "F",
        6: "G",
        7: "H",
        8: "I",
        9: "J",
        10: "K",
        11: "L",
        12: "M",
        13: "N",
        14: "O",
        15: "P",
        16: "Q",
        17: "R",
        18: "S",
        19: "T",
        20: "U",
        21: "V",
        22: "W",
        23: "X",
        24: "Y",
        26: "Z",
    }
    remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
    result = {i: letters[i] for i in letters if i not in remove_keys}


def m_10_5_9():
    students = {
        "Timur": (170, 75),
        "Ruslan": (180, 105),
        "Soltan": (192, 68),
        "Roman": (175, 70),
        "Madlen": (160, 50),
        "Stefani": (165, 70),
        "Tom": (190, 90),
        "Jerry": (180, 87),
        "Anna": (172, 67),
        "Scott": (168, 78),
        "John": (186, 79),
        "Alex": (195, 120),
        "Max": (200, 110),
        "Barak": (180, 89),
        "Donald": (170, 80),
        "Rustam": (186, 100),
        "Alice": (159, 59),
        "Rita": (170, 80),
        "Mary": (175, 69),
        "Jane": (190, 80),
    }
    result = {
        name: info for name, info in students.items() if info[0] > 167 and info[-1] < 75
    }


def m_10_5_10():
    tuples = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (10, 11, 12),
        (13, 14, 15),
        (16, 17, 18),
        (19, 20, 21),
        (22, 23, 24),
        (25, 26, 27),
        (28, 29, 30),
        (31, 32, 33),
        (34, 35, 36),
    ]
    result = {n1: (n2, n3) for (n1, n2, n3) in tuples}


def m_10_5_11():
    student_ids = [
        "S001",
        "S002",
        "S003",
        "S004",
        "S005",
        "S006",
        "S007",
        "S008",
        "S009",
        "S010",
        "S011",
        "S012",
        "S013",
    ]
    student_names = [
        "Camila Rodriguez",
        "Juan Cruz",
        "Dan Richards",
        "Sam Boyle",
        "Batista Cesare",
        "Francesco Totti",
        "Khalid Hussain",
        "Ethan Hawke",
        "David Bowman",
        "James Milner",
        "Michael Owen",
        "Gary Oldman",
        "Tom Hardy",
    ]
    student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]
    result = [
        {sid: {name: grade}}
        for (sid, name, grade) in zip(student_ids, student_names, student_grades)
    ]
