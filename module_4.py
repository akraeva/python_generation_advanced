# 4. Вложенные списки
"""
Данный модуль посвящен работе с вложенными списками.
Повторяется тип данных list. Рассматриваются создание, обход,
обработка и вывод вложенных списков, списочные методы, а также
работа с матрицами и операции над ними.
"""

# 4.1 Повторяем списки


# 4.2 Вложенные списки. Часть 1


def m_4_2_1():
    list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
    list1[2][2].append(7000)
    print(list1)


def m_4_2_2():
    list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
    sub_list = ["h", "i", "j"]
    list1[2][1][2].extend(sub_list)
    print(list1)


def m_4_2_3():
    list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
    maximum = max([max(i) for i in list1])

    print(maximum)


def m_4_2_4():
    list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
    [i.reverse() for i in list1]
    print(list1)


def m_4_2_5():
    list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
    total = sum([sum(i) for i in list1])
    counter = sum([len(i) for i in list1])
    print(total / counter)


# 4.3 Вложенные списки. Часть 2


def m_4_3_1():  # Список по образцу 1
    n = int(input())
    res = [[i + 1 for i in range(n)]] * n
    for row in res:
        print(row)


def m_4_3_2():  # Список по образцу 2
    n = int(input())
    res = []
    for i in range(n):
        res.append([j + 1 for j in range(i + 1)])
    for row in res:
        print(row)


def m_4_3_3():  # Треугольник Паскаля 1
    def pascal(num):
        res = [1]
        for i in range(num):
            res = [1] + [res[j] + res[j + 1] for j in range(len(res) - 1)] + [1]
        return res

    n = int(input())
    print(pascal(n))


def m_4_3_4():  # Треугольник Паскаля 2
    def pascal(num):
        res = [[1]]
        for i in range(num - 1):
            row = res[-1]
            res.append([1] + [row[j] + row[j + 1] for j in range(len(row) - 1)] + [1])
        return res

    n = int(input())
    for row in pascal(n):
        print(" ".join([str(i) for i in row]))


def m_4_3_5():  # Упаковка дубликатов
    data = input().split()
    res = [[data[0]]]
    for i in data[1:]:
        if res[-1][-1] == i:
            res[-1].append(i)
        else:
            res.append([i])
    print(res)


def m_4_3_6():  # Разбиение на чанки
    def chunked(data, count):
        res = [data[i : i + count] for i in range(0, len(data), count)]
        return res

    string = input().split()
    num = int(input())
    print(chunked(string, num))


def m_4_3_7():  # Подсписки списка
    data = input().split()
    res = [[]]
    for step in range(1, len(data) + 1):
        res.extend([data[i : i + step] for i in range(len(data) + 1 - step)])
    print(res)


# 4.4 Матрицы. Часть 1


def m_4_4_1():  # Вывести матрицу 1
    n, m = int(input()), int(input())
    mtrx = [[input() for __ in range(m)] for _ in range(n)]
    print("\n".join([" ".join(row) for row in mtrx]))


def m_4_4_2():  # Вывести матрицу 1
    n, m = int(input()), int(input())
    mtrx = [[input() for __ in range(m)] for _ in range(n)]
    print("\n".join([" ".join(row) for row in mtrx]))
    print()
    for i in range(m):
        print(" ".join([mtrx[j][i] for j in range(n)]))


def m_4_4_3():  # След матрицы
    n = int(input())
    mtrx = [input().split() for _ in range(n)]
    print(sum([int(mtrx[i][i]) for i in range(n)]))


def m_4_4_4():  # Больше среднего
    n = int(input())
    mtrx = [[int(x) for x in input().split()] for _ in range(n)]
    print(
        "\n".join(
            [str(len([x for x in row if x > sum(row) / len(row)])) for row in mtrx]
        )
    )


def m_4_4_5():  # Максимальный в области 1
    n = int(input())
    mtrx = [[int(x) for x in input().split()] for _ in range(n)]
    print(max([max([mtrx[i][j] for j in range(i + 1)]) for i in range(n)]))


def m_4_4_6():  # Максимальный в области 2
    n = int(input())
    mtrx = [[int(x) for x in input().split()] for _ in range(n)]
    print(
        max(
            [
                max(
                    [
                        mtrx[i][j]
                        for j in range(n)
                        if (i >= j and i <= n - j - 1) or (i <= j and i >= n - j - 1)
                    ]
                )
                for i in range(n)
            ]
        )
    )


def m_4_4_7():  # Суммы четвертей
    n = int(input())
    mtrx = [[int(x) for x in input().split()] for _ in range(n)]
    res = [
        (
            sum(
                [
                    sum([mtrx[i][j] for j in range(n) if (i < j and i < n - j - 1)])
                    for i in range(n)
                ]
            )
        ),
        (
            sum(
                [
                    sum([mtrx[i][j] for j in range(n) if (i < j and i > n - j - 1)])
                    for i in range(n)
                ]
            )
        ),
        (
            sum(
                [
                    sum([mtrx[i][j] for j in range(n) if (i > j and i > n - j - 1)])
                    for i in range(n)
                ]
            )
        ),
        (
            sum(
                [
                    sum([mtrx[i][j] for j in range(n) if (i > j and i < n - j - 1)])
                    for i in range(n)
                ]
            )
        ),
    ]
    ans = [
        "Верхняя четверть: ",
        "Правая четверть: ",
        "Нижняя четверть: ",
        "Левая четверть: ",
    ]
    print("\n".join([ans[i] + str(res[i]) for i in range(len(ans))]))


# 4.5 Матрицы. Часть 2


def m_4_5_1():  # Таблица умножения
    n, m = int(input()), int(input())
    print(
        "\n".join(
            [("".join([str(i * j).ljust(3) for j in range(m)])) for i in range(n)]
        )
    )


def m_4_5_2():  # Максимум в таблице
    n, m = int(input()), int(input())
    mtrx = [[int(x) for x in input().split()] for _ in range(n)]
    mtrx_max = max([max([mtrx[i][j] for j in range(m)]) for i in range(n)])
    print(
        " ".join(
            [
                [str(i), str(mtrx[i].index(mtrx_max))]
                for i in range(n)
                if mtrx_max in mtrx[i]
            ][0]
        )
    )


def m_4_5_3():  # Обмен столбцов
    n, m = int(input()), int(input())
    mtrx = [input().split() for _ in range(n)]
    i, j = [int(x) for x in input().split()]

    for row in mtrx:
        row[i], row[j] = row[j], row[i]
        print(" ".join(row))


def m_4_5_4():  # Симметричная матрица
    n = int(input())
    mtrx = [[int(x) for x in input().split()] for _ in range(n)]
    print(
        "NO"
        if [0 for j in range(n) for i in range(n) if mtrx[i][j] != mtrx[j][i]]
        else "YES"
    )


def m_4_5_5():  # Обмен диагоналей
    n = int(input())
    mtrx = [input().split() for _ in range(n)]

    for j in range(n):
        mtrx[j][j], mtrx[n - j - 1][j] = mtrx[n - j - 1][j], mtrx[j][j]

    print("\n".join([" ".join(row) for row in mtrx]))


def m_4_5_6():  # Зеркальное отображение
    n = int(input())
    mtrx = [input().split() for _ in range(n)]
    print("\n".join([" ".join(row) for row in mtrx[::-1]]))


def m_4_5_7():  # Поворот матрицы
    n = int(input())
    mtrx = [[int(x) for x in input().split()] for _ in range(n)]

    print(
        "\n".join(
            [
                " ".join([str(mtrx[i][j]) for i in range(n - 1, -1, -1)])
                for j in range(n)
            ]
        )
    )


def m_4_5_8():  # Ходы коня
    field = [["."] * 8 for _ in range(8)]
    j, i = [8 - int(ch) if ch.isdigit() else ord(ch) - ord("a") for ch in input()]
    field[i][j] = "N"
    pos = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]
    for a, b in pos:
        if i + a in range(8) and j + b in range(8):
            field[i + a][j + b] = "*"
    print("\n".join([" ".join(row) for row in field]))


def m_4_5_9():  # Магический квадрат
    def unic(m, len_m):
        res = sorted([m[i][j] for j in range(len_m) for i in range(len_m)])
        return res == [i + 1 for i in range(len_m**2)]

    def same_sum(m, len_m):
        res = sum([m[i][i] for i in range(len_m)])
        if sum([m[n - i - 1][i] for i in range(len_m)]) != res:
            return False
        for row in m:
            if sum(row) != res:
                return False
        for j in range(len_m):
            if sum([m[i][j] for i in range(len_m)]) != res:
                return False
        return True

    n = int(input())
    mtrx = [[int(x) for x in input().split()] for _ in range(n)]

    print("YES" if unic(mtrx, n) and same_sum(mtrx, n) else "NO")


# 4.6 Матрицы. Часть 3


def m_4_6_1():  # Шахматная доска
    n, m = map(int, input().split())
    mtxr = [["." if (i + j) % 2 == 0 else "*" for j in range(m)] for i in range(n)]

    print("\n".join([" ".join(row) for row in mtxr]))


def m_4_6_2():  # Побочная диагональ
    n = int(input())
    mtrx = [[0] * (n - i - 1) + [1] + [2] * (i) for i in range(n)]
    print("\n".join([" ".join(map(str, row)) for row in mtrx]))


def m_4_6_3():  # Заполнение 1
    n, m = map(int, input().split())
    matrix = [[j + 1 + m * i for j in range(m)] for i in range(n)]
    for row in matrix:
        print(" ".join([str(i).ljust(3) for i in row]))


def m_4_6_4():  # Заполнение 2
    n, m = map(int, input().split())
    matrix = [[i + 1 + n * j for j in range(m)] for i in range(n)]
    for row in matrix:
        print(" ".join([str(i).ljust(3) for i in row]))


def m_4_6_5():  # Заполнение 3
    n = int(input())
    matrix = [
        [1 if i == j or (n - i - 1) == j else 0 for j in range(n)] for i in range(n)
    ]
    for row in matrix:
        print(" ".join([str(i).ljust(3) for i in row]))


def m_4_6_6():  # Заполнение 4
    n = int(input())
    matrix = [
        [
            0 if (i > j and i < n - j - 1) or (i < j and i > n - j - 1) else 1
            for j in range(n)
        ]
        for i in range(n)
    ]
    for row in matrix:
        print(" ".join([str(i).ljust(3) for i in row]))


def m_4_6_7():  # Заполнение 5
    n, m = map(int, input().split())
    row = [j + 1 for j in range(m)]
    matrix = [row[i % m :] + row[: i % m] for i in range(n)]
    for row in matrix:
        print(" ".join([str(i).ljust(3) for i in row]))


def m_4_6_8():  # Заполнение змейкой
    n, m = map(int, input().split())
    matrix = [
        [j + 1 + m * i for j in range(m)][:: 1 if i % 2 == 0 else -1] for i in range(n)
    ]
    for row in matrix:
        print(" ".join([str(i).ljust(3) for i in row]))


def m_4_6_9():  # Заполнение диагоналями
    n, m = map(int, input().split())
    matrix = [[0] * m for i in range(n)]
    counter = 1
    for k in range(n + m - 1):
        for i in range(n):
            if k - i in range(0, m):
                matrix[i][k - i] = counter
                counter += 1

    for row in matrix:
        print(" ".join(str(i).ljust(3) for i in row))


def m_4_6_10():  # Заполнение спиралью
    n, m = map(int, input().split())

    border = 0
    location = []
    while border < m - border and border < n - border:
        location.extend((border, x) for x in range(border, m - border))
        location.extend((x, m - border - 1) for x in range(border + 1, n - border))
        if len(location) < n * m:
            location.extend(
                (n - border - 1, x) for x in range(m - border - 2, border - 1, -1)
            )
            location.extend((x, border) for x in range(n - border - 2, border, -1))
        border += 1

    matrix = [[0] * m for _ in range(n)]
    counter = 1
    for i, j in location:
        matrix[i][j] = counter
        counter += 1

    for row in matrix:
        print(" ".join(str(i).ljust(3) for i in row))


# 4.7 Операции над матрицами в математике


def m_4_7_1():  # Сложение матриц
    def read_matrix(len_matrix):
        return [list(map(int, input().split())) for _ in range(n)]

    n, m = map(int, input().split())
    A = read_matrix(n)
    input()
    B = read_matrix(n)

    res = [[a + b for a, b in zip(a_row, b_row)] for a_row, b_row in zip(A, B)]

    for row in res:
        print(*row)


def m_4_7_2():  # Умножение матриц
    def read_matrix():
        n, m = map(int, input().split())
        matrix = [list(map(int, input().split())) for _ in range(n)]
        return matrix

    A = read_matrix()
    input()
    B = read_matrix()

    AB = [
        [sum([a * b for a, b in zip(a_row, b_col)]) for b_col in zip(*B)] for a_row in A
    ]

    for row in AB:
        print(*row)


def m_4_7_3():  # Возведение матрицы в степень
    def matrix_mult(A, B):
        return [
            [sum(a * b for a, b in zip(a_row, b_col)) for b_col in zip(*B)]
            for a_row in A
        ]

    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    m = int(input())
    res = matrix
    for i in range(m - 1):
        res = matrix_mult(res, matrix)

    for row in res:
        print(*row)
