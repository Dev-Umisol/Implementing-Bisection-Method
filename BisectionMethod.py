def square_root_bisection(square_root_num, tolerance=1e-7, max_iterations=50):
    """ Finds the square root of a number using bisection method """
    if square_root_num < 0:
        raise ValueError ("Square root of negative number is not defined in real numbers") # <-- Edge case for negative numbers
    
    if square_root_num == 0 or square_root_num == 1:
        print(f"The square root of {square_root_num} is {square_root_num}")
        return square_root_num # <-- Edge case for 0 and 1 since, square root of them is just 0 and 1
    
    # Initial bounds
    low = 0
    high = max(1, square_root_num)
    root = None
    
    for i in range(max_iterations):
        mid = (low + high) / 2 # <-- finding midpoint
        
        if high - low <= tolerance: # Check if within tolerance
            root = mid
            break
        elif (mid*mid) < square_root_num:
            low = mid # Root in upper half
        else:
            high = mid # Root in lower half
            
    if root:
        print(f"The square root of {square_root_num} is approximately {root}")
        return root
    else:
        print(f"Failed to converge within {max_iterations} iterations")
        return None

# -->Example usage<--
square_root_bisection(0)
square_root_bisection(0.25, 1e-7, 50)
square_root_bisection(1)
square_root_bisection(81, 1e-3, 50)
square_root_bisection(225, 1e-3, 100)
square_root_bisection(0.001, 1e-7, 50)
square_root_bisection(225, 1e-7, 10)
