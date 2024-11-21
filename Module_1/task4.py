# 4th program

input_str = '123.456'
input_float = float(input_str)

def first_try():
    input_float_fixed = input_float * 10
    input_int_fixed = int(input_float_fixed)
    print(input_int_fixed % 10)

def seckond_try():
    fraction = input_float - int(input_float)
    print(int(fraction*10))

first_try()
seckond_try()

