immutable_var : tuple = 1, True, "Super String"
print('Кортеж: ', immutable_var)
print('Первый элемент: ', immutable_var[0])
try:
    immutable_var[0] += 1
    print('Новый кортеж: ', immutable_var)
except Exception as e:
    print("Невозможно присвоить новое значение элементу неизменяемой переменной: ", e)

mutable_list : list = list(immutable_var)
# same as:
# mutable_var = [1, True, "Super String"]

print("Список: ", mutable_list)
mutable_list[0] += 1
mutable_list[1] = False
print("Новый список: ", mutable_list)


