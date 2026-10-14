def is_prime(number):
    if number <= 1:
        return False
    for div in range(2, number):
        if number % div == 0:
            return False
    return True

def count_primes(limit):
    total = 0
    for number in range(1, limit + 1):
        if is_prime(number):
            total += 1
    return total

print(count_primes(10))
print(count_primes(20))