def is_prime(num) -> bool:
    """
    Checks if a number is prime.
    
    Args:
        num (int): Number to check
    
    Returns:
        bool: True if the number is prime, False otherwise
    """
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def find_primes(n) -> list:
    """
    Finds all prime numbers less than n.
    
    Args:
        n (int): Upper bound (exclusive)
    
    Returns:
        list: List of prime numbers less than n
    """
    primes = []
    for num in range(2, n):
        if is_prime(num):
            primes.append(num)
    
    return primes

def main():
    """
    Main function to read input and display result
    """
    n = int(input())
    primes = find_primes(n)
    print(primes)

if __name__ == "__main__":
    main()
