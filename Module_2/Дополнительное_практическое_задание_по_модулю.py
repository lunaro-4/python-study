num = int(input("Введите число: "))


def generate_password(number: int) -> list:
    password: list = []
    for i in range(1, number):
        for j in range(i, number):
            ij_summ = i + j
            if number % ij_summ == 0:
                if i == j:
                    continue
                password.append(str(i))
                password.append(str(j))
    return password


password = generate_password(num)
print(''.join(password))
