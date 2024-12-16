def print_params(a=1, b='строка', c=True):
    print('----------')
    print("a= ", a)
    print("b= ", b)
    print("c= ", c)


values_list = ['string', 12]
values_dict = {
        'b': 'string',
        'c': 32
        }
values_list_2 = [54.32, 'Строка']


print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, False)
