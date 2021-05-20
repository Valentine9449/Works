#1 Список зарезервированых слов.
import keyword
print(keyword.kwlist)
#2 Список Дзен-Пайтон
import this
print(this)
#3Создать python-модуль для реализации ввода через клавиатуру целочисленных значений.
# Добавить функционал конвертации во float и str.
num = int(input("Введите число: "))
print(num)
print(float(num),type(float(num)))
print(str(num),type(str(num)))
#4Создать python-модуль для реализации ввода через клавиатуру дробных значений.
# Добавить функционал конвертации в int и str.
num_two = float(input("Введите число: "))
print(num_two,type(num_two))
print(int(num_two),type(int(num_two)))
print(str(num_two),type(str(num_two)))