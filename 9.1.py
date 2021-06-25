# Создайте словарь с количеством элементов не менее 5-ти.
# Поменяйте местами первый и последний элемент объекта.
# Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value».
# Выведите на печать итоговый словарь. Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).

# 1

car = {'brand': 'Renault',
       'model': 'Logan',
       'color': 'Silver',
       'price': 4600,
       'status': 'new'
       }

print("Задание - 1")
print("Начальный словарь: ", car)
print(id(car))

car['brand'], car['status'] = car['status'], car['brand']
car.pop('model')
car.update({'new_key': 'new_value'})

print("Итоговый словарь: ", car)
print(id(car))

# Как получить значение по ключу "marks" словаря student = {"name": "Emma", "class": 9, "marks": 75}
# 2


print("Задание - 2")
student = {"name": "Emma", "class": 9, "marks": 75}
print(student.get('marks'))

# Как получить "d":sample = {"1":["a","b"], "2":["c","d"]}.


print("Задание - 3")
sample = {"1": ["a", "b"], "2": ["c", "d"]}
for sam in sample.values():
    if 'd' in sam:
        print(sam[1])


#Дан список стран и городов каждой страны. Затем дан cам писок названия городов.
#Для каждого города укажите, в какой стране он находится.


print("Задание - 4")
dict_ = {}
list_2 = ["Киев", "Токио", "Минск", "Сочи", "Мюнхен"]
list_1 = ["Украина-Киев", "Россия-Сочи", "Беларусь-Минск", "Япония-Токио", "Германия-Мюнхен"]
for i in list_1:
        spl = i.split('-')
        if spl[1] in list_2:
                dict_.update({spl[0]:spl[1]})
print(dict_)




#Что выведет этот код? p = {"name": "Mike", "salary": 8000} print(p.get("age")).


print("Задание - 5")
p = {"name": "Mike", "salary": 8000}
print("Выведет - None ")
print(p.get("age"))



#Создайте словарь, в котором ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в куб.


print("Задание - 6")
first = range(10)
values = {i ** 3 for i in range(1, 11)}
print(dict(zip(first, values)))



#Создайте словарь из строки следующим образом: в качестве ключей возьмите буквы строки,
# а значениями пусть будут числа, соответствующие количеству вхождений данной буквы в строку.

print("Задание - 7")
text = input("Введите слово: ")

dictionary_2 = {i: text.count(i) for i in text}
print(dictionary_2)





#Для английского алфовита сгенерировать словарь-шифратор, то есть словарь, где ключ - буква алфавита,
# а значение являются - случайное значение. Используя словарь, зашифровать/расшифровать введенное сообщение


word = input("Введите слово: ")
print("Введённое слово:", word)

encoder = {
    'a': 2, 'b': 1,
    'c': 3, 'd': 5,
    'e': 17, 'f': 8,
    'g': 12, 'h': 111,
    'i': 4, 'j': 0,
    'k': 16, 'l': 43,
    'm': 22, 'n': 883,
    'o': 56, 'p': 91,
    'q': 9, 'r': 100,
    's': 8, 'u': 80,
    'v': 10, 'w': 54,
    'x': 20, 'y': 22,
    'z': 6
}

print("Шифровка: ")

for chars in word:
    if chars in encoder.keys():
        chars = encoder.get(chars)
    print(chars, end='')

number = int(input("\nВведите число: "))


decoder = {v: k for k, v in encoder.items()}

if number in decoder.keys():
    number = decoder.get(number)
    print(number, end='')
else:
    print("В словаре нету такого ключа")
