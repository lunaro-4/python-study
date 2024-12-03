my_string : str = input("\\/ Введите текст: \\/ \n")
print("Верхний регистр: ", my_string.upper())
print("Нижний регистр: ", my_string.lower())
# Решил двумя способами
def no_space_1():
    print("Без пробелов: ", my_string.replace(' ', ''))
def no_space_2():
    print("Без пробелов: ", ''.join(my_string.split(' ')))
no_space_1()
# no_space_2()
print("Первый символ: ", my_string[0])
print("Последний символ: ", my_string[-1])
