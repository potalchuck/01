numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for number in numbers:
    is_prime = True
    if number <= 1:
        is_prime = False
    else:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)
new_not_primes=not_primes[1:]
print("Primes:", primes)
print("Not Primes:", new_not_primes)