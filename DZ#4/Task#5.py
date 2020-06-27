# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

#Решение

from functools import reduce


def my_func(prev_el, el):
    return prev_el * el
# prev_el - предыдущий элемент
# el - текущий элемент

print(f'Список четных значений: {[el for el in range(1, 11) if el % 2 == 0]}')
print(f'Результат вычисления произведения элементов списка: {reduce(my_func, [el for el in range(1, 11) if el % 2 == 0])}')