from itertools import combinations

def get_all_subsets(numbers) -> list:
    """
    Gets all subsets of a given set using itertools.combinations.
    
    Args:
        numbers (list): List of natural numbers
    
    Returns:
        list: List of all subsets as lists, where each subset is a list of numbers
    """
    all_subsets = []
    
    for i in range(len(numbers) + 1):
        for combo in combinations(numbers, i):
            all_subsets.append(list(combo))
    
    return all_subsets

def main() -> None:
    """
    Main function to read input and display all subsets.
    """
    numbers = list(map(int, input().split()))
    subsets = get_all_subsets(numbers)
    
    for subset in subsets:
        print(subset)

if __name__ == "__main__":
    main()
