
def count_individual(arg) -> int:
    if isinstance(arg, str):
        return len(arg)
    elif isinstance(arg, int):
        return arg
    print(f"Unhandled input! arg {arg} is {type(arg)}")
    exit()


def is_iterable(variable):
    return isinstance(variable, list) or isinstance(variable, tuple) or isinstance(variable, set)




def count_main(*args) -> int:
    sum: int = 0
    for arg in args:
        if isinstance(arg, dict):
            sum += count_main(*arg.keys())
            sum += count_main(*arg.values())
        elif is_iterable(arg):
            sum += count_main(*arg)
        else:
            sum += count_individual(arg)
    return sum


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
print(count_main(*data_structure))

