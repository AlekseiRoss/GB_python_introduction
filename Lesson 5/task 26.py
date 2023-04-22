"""
Задача 26:  Посчитать факториал (произведение 1 до N) и треугольное число
(сумма чисел от 1 до N) для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов
"""


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def triangular_number(n):
    if n == 1:
        return 1
    else:
        return n + triangular_number(n-1)


if __name__ == "__main__":
    # 6
    print(factorial(3))
    # 10
    print(triangular_number(4))
