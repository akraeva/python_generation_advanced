# 17. Работа с файлами
"""
Модуль посвящен работе с файлами в Python. Рассматриваются файловый
ввод и вывод, чтение и запись текстовых файлов, построчная обработка
данных и использование менеджера контекста для безопасной работы с файлами.
"""
import random
from functools import reduce

# 17.1 Файловый ввод и вывод


# 17.2 Работа с текстовыми файлами. Часть 1


def m_17_2_1():  # Содержимое файла
    file_name = input()  # "data/test_file.txt" <= для тестов

    file = open(file_name, encoding="utf-8")
    for file_content in file:
        print(file_content.rstrip())

    file.close()


def m_17_2_2():  # Предпоследняя строка
    file_name = input()  # "data/test_file.txt" <= для тестов

    file = open(file_name, encoding="utf-8")
    last_line = file.readlines()[-2]
    print(last_line.rstrip())

    file.close()


def m_17_2_3():  # Случайная строка
    # import random

    file_name = "lines.txt"  # "data/lines.txt" <= для тестов

    file = open(file_name, encoding="utf-8")
    random_line = file.readlines()
    print(random_line[random.randint(0, len(random_line))].rstrip())
    # правильнее использовать random.choice

    file.close()


def m_17_2_4():  # Сумма двух-1
    file_name = "numbers.txt"  # "data/numbers.txt" <= для тестов

    file = open(file_name, encoding="utf-8")
    print(sum(map(int, file.readlines())))

    file.close()


def m_17_2_5():  # Сумма двух-2
    file_name = "nums.txt"  # "data/nums.txt" <= для тестов
    file = open(file_name, encoding="utf-8")
    print(sum(map(int, file.read().split())))
    file.close()


def m_17_2_6():  # Общая стоимость
    # вариант без импорт reduce
    file_name = "data/prices.txt"  # "data/prices.txt" <= для тестов
    file = open(file_name, encoding="utf-8")
    sum = 0
    for row in file:
        _, count, price = row.split("\t")
        sum += int(count) * int(price)
    print(sum)
    file.close()

    # from functools import reduce

    file_name = "data/prices.txt"  # "data/prices.txt" <= для тестов
    file = open(file_name, encoding="utf-8")

    print(
        reduce(
            lambda acc, line: acc
            + int(line.split("\t")[1]) * int(line.split("\t")[-1]),
            file,
            0,
        )
    )
    file.close()


# 17.3 Работа с текстовыми файлами. Часть 2


def m_17_3_1():  # Переворот строки
    file_name = "text.txt"  # "data/text.txt" <= для тестов
    with open(file_name, encoding="utf-8") as file:
        print(file.readline()[::-1])


def m_17_3_2():  # Обратный порядок
    file_name = "data.txt"  # "data/data.txt" <= для тестов
    with open(file_name, encoding="utf-8") as file:
        print(*(line.strip() for line in file.readlines()[::-1]), sep="\n")


def m_17_3_3():  # Длинные строки
    file_name = "lines.txt"  # "data/lines-2.txt" <= для тестов
    with open(file_name, encoding="utf-8") as file:
        lines = list(map(str.strip, file.readlines()))
        max_len = max(len(line) for line in lines)
        max_lines = filter(lambda line: len(line) == max_len, lines)
    print(*max_lines, sep="\n")


def m_17_3_4():  # Сумма чисел в строках
    file_name = "numbers-2.txt"  # "data/numbers-2.txt" <= для тестов
    with open(file_name, encoding="utf-8") as file:
        lines = (
            (int(num) for num in line.strip().split()) for line in file.readlines()
        )
        lines_sum = (sum(line) for line in lines)
    print(*lines_sum, sep="\n")


def m_17_3_5():  # С умма чисел в файле
    file_name = "nums-2.txt"  # "data/nums-2.txt" <= для тестов
    with open(file_name, encoding="utf-8") as file:
        nums = "".join(
            ch if ord(ch) in range(ord("0"), ord("9") + 1) else " "
            for ch in file.read()
        ).split()
    print(sum(map(int, nums)))


def m_17_3_6():  # Статистика по файлу
    file_name = "file.txt"  # "data/file.txt" <= для тестов
    with open(file_name, encoding="utf-8") as file:
        lines = [line.strip() for line in file.readlines()]
        words = sum(len(line.split()) for line in lines)
        letters = len(
            list(
                filter(
                    lambda x: x.isalpha(),
                    [ch for line in lines for word in line.split() for ch in word],
                )
            )
        )
    print(f"Input file contains:\n{letters} letters\n{words} words\n{len(lines)} lines")


def m_17_3_7():  # Random name and surname
    # import random
    file_1 = "first_names.txt"  # "data/first_names.txt" <= для тестов
    file_2 = "last_names.txt"  # "data/last_names.txt" <= для тестов
    with open(file_1, encoding="utf-8") as first_file, open(
        file_2, encoding="utf-8"
    ) as last_file:
        first_names = [line.strip() for line in first_file.readlines()]
        last_names = [line.strip() for line in last_file.readlines()]
        for _ in range(3):
            print(random.choice(first_names), random.choice(last_names))


def m_17_3_8():  # Необычные страны
    file_name = "population.txt"  # "data/population.txt" <= для тестов
    with open(file_name, encoding="utf-8") as file:
        lines = [line.strip().split("\t") for line in file.readlines()]
        print(
            *map(
                lambda line: line[0],
                filter(
                    lambda line: line[0][0] == "G" and int(line[-1]) > 500000, lines
                ),
            ),
            sep="\n",
        )


def m_17_3_9():  # CSV-файл
    def read_csv():
        file_name = "data.csv"  # "data/pdata.csv" <= для тестов
        data_dict = []
        with open(file_name, encoding="utf-8") as file:
            keys = file.readline().strip().split(",")
            values = [line.strip().split(",") for line in file.readlines()]
            for row in values:
                data_dict.append(dict(zip(keys, row)))
        return data_dict


# 17.4 Работа с текстовыми файлами. Часть 3


def m_17_4_1():  # Входная строка
    s = input()
    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(s)


def m_17_4_2():  # Случайные числа
    # import random
    with open("random.txt", "w", encoding="utf-8") as file:
        print(*(random.randint(111, 777 + 1) for _ in range(25)), sep="\n", file=file)


def m_17_4_3():  # Нумерация строк
    file_name = "input.txt"  # "data/input.txt" <= для тестов
    with open(file_name, encoding="utf-8") as input_file, open(
        "output.txt", "w", encoding="utf-8"
    ) as output_file:
        lines = input_file.readlines()
        output_file.writelines([f"{lines.index(line) + 1}) {line}" for line in lines])


def m_17_4_4():  # Подарок на новый год
    file_name = "data/class_scores.txt"  # "data/class_scores.txt" <= для тестов
    with open(file_name, encoding="utf-8") as file:
        scores = [row.strip().split() for row in file.readlines()]
    result = [
        f"{row[0]} {int(row[-1]) + 5 if int(row[-1]) + 5 <= 100 else 100}"
        for row in scores
    ]
    with open("new_scores.txt", "w", encoding="utf-8") as file:
        print(*result, sep="\n", file=file)


def m_17_4_5():  # Загадка от Жака Фреско
    goat_dict = {}
    file_name = "data/goats.txt"  # "data/goats.txt" <= для тестов
    with open(file_name, encoding="utf-8") as file:
        line = file.readline()
        while (line := file.readline().strip()) != "GOATS":
            goat_dict[line] = 0

        for line in file:
            goat_dict[line.strip()] += 1

    goat_count = sum(goat_dict.values())
    result = [color for color, count in goat_dict.items() if count / goat_count > 0.07]

    with open("answer.txt", "w", encoding="utf-8") as file:
        print(*sorted(result), sep="\n", file=file)


def m_17_4_6():  # Конкатенация файлов
    file_names = [input() for _ in range(int(input()))]
    with open("output.txt", "w", encoding="utf-8") as output_file:
        for file_name in file_names:
            with open(file_name, encoding="utf-8") as file:
                output_file.writelines(file.readlines())


def m_17_4_7():  # Лог файл
    def time_calc(*times):
        t1, t2 = (time.split(":") for time in times)
        to_min = lambda h, m: int(h) * 60 + int(m)
        return to_min(*t2) - to_min(*t1)

    file_name = "logfile.txt"  # "data/logfile.txt" <= для тестов
    with open(file_name, encoding="utf-8") as log_file, open(
        "output.txt", "w", encoding="utf-8"
    ) as output:
        for user in log_file:
            name, *time = user.strip().split(", ")
            if time_calc(*time) >= 60:
                output.write(name + "\n")
