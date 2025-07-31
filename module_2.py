# 2. Повторяем основные конструкции языка Python
"""
Этот модуль содержит задачи для повторения тем,
изученных в предыдущем курсе.
"""

# 2.1 Часть 1


def m_2_1_1():
    a, b = int(input()), int(input())
    print(a + b, a - b, a * b, a / b, a // b, a % b, (a**10 + b**10) ** 0.5, sep="\n")


def m_2_1_2():
    m, h = float(input()), float(input())
    imt = m / h**2
    if imt > 25:
        print("Избыточная масса")
    elif imt < 18.5:
        print("Недостаточная масса")
    else:
        print("Оптимальная масса")


def m_2_1_3():
    s = len(input()) * 0.6
    print(f"{int(s)} р. {round(s%1*100)} коп.")


def m_2_1_4():
    print(len(input().split()))


def m_2_1_5():
    cal = [
        "Дракон",
        "Змея",
        "Лошадь",
        "Овца",
        "Обезьяна",
        "Петух",
        "Собака",
        "Свинья",
        "Крыса",
        "Бык",
        "Тигр",
        "Заяц",
    ]
    print(cal[(int(input()) - 8) % 12])


def m_2_1_6():
    s = input()
    print(int((s[0] if len(s) > 5 else "") + s[-1:-6:-1]))


def m_2_1_7():
    n = input()
    n = ["", "  ", " "][len(n) % 3] + n
    print(",".join([n[x : x + 3] for x in range(0, len(n), 3)]).strip())


def m_2_1_8():
    n, k = int(input()), int(input())
    nums = [i + 1 for i in range(n)]

    num = 0
    while len(nums) != 1:
        num = (num + k - 1) % len(nums)
        nums.pop(num)

    print(nums[0])


# 2.2 Часть 2


def m_2_2_1():
    res = [0, 0, 0, 0, 0]
    for _ in range(int(input())):
        x, y = [int(i) for i in input().split()]
        n = 0
        if x > 0 and y > 0:
            n = 1
        elif x < 0 and y > 0:
            n = 2
        elif x < 0 and y < 0:
            n = 3
        elif x > 0 and y < 0:
            n = 4
        res[n] += 1

    print(f"Первая четверть: {res[1]}")
    print(f"Вторая четверть: {res[2]}")
    print(f"Третья четверть: {res[3]}")
    print(f"Четвертая четверть: {res[4]}")


def m_2_2_2():
    nums = [int(i) for i in input().split()]
    res = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            res += 1
    print(res)


def m_2_2_3():
    nums = [i for i in input().split()]
    for i in range(1, len(nums), 2):
        nums[i], nums[i - 1] = nums[i - 1], nums[i]
    print(" ".join(nums))


def m_2_2_4():
    nums = [i for i in input().split()]
    nums.insert(0, nums.pop(-1))
    print(" ".join(nums))


def m_2_2_5():
    print(len(set([i for i in input().split()])))


def m_2_2_6():
    nums = [int(input()) for _ in range(int(input()))]
    n, res = int(input()), "НЕТ"
    for i in range(len(nums) - 1):
        if nums[i] != 0 and n % nums[i] != 0:
            continue
        for j in range(i + 1, len(nums)):
            if nums[j] * nums[i] == n:
                res = "ДА"
                break
    print(res)


def m_2_2_7():
    res = {
        ("камень", "ножницы"): "Тимур",
        ("ножницы", "бумага"): "Тимур",
        ("бумага", "камень"): "Тимур",
        ("ножницы", "камень"): "Руслан",
        ("бумага", "ножницы"): "Руслан",
        ("камень", "бумага"): "Руслан",
    }
    t, r = input(), input()
    print("ничья" if t == r else res.get((t, r)))


def m_2_2_8():
    res = {
        "камень": ("ножницы", "ящерица"),
        "ножницы": ("ящерица", "бумага"),
        "бумага": ("камень", "Спок"),
        "ящерица": ("Спок", "бумага"),
        "Спок": ("ножницы", "камень"),
    }
    t, r = input(), input()
    print("ничья" if t == r else "Тимур" if r in res.get(t) else "Руслан")


def m_2_2_9():
    print(len(max(input().split("О"))))


def m_2_2_10():
    name = "anton"
    for i in range(int(input())):
        data = input()
        index = 0
        for ch in data:
            if ch == name[index]:
                index += 1
            if index == len(name):
                print(i + 1, end=" ")
                break


def m_2_2_11():
    word = input() + " запретил букву"
    chars = ("".join(sorted(list((set(word)))))).strip()
    for i in chars:
        print(word, i)
        word = " ".join(("".join([ch for ch in word if ch != i])).strip().split())
