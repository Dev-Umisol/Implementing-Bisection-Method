def square_root_bisection(square_root_num, tolerance=1e-7, max_iterations=50):
    if square_root_num < 0:
        raise ValueError ("Square root of negative number is not defined in real numbers")
    
    if square_root_num == 0 or square_root_num == 1:
        print(f"The square root of {square_root_num} is {square_root_num}")
        return square_root_num
    
    low = 0
    high = max(1, square_root_num)
    root = None
    
    for i in range(max_iterations):
        mid = (low + high) / 2
        
        if abs(mid * mid - square_root_num) <= tolerance:
            root = mid
            
            break
        elif (mid * mid) < square_root_num:
            low = mid
        else:
            high = mid
            
    if root:
        print(f"The square root of {square_root_num} is approximately {root}")
        return root
    else:
        print(f"Failed to converge within {max_iterations} iterations")
        return None

square_root_bisection(0.001, 1e-7, 50)