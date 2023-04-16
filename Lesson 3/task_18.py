"""
Задача 18: Требуется найти в массиве A[N] самый близкий по величине элемент к
заданному числу X. Пользователь в первой строке вводит натуральное число N –
количество элементов в массиве. В последующих  строках записаны N целых чисел
Ai. Последняя строка содержит число X
Ввод: 5
Ввод: 1 2 6 4 9
Ввод: 8
-> 9
"""

if __name__ == '__main__':
    arr_len = int(input('Введите длину массива: '))
    arr = []
    for i in range(arr_len):
        arr.append(int(input(f'введите {i+1}-е число массива: ')))
    x = int(input('Введите число, число X: '))
    neighbour = abs(abs(x) - abs(arr[0]))
    index = 0
    for i in range(1, arr_len):
        new_neighbour = abs(abs(x) - abs(arr[i]))
        if new_neighbour < neighbour:
            index = i
            neighbour = new_neighbour
    print(f'Ближайшее число: {arr[index]}')
