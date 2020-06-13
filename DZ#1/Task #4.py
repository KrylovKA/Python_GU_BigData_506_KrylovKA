number  = int(input('Введи целое положительное число:'))
number_1 = number % 10
number = number // 10
while number > 0:
    if number % 10 > number_1:
        number_1 = number % 10
    number = number // 10
print(f"Самая большая цифра в числе:{number_1}")