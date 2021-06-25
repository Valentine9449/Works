# Задача 1
# Дано список словорей
# Создать список кортежей из списка словаря


dict_one = [{'color': 'red', 'value': 'high'}, {'color': 'yellow', 'value': 'low'}]

lst = []
for d in dict_one:
    lst.append(tuple(d.values()))
print(lst)

# Задача 2
# Дано словарь, преобразовать его в список кортежей

a_dictionary = {"a": 1, "b": 2, "c": 3}

lst_two = a_dictionary.items()

la = []
for a in lst_two:
    la.append(tuple(a))

print(la)

# Задача 3
# Дано два списка,Создать из них список кортежей list_c = [(1,5), (2,6), (3,7), (4,8)]


list_a = [1, 2, 3, 4]

list_b = [5, 6, 7, 8]

a = list(zip(list_a, list_b))

print(a)

# Задача 4
# Дано словарь,Создать кортеж занчений для первих трьох єлементов словоря

dict_three = {1: 'entry 1', 2: 'entry 2', 3: 'entry 3', 4: 'entry 4'}
list_dict = list(dict_three.values())
print(tuple(list_dict[:3]))

# Задача 5
# Дано список, добавить значение 'foo' на первое место списка и конвертировать в tuple

last_list = ["bar", "baz", "qux", "etc"]

last_list.insert(0, 'foo')
print(tuple(last_list))
