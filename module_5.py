# 5. Итоговая работа на вложенные списки и матрицы
"""
Этот модуль содержит дополнительные задачи по изученным темам.
Они помогут еще раз закрепить ваши знания, углубить понимание
ключевых концепций и убедиться, что вы освоили материал.
"""

# 5.1 Подзаголовок


def m_5_1_1():  # Каждый n-ый элемент
    s = input().split()
    n = int(input())
    res = [[s[j] for j in range(i, len(s), n)] for i in range(n)]
    print(res)


def m_5_1_2():  # Максимальный в области 2
    n = int(input())
    matrix = [[int(x) for x in input().split()] for _ in range(n)]
    res = max(matrix[i][j] for j in range(n) for i in range(n) if i >= n - j - 1)
    print(res)


def m_5_1_3():  # Транспонирование матрицы
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    res = list(zip(*matrix))
    for row in res:
        print(*row)


def m_5_1_4():  # Снежинка
    n = int(input())
    matrix = [["."] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == (n - 1) / 2 or j == (n - 1) / 2 or i == j or (n - i - 1) == j:
                matrix[i][j] = "*"

    for row in matrix:
        print(*row)


def m_5_1_5():  # Симметричная матрица
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    res = [
        0
        for i in range(n)
        for j in range(n - i - 1)
        if matrix[i][j] != matrix[n - j - 1][n - i - 1]
    ]

    print("NO" if res else "YES")


def m_5_1_6():  # Латинский квадрат
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    ref = [i + 1 for i in range(n)]
    matrix += list(zip(*matrix))
    res = [0 for row in matrix if sorted(row) != ref]

    print("NO" if res else "YES")


def m_5_1_7():  # Ходы ферзя
    x, y = [8 - int(ch) if ch.isdigit() else ord(ch) - ord("a") for ch in input()]

    field = [
        ["*" if i == y or j == x or abs(x - j) == abs(y - i) else "." for j in range(8)]
        for i in range(8)
    ]
    field[y][x] = "Q"

    for row in field:
        print(*row)


def m_5_1_8():  # Диагонали, параллельные главной
    n = int(input())
    matrix = [[abs(i - j) for j in range(n)] for i in range(n)]

    for row in matrix:
        print(*row)
