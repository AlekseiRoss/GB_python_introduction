"""
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не
превосходящие числа N.
"""


def natural_pow_of_2(n):
    arr = []
    for i in range(-n, n+1):
        arr.append(2**i)
    return arr


if __name__ == '__main__':
    print(natural_pow_of_2(5))
