# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

#Решение
def function():
    try:
        with open('textfile_for_task5.txt', 'w+') as file:
            line = input('Введите цифры через пробелов: \n')
            file.writelines(line)
            my_numb = line.split()
            print(f'Сумма чисел в файле равняется: {sum(map(int, my_numb))}')
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
function()