def nth_root(n, X):
    """
    Function to find the nth root of a number X using binary search.
    
    :param n: The degree of the root (e.g., 2 for square root, 3 for cube root)
    :param X: The number for which we want to find the nth root
    :return: The nth root of X
    """
    if X < 0 and n % 2 == 0:
        raise ValueError("Cannot compute even root of a negative number.")
    
    low = 0
    high = max(1, X)  # The nth root of X is at most X if X >= 1
    precision = 1e-10  # Precision for the result
    
    while high - low > precision:
        mid = (low + high) / 2
        mid_powered = mid ** n
        
        if mid_powered < X:
            low = mid
        else:
            high = mid
            
    return (low + high) / 2