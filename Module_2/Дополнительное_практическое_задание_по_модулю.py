# Функция также добавляет пару '11' для четных чисел,
# хотя в примере этого не было
def generate_password(number: int) -> list:
    password: list = []
    for i in range(1, number):
        for j in range(i, number):
            ij_summ = i + j
            if number % ij_summ == 0:
                password.append(str(i))
                password.append(str(j))
    # print(''.join(password))
    return password


print(''.join(generate_password(6)))
print(''.join(generate_password(7)))
print(''.join(generate_password(8)))
print(''.join(generate_password(9)))
print(''.join(generate_password(19)))
