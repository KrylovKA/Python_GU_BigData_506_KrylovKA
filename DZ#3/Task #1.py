# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

# Решение:
def task_1():
    try:
        return num_1 / num_2
    except ZeroDivisionError:
        return 'Ошибка! Нельзя делить на 0'
    except ValueError:
        return 'No value'
num_1 = int(input('Пожалуйста, введите первое число:'))
num_2 = int(input('Пожалуйста, введите второе число:'))
# if num_1 or num_2 == type(int):
#     print("Введено корректное число")
# else:
#     print("Разрешен ввод только целых чисел!")
division_numbers = num_1/num_2
division_numbers = task_1()
print(f"Результат деления - {division_numbers}")