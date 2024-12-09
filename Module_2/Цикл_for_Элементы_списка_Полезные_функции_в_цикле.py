numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes: list = []
not_primes: list = []

for i in range(len(numbers)):
    num = numbers[i]
    if num == 0 or num == 1:
        continue
    is_prime = True
    for j in range(2, num-1):
        fraction = num % j
        is_prime = fraction != 0
        if not is_prime:
            not_primes.append(num)
            break
    if is_prime:
        primes.append(num)


print("Primes: ", primes)
print("Not Primes: ", not_primes)
