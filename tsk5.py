def ratosphen(n) -> set:
    """
    Finds all prime numbers less than n using the Sieve of Eratosthenes algorithm with sets.
    
    Args:
        n (int): Upper bound (exclusive). Finds primes less than n.
    
    Returns:
        set: A set containing all prime numbers less than n
    """
    if n <= 2:
        return set()
    
    numbers = set(range(2, n))
    
    for i in range(2, int(n**0.5) + 1):
        for multiple in range(i * 2, n, i):
            numbers.discard(multiple)
    
    return numbers

def main():
    """
    Main function to read input and display result.
    """
    n = int(input())
    primes_set = ratosphen(n)
    primes_list = sorted(primes_set)
    print(primes_list)

if __name__ == "__main__":
    main()


