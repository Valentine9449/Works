import math
from math import sqrt



#1

a = 2
b = 2
if a %2 !=0 and b %2 !=0:
    print("Оба числа нечетные")
elif a %2 !=0:
    print("Число:", a, "нечетное")
elif b %2 !=0:
    print("Число:", b, "нечетное")
else:
    print("Все числа четные")

#*********************************#

#2

first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))
if first > second and first < third:
    print("Среднее число - ", first)
if second > first and second < third:
    print("Среднее число - ", second)
if third > first and third < second:
    print("Среднее число - ", third)


#*********************************#

#3
 
x = float(input("Введите x: "))
y = float(input("Введите y: "))
r = float(input("Введите радиус: "))
h = sqrt(x**2 + y**2)
print("Расстояние до точки от начала координат равно %.2f" % h)
if h > r:
    print("Точка находится за пределами круга")
else:
    print("Точка принадлежит кругу")



#*********************************#

#4
x = int(input("Введите x:"))
def f(x):
    if x > 0:
        return  2 * x - 10
    elif x == 0:
        return 0
    elif x < 0:
        return 2 * abs(x) - 1
f(x)
    
#*********************************#

#5
"""a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
print("Наибольшее число - ", max(a, b, c))
"""

#*********************************#

#6

a = int(input("Введите сторону А: "))
b = int(input("Введите сторону B: "))
c = int(input("Введите сторону C: "))
 
if a + b <= c or a + c <= b or b + c <= a:
    print("Треугольник не существует")
elif a != b and a != c and b != c:
    print("Треугольник разносторонний")
elif a == b == c:
    print("Треугольник равносторонний")
else:
    print("Треугольник равнобедренный")

#*********************************#

#7
x = int(input("Введите x: "))
y = int(input("Введите y: "))
if x > 0 and y > 0:
    print('Первая')
elif x < 0 and y > 0:
    print('Вторая')
elif x < 0 and y < 0:
    print('Третья')
elif x > 0 and y < 0:
    print('Четвёртая')

#*********************************#

#8

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a/b:
    print("Первое число делится на второе, результат: ", a/b)
else:
    print("Первое число не делится на второе")

#*********************************#

#9


a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
formula = b**2 - 4 * a * c
print("D = ", formula)
if formula > 0:
    x1 = (-b + math.sqrt(formula)) / (2 * a)
    x2 = (-b - math.sqrt(formula)) / (2 * a)
    print("x1 = ",x1, "\nx2 = ",x2)
elif formula == 0:
    x = -b / (2 * a)
    print("x = ", x)
else:
    print("Корней нет")
