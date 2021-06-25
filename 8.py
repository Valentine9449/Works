import random


# Заполнить список ста нулями,
# кроме первого и последнего элементов, которые должны быть равны единице;



a = [(0 for items in range(0, 100))]
a[0] = 1
a[-1] = 1
print(a)


# Сформировать возрастающий список из чётных чисел (количество элементов 45);


list_two = []
for numbers in range(0, 91, 2):
    list_two = numbers
    print(list_two)


# Пользователь вводит число. Определить, содержит ли список данное число x.
# Вывести информационное сообщение содержит или не содержит;


x = int(input("Введите число: "))
list_three = [random.randint(0, 20) for i in range(10)]

if x in list_three:
    print("Список содержит данное число.")
else:
    print("Список не содержит данное число.")


# Найдите сумму и произведение элементов списка.
# Результаты вывести на экран;


list_four = [random.randint(0, 20) for i in range(10)]

print(list_four)
prozv = 1
list_sum = 0


for item in list_four:
    prozv *= item
    list_sum += item
print("Произведение эелементов списка: ", prozv)
print("Сумма элементов списка: ", list_sum )



# Найти наибольший элемент списка и вывести его на экран;


list_five = [[random.randint(0, 20) for i in range(10)]]
for numbers in list_five:
    print("Наибольший элемент списка: ", max(numbers))


# Определите, есть ли в списке повторяющиеся элементы,
# если да, то вывести на экран это значение;


list_six = [20, 20, 10, 30, 40, 10]
repeating_elements = [list_six[nums] for nums in range(len(list_six)) if not nums == list_six.index(list_six[nums])]
print(repeating_elements)


# Поменять местами самый большой и самый маленький элементы списка;

spisok = [6,10,7,3,17,4,2]
print("Начальный список: ", spisok)
maximum = max(spisok)
minimum = min(spisok)
 
for elem in range(len(spisok)):
  if spisok[elem] == maximum:
    spisok[elem] = minimum
  elif spisok[elem] == minimum:
    spisok[elem] = maximum
 
print("Изменённый список: ", spisok)


# Дан произвольный список. Представьте его в обратном порядке.

last_list = ['Солнце', 'Дождь', 'Тучи', 'Ветер', 'Небо', 'Марс']
print("Стандартный список: ", last_list)
last_list.reverse()
print("Развёрнутый список:", last_list)

