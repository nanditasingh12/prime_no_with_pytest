def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def first_100_primes():
    primes = []
    num = 2
    while len(primes) < 100:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes
