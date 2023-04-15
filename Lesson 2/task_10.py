from random import randint

"""
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые –
гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы
все монетки были повернуты вверх одной и той же стороной.
"""


def solution(coins_arr):
    counter = 0
    for i in range(len(coins_arr)):
        if coins_arr[i] == 1:
            counter += 1
    if counter > len(coins_arr) / 2:
        counter = len(coins_arr) - counter
    return counter


if __name__ == "__main__":
    # количество монет
    n = 5
    coins = [randint(0, 1) for i in range(n)]
    print(coins)
    print(f'Минимальное число монеток, которые нужно перевернуть, чтобы все '
          f'монетки были повернуты вверх одной и той же стороной: '
          f'{solution(coins)}')
