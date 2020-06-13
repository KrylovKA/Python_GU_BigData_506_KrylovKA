number_n  = int(input('Введи число n:'))
number = str(number_n)
double_n = number + number
triple_n = number + number + number
sum = number_n + int(double_n) + int(triple_n)
print(f"Значение числа n: {sum}")