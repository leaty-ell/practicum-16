def get_all_subsets(numbers) -> list:
    """
    Gets all subsets of a given set using iterative method.
    
    Args:
        numbers (list): List of natural numbers
    
    Returns:
        list: List of all subsets as lists
    """
    all_subsets = [[]]
    
    for num in numbers:
        new_subsets = []
        for subset in all_subsets:
            new_subset = subset + [num]
            new_subsets.append(new_subset)
        
        all_subsets.extend(new_subsets)
    
    return all_subsets

def main():
    """
    Main function to read input and display result
    """
    numbers = list(map(int, input().split()))
    
    subsets = get_all_subsets(numbers)
    for subset in subsets:
        print(subset)

if __name__ == "__main__":
    main()
