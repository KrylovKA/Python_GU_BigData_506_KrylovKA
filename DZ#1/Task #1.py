# print(f"{7/99:.4f}")
#Create chat bot
name = input('Привет, меня зовут робот Иван!. Введи пож-та свое имя:')
print(f"Привет {name}!. Очень притно познакомится")
age = input('А сколько вам лет?:')
permissible_age = "18"
if age <= permissible_age:
    print("Вход запрещен!")
else:
    print("Введен корректный возраст пользователя")
