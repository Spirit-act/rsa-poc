#!/usr/env/python3

p: int = 1 # first prime number
q: int = 3 # second prime number

n: int = p * q # modulus


# @see https://en.wikipedia.org/wiki/Primality_test
def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if not n%2 or not n%3:
        return False
    i = 5
    stop = int(n**0.5)
    while i <= stop:
        if not n%i or not n%(i + 2):
            return False
        i += 6
    return True


# recursive Euclidean algorithm
# @see https://en.wikipedia.org/wiki/Euclidean_algorithm
def gcd(x: int, y: int) -> int:
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
