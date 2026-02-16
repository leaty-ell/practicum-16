def check_repeating(numbers, target) -> bool:
    """
    Checks if a number belongs to the set of repeating numbers.
    
    Args:
        numbers (list): List of natural numbers
        target (int): Number to check
    
    Returns:
        bool: True if target is a repeating number, False otherwise
    """
    count = numbers.count(target)
    return count > 1

def main():
    """
    Main function to read input and display result
    """
    numbers = list(map(int, input().split()))
    target = int(input())
    result = check_repeating(numbers, target)   
    print(result)

if __name__ == "__main__":
    main()
