
first = int(input('Enter first value : '))
second = int(input('Enter second value : '))
third = int(input('Enter third value : '))

first_same_as_second = first==second
second_same_as_third = second==third
third_same_as_first = third==first


if first_same_as_second and second_same_as_third:
    print('3')

elif first_same_as_second or second_same_as_third or third_same_as_first:
    print('2')
else:
    print('0')
