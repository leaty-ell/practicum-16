from itertools import permutations

def get_permutations(numbers) -> list:
    """
    Gets all permutations of a set in lexicographic order.
    
    Args:
        numbers (list): List of natural numbers
    
    Returns:
        list: List of all permutations as tuples
    """
    numbers.sort()
    all_permutations = list(permutations(numbers))
    
    return all_permutations

def main():
    """
    Main function to read input and display result
    """
    numbers = list(map(int, input().split()))
    
    permutations_list = get_permutations(numbers)
    for perm in permutations_list:
        print(list(perm))

if __name__ == "__main__":
    main()
