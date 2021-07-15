from datetime import datetime


def measure_exec_time(func):

    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        last = datetime.now()
        another = last - start
        print(func.__name__, str(another))
        return result
    return wrapper


def gen_list_dicts(n=0):
    lst = []
    for items in range(n + 1):
        lst.append({j: j ** 2 for j in range(items + 1)})
    return lst


for i in range(5):
    print(gen_list_dicts(i))

list_one = list(range(1, 11))
list_two = list(range(11, 21))
list_three = list(range(21, 31))

list_one, list_three = (filter(lambda x: not x % 2, lst) for lst in (list_one, list_three))
list_two = filter(lambda x: x % 2, list_two)

union = zip(list_one, list_two, list_three)
sum_of_list = map(sum, union)
sum_odd_of_lis = list(filter(lambda x: x % 2, sum_of_list))

print(sum_odd_of_lis)

