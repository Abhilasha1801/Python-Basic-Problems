def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    # Only need to check up to sqrt(num)
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def print_primes_up_to(N: int):
    primes = []
    for x in range(2, N + 1):
        if is_prime(x):
            primes.append(x)
    print(" ".join(str(p) for p in primes))

if __name__ == "__main__":
    N = int(input("Enter N: "))
    print_primes_up_to(N)
