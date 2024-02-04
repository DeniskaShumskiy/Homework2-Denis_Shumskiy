print("Привет, это игра в числа")
my_name = input("Как вас зовут? ")
print("Добрый день " + my_name)
number = float(input("Введите число ")) # Присваиваем переменной int и выводим input для ввода числа
if (number % 2) == 0: # Высчитываем остаток от деления числа, который должен равняться 0
    if type(number) == float:
        print(number)
        print("Вы ввели чётное число")
else:
    print(number)
    print("Вы ввели нечётное число")

