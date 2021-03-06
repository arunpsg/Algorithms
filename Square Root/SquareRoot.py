def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    left = 0
    right = number
    while left <= right:
        mid = (left + right)//2
        if mid * mid <= number < (mid+1)*(mid+1):
            return mid
        elif number < mid * mid:
            right = mid
        else:
            left = mid + 1
    pass

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print("Pass" if  (1000 == sqrt(1000001)) else "Fail")
print("Pass" if  (10 == sqrt(100.25)) else "Fail")