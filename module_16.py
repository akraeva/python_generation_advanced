# 16. Итоговая работа на функции
"""
Этот модуль содержит дополнительные задачи по изученным темам.
Они помогут еще раз закрепить ваши знания, углубить понимание
ключевых концепций и убедиться, что вы освоили материал.
"""
from functools import reduce

# 16.1 Часть 1


def m_16_1_1():  # Письмо для экзамена
    def generate_letter(mail, name, date, time, place, teacher="Тимур Гуев", number=17):
        letter = f"To: {mail}\nПриветствую, {name}!\nВам назначен экзамен, который пройдет {date}, в {time}.\nПо адресу: {place}.\nЭкзамен будет проводить {teacher} в кабинете {number}.\nЖелаем удачи на экзамене!"
        return letter


def m_16_1_2():  # Pretty print
    def pretty_print(data, side="-", delimiter="|"):
        row = delimiter + delimiter.join(f" {d} " for d in data) + delimiter
        header = f" {side*(len(row)-2)} "
        print(header, row, header, sep="\n")


# 16.2 Часть 2


# 16.3 Часть 3


def m_16_3_1():
    def concat(*args, sep=" "):
        return sep.join(f"{i}" for i in args)


def m_16_3_2():
    # from functools import reduce

    def product_of_odds(data):
        return reduce(lambda i, acc: acc * i, filter(lambda i: i % 2 == 1, data), 1)


def m_16_3_3():
    words = "the world is mine take a look what you have started".split()
    print(*map(lambda x: f'"{x}"', words), sep=" ")


def m_16_3_4():
    numbers = [
        18,
        191,
        9009,
        5665,
        78,
        77,
        45,
        23,
        19991,
        908,
        8976,
        6565,
        5665,
        10,
        1000,
        908,
        909,
        232,
        45654,
        786,
    ]
    print(*filter(lambda x: str(x) != str(x)[::-1], numbers), sep=" ")


def m_16_3_5():
    numbers = [
        (10, -2, 3, 4),
        (-13, 56),
        (1, 9, 2),
        (-1, -9, -45, 32),
        (-1, 5, 1),
        (17, 0, 1),
        (0, 1),
        (3,),
        (39, 12),
        (11, -23),
        (10, -100, 21, 32),
        (3, -8),
        (1, 1),
    ]
    sorted_numbers = sorted(numbers, key=(lambda x: sum(x) / len(x)), reverse=True)
    print(sorted_numbers)


def m_16_3_6():
    def call(func, *args):
        return func(*args)


def m_16_3_7():
    def compose(f, g):
        return lambda x: f(g(x))


def m_16_3_8():
    def arithmetic_operation(operation):
        match operation:
            case "+":
                return lambda a, b: a + b
            case "-":
                return lambda a, b: a - b
            case "*":
                return lambda a, b: a * b
            case "/":
                return lambda a, b: a / b


def m_16_3_9():  # В одну строку
    print(*sorted(input().split(), key=lambda x: x.lower()), sep=" ")


def m_16_3_10():  # Гематрия слова
    print(
        *sorted(
            (input() for _ in range(int(input()))),
            key=lambda word: (sum(ord(ch.upper()) - ord("A") for ch in word), word),
        ),
        sep="\n",
    )


def m_16_3_11():  # Сортировка IP-адресов
    print(
        *(
            ".".join(addr)
            for addr in sorted(
                (input().split(".") for _ in range(int(input()))),
                key=lambda address: sum(
                    int(part) * 256 ** (3 - i) for i, part in enumerate(address)
                ),
            )
        ),
        sep="\n",
    )
