import json


def load_dict(another, path):
    json.dump(another, open(path, 'w'), indent=2)


def some_func(*args, **kwargs):
    amount_elems = len(args) // 5
    lst = []
    for i in range(5):
        first = i * amount_elems
        last = first + amount_elems if i < 5 - 1 else None
        lst.append(list(args[first: last]))
    return dict(zip(kwargs.values(), lst))


def main():
    path = 'res.json'
    tpl = tuple(range(1, 22))
    another = dict((tuple([f'bl{l}' * 2] * 2) for l in 'qazwsx'))
    res = some_func(*tpl, **another)
    # print(res)
    load_dict(res, path)


if __name__ == '__main__':
    main()
