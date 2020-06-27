# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

#employee_name - имя сотрудника; production_in_hours - выработка в часах; rate_per_hour - ставка в час; bonus - премия

# Решение

from sys import argv

name, production_in_hours, rate_per_hour, bonus = argv

try:
    print("Имя сотрудника: ", name)
    print("Выработка сотрудника в часах:", production_in_hours)
    print("Ставка сотрудника в час(руб.):", rate_per_hour)
    print("Премия сотрудника(руб.):", bonus)
    production_in_hours = int(production_in_hours)
    rate_per_hour = int(rate_per_hour)
    bonus = int(bonus)
    res = production_in_hours * rate_per_hour + bonus
    print(f'заработная плата сотрудника - {name} составляет:{res}')
except ValueError:
    print('Not a number')