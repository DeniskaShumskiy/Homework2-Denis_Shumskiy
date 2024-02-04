print("Длины сторон треугольника")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
flag = ""
if a + b > c:
    if a + c > b:
        if b + c > a:
            print("Треугольник есть") # Если две стороны больше либо равно третье,
            # то треугольник есть
        else:
            flag = "a"
    else:
        flag = "b"
else:
    flag = "c"
if flag != "":
    print("Треугольника нет")



























