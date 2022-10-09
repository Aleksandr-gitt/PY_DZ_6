# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.
# in  9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]
import random


def nums(num):
    return random.choices(range(num*2), k=num)

def result(ls):
    i = 1
    res = [ls[i] for i in range(i, len(ls)) if ls[i] > ls[i-1]]
    return res

num = int(input('Введите длину списка: '))
ls_nums = nums(num)
print(ls_nums)
print(result(ls_nums))
