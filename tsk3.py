def only_sweettooth_likes(sweettooth_likes, friends_likes) -> int:
    """
    Finds products that only Sweettooth likes.
    
    Args:
        sweettooth_likes (list): Products liked by Sweettooth
        friends_likes (list): List of lists, each inner list contains products liked by a friend
    
    Returns:
        int: Number of products liked only by Sweettooth
    """
    sweettooth_set = set(sweettooth_likes)
    
    friends_set = set()
  
    for friend in friends_likes:
        for product in friend:
            friends_set.add(product)
    
    count = 0
    for product in sweettooth_set:
        if product not in friends_set:
            count += 1
    
    return count

def main():
    """
    Main function to read input and display result
    """
    sweettooth_likes = input().split()
    
    n = int(input())
    
    friends_likes = []
    for i in range(n):
        friend = input().split()
        friends_likes.append(friend)
    
    result = only_sweettooth_likes(sweettooth_likes, friends_likes)
    print(result)

if __name__ == "__main__":
    main()
