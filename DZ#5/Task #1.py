# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

#Решение
my_file = open('textfile_for_task1.txt', 'w')

line = input('Введите текст: \n')
while line:
    my_file.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

my_file.close()
my_file = open('textfile_for_task1.txt', 'r')
content = my_file.readlines()
print(content)
my_file.close()