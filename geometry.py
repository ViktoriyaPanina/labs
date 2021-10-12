def is_int(_str):
    try:
        int(_str)
        return True
    except ValueError:
        return False


def check_side():
    flag = False
    while flag == False:
        _side = (input("Введите сторону треугольника: "))
        flag = is_int(_side)
        if flag and (int(_side) <= 0):
            flag = False
        if not flag:
            print("Некорректный ввод, введите целое число")
            _side = (input("Введите сторону треугольника: "))
            flag = is_int(_side)
    return int(_side)


sides = []
a = check_side()
sides.append(a)
b = check_side()
sides.append(b)
c = check_side()
sides.append(c)
print("a = ", a)
print("b = ", b)
print("c = ", c)


if (a + b <= c) or (a + c <= b) or (b + c <= a):
    print("Треугольник  со сторонами ", a, b, c, " не существует")
else:
    if a == b == c:
        print("Треуголник со сторонами ", a, b, c, "равносторонний")
    elif (a == b) or (b == c) or (a == c):
        print("Треуголник со сторонами ", a, b, c, "равнобедренный")
    else:
        print("Треуголник со сторонами ", a, b, c, "разносторонний")
    sides.sort()
    if sides[2]**2 == sides[0]**2 + sides[1]**2:
        print("Треугольник со сторонами ", a, b, c, " прямоугольный")
    if sides[2] ** 2 <= sides[0] ** 2 + sides[1] ** 2:
        print("Треугольник со сторонами ", a, b, c, " остроугольный")
    if sides[2] ** 2 >= sides[0] ** 2 + sides[1] ** 2:
        print("Треугольник со сторонами ", a, b, c, " тупоугольный")
