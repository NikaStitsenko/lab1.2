'''Дважды ввести пароль
программа, которая сравнивает пароль и его
подтверждение.
* совпадают: «Пароль принят»
* иначе: «Пароль не принят»'''

a = input()
b = input()
if a == b:
    print("Пароль принят")
else:
    print("Пароль не принят")