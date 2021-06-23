set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6}
set3 = {3, 4, 6, 7}

print(set1.intersection(set2, set3))
print(set1.difference(set2, set3))
print(set1.union(set2, set3))

#Задача 5
#Добавить список элементов к заданному набору



sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]
sampleList = set(sampleList)
print('5', sampleSet.union(sampleList))




#Задача 6
#Вернуть новый набор идентичных предметов из заданных двух наборов


new_set1 = {10, 20, 30, 40, 50}
new_set2 = {30, 40, 50, 60, 70}
print('6', new_set1.intersection(new_set2))


#Задача 7
#Возвращает новый набор со всеми элементами из обоих наборов, удаляя дубликаты.

print('7', new_set1.union(new_set2))


#Задача 8
#Учитывая два набора Python, обновите первый набор элементами, которые существуют только в первом наборе, но не во втором наборе.



another_new_set1 = {10, 20, 30}
another_new_set2 = {20, 40, 50}
another_new_set1 = another_new_set1.difference(another_new_set2)
print('8', another_new_set1)


#Задача 9
#Удалите элементи 10, 20, 30 из следующего набора


set1 = {10, 20, 30, 40, 50}
set1.discard(10)
set1.discard(20)
set1.discard(30)
print('9', set1)


#Задача 10
#Проверьте, есть ли в двух наборах какие-либо общие элементы. Если да, отобразите общие элементы.


set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
set3 = "Есть общие элементы: " if set1.intersection(set2) else "Нету общих элементов"
print('10', set3,' - ', set1 & set2)


#Задача 11
#Обновите набор 1, добавив элементы из набора 2


set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
set1 |= set2
print('11', set1)



#Задача 12
#Удалите элементы из set1, которые не являются общими для set1 и set2


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
last_set = (set1 | set2) - (set1 & set2)

for item in last_set:
    if item in set1:
        set1.remove(item)
print('12', set1)