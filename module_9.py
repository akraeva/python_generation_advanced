# 9. Итоговая работа на множества
"""
Этот модуль содержит дополнительные задачи по изученным темам.
Они помогут еще раз закрепить ваши знания, углубить понимание
rлючевых концепций и убедиться, что вы освоили материал.
"""


# 9.1 Часть 1
def m_9_1_1():
    set1 = {"a", "t", "f", "p"}
    set2 = {"a", "t", "f"}
    print(set1 - set2)


# 9.2 Часть 2


def m_9_2_1():  # Домашнее задание
    n, m, k, p = (int(input()) for _ in range(4))
    print(n - (m + k - p))


def m_9_2_2():  # Восход
    nums = input().split()
    print(len(nums) - len(set(nums)))


def m_9_2_3():  # Города
    cities = set(input() for i in range(int(input())))
    print("REPEAT" if input() in cities else "OK")


def m_9_2_4():  # Книги на прочтение
    m, n = int(input()), int(input())
    lib = set(input() for _ in range(m))
    book_list = [input() for _ in range(n)]
    for book in book_list:
        print("YES" if book in lib else "NO")


def m_9_2_5():  # Странное увлечение
    list1, list2 = (set(int(x) for x in input().split()) for _ in range(2))
    print(*sorted(list1 & list2, reverse=True)) if list1 & list2 else print("BAD DAY")


def m_9_2_6():  # Онлайн-школа BEEGEEK 1
    nums = set(input().split())
    res = set(input().split())
    print(("NO", "YES")[nums == res])


def m_9_2_7():  # Онлайн-школа BEEGEEK 2
    m, n = int(input()), int(input())
    math = set(input() for _ in range(m))
    inf = set(input() for _ in range(n))

    print(len(math - inf))


def m_9_2_8():  # Онлайн-школа BEEGEEK 3
    m, n = int(input()), int(input())
    math = set(input() for _ in range(m))
    inf = set(input() for _ in range(n))
    res = len(math ^ inf)
    print(res if res else "NO")


def m_9_2_9():  # Онлайн-школа BEEGEEK 4
    print(*sorted(set(input().split()) | set(input().split())))


def m_9_2_10():  # Онлайн-школа BEEGEEK 5
    m, n = int(input()), int(input())
    names = set(input() for _ in range(n + m))
    res = len(names) * 2 - (n + m)
    print(res if res else "NO")


def m_9_2_11():  # Онлайн-школа BEEGEEK 6
    data = [set(input() for __ in range(int(input()))) for _ in range(int(input()))]
    res = data[0]
    for i in data[1:]:
        res &= i
    print(*sorted(res), sep="\n")
