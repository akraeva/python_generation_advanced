# 3. Тип данных bool и NoneType
"""
Этот модуль посвящен логическому типу bool и типу NoneType.
Рассматриваются логические операторы, функции bool(), type(), isinstance(),
особенности значения None и его поведение в различных выражениях.
"""

# 3.1 Тип данных bool


def m_3_1_1():
    # объявление функции
    def func(num1, num2):
        return num1 % num2 == 0

    # считываем данные
    num1, num2 = int(input()), int(input())

    # вызываем функцию
    if func(num1, num2):
        print("делится")
    else:
        print("не делится")


# 3.2 Тип данных NoneType
