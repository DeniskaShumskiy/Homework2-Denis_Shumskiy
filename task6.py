n = int(input("Введите число "))
temp = n # Создаём ещё одну переменную
rev = 0
while (n > 0): # Переворачиваем исходное число
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
    if(temp == rev):
        print("Это палиндром")
else:
        print("Это не палиндром")






















