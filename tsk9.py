from itertools import combinations

def get_k_subsets(numbers, k) -> list:
    """
    Gets all k-element subsets of a given set.
    
    Args:
        numbers (list): List of natural numbers
        k (int): Size of subsets
    
    Returns:
        list: List of all k-element subsets as lists
    """
    k_subsets = list(combinations(numbers, k))
    
    result = []
    for subset in k_subsets:
        result.append(list(subset))
    
    return result

def main():
    """
    Main function to read input and display result
    """
    numbers = list(map(int, input().split()))
    k = int(input())
    subsets = get_k_subsets(numbers, k)
    
    for subset in subsets:
        print(subset)

if __name__ == "__main__":
    main()
