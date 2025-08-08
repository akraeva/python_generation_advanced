# 11. Итоговая работа на словари
"""
Этот модуль содержит дополнительные задачи по изученным темам.
Они помогут еще раз закрепить ваши знания, углубить понимание
ключевых концепций и убедиться, что вы освоили материал.
"""

# 11.1 Часть 1


def m_11_1_1():
    my_dict = {
        "C1": [10, 20, 30, 7, 6, 23, 90],
        "C2": [20, 30, 40, 1, 2, 3, 90, 12],
        "C3": [12, 34, 20, 21],
        "C4": [22, 54, 209, 21, 7],
        "C5": [2, 4, 29, 21, 19],
        "C6": [4, 6, 7, 10, 55],
        "C7": [4, 8, 12, 23, 42],
        "C8": [3, 14, 15, 26, 48],
        "C9": [2, 7, 18, 28, 18, 28],
    }

    for i, nums in my_dict.items():
        my_dict[i] = [n for n in nums if n <= 20]


def m_11_1_2():
    emails = {
        "nosu.edu": ["timyr", "joseph", "svetlana.gaeva", "larisa.mamuk"],
        "gmail.com": ["ruslan.chaika", "rustam.mini", "stepik-best"],
        "msu.edu": ["apple.fruit", "beegeek", "beegeek.school"],
        "yandex.ru": ["surface", "google"],
        "hse.edu": ["tomas-henders", "cream.soda", "zivert"],
        "mail.ru": ["angel.down", "joanne", "the.fame.moster"],
    }
    res = [f"{name}@{domain}" for domain, names in emails.items() for name in names]
    print(*sorted(res), sep="\n")


# 11.2 Часть 2


def m_11_2_1():  # Минутка генетики
    d = {"G": "C", "C": "G", "T": "A", "A": "U"}
    print("".join(d[i] for i in input()))


def m_11_2_2():  # Порядковый номер
    d = {}
    res = []
    for i in input().split():
        d[i] = d.get(i, 0) + 1
        res.append(d[i])
    print(*res)


def m_11_2_3():  # Scrabble game
    d = {1: "AEILNORSTU", 2: "DG", 3: "BCMP", 4: "FHVWY", 5: "K", 8: "JX", 10: "QZ"}

    points = {ch: n for n, chs in d.items() for ch in chs}
    print(sum(points[i] for i in input().upper()))


def m_11_2_4():  # Строка запрос
    def build_query_string(params):
        res = "&".join(
            sorted(f"{parameter}={value}" for parameter, value in params.items())
        )
        return res


def m_11_2_5():  # Слияние словарей
    def merge(values):
        res = {k: set() for d in values for k in d}
        for d in values:
            for k, v in d.items():
                res[k].add(v)
        return res


def m_11_2_6():  # Опасный вирус
    rools = {
        name: set(rool)
        for _ in range(int(input()))
        for name, *rool in [input().split()]
    }
    trslt = {"write": "W", "read": "R", "execute": "X"}
    for _ in range(int(input())):
        act, name = input().split()
        print("OK" if trslt[act] in rools[name] else "Access denied")


def m_11_2_7():  # Покупки в интернет-магазине
    db = {}
    for _ in range(int(input())):
        name, goods, quantity = input().split()
        db.setdefault(name, {})
        db[name][goods] = db[name].get(goods, 0) + int(quantity)

    for name, goods in sorted(db.items()):
        print(name + ":")
        print(*(f"{g} {s}" for (g, s) in sorted(goods.items())), sep="\n")
