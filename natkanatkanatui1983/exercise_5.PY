

print(6 % 2)
print(7 % 2)



number % divisor == 0
def is_prime(number):
    if number < 2:
        return false

        for divisor in range(2, number):
            if number % divisor == 0:
                return False

def is_prime(number):
    if number < 2:
        return False

for divisor in range(2, number):
    if number % divisor == 0:
        return False
return True

def count_primes(limit):
    count = 0:

    for number in range(2,limit + 1):
        if is _prime(number):
            count += 1
    return count

def is_prime(number):
    if number < 2:
        return False
for divisor in range(2, number):
    if number % divisor == 0:
        return False
return true

def count_primes(Limit):
    count = 0

    for number in range(2, Limit + 1):
        if is_prime(number):
            count += 1
    return count

    print(count_primes(10))
    print(count_primes(20))