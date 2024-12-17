def process_last_digit(number: int) -> int:
    if number != 0:
        return number
    return 1


def get_multiplied_digits(number: int) -> int:
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) < 2:
        return process_last_digit(first)
    return first * get_multiplied_digits(int(str_number[1:]))


result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)
