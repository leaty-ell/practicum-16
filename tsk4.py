def belongs_to_intersection(set1, set2, target) -> bool:
    """
    Checks if a number belongs to the intersection of two sets.
    
    Args:
        set1 (set): First set of numbers
        set2 (set): Second set of numbers
        target (int): Number to check
    
    Returns:
        bool: True if target is in the intersection, False otherwise
    """
    return target in set1 and target in set2

def main():
    """
    Main function to read input and display result
    """
    set1 = set(map(int, input().split()))
    set2 = set(map(int, input().split()))
    target = int(input())
  
    result = belongs_to_intersection(set1, set2, target)
    print(result)

if __name__ == "__main__":
    main()
