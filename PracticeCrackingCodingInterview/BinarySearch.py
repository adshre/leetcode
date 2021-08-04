# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
def binarySearch(a, x):
    low = 0
    high = len(a) - 1

    while low <= high :
        mid = low + high // 2 # // for int division as indices cannot be float
        if a[mid] < x :
            low = mid + 1
        elif a[mid] > x :
            high = mid - 1
        else :
            return mid
    return -1                # if low > high error case
    
    
def binarySearchRecursive(a, x, low, high):
    if low > high : return -1.    # base condition check for error
    
    mid = low + high // 2
    
    if a[mid] < x :
        return binarySearchRecursive(a, x ,mid + 1, high)
    elif a[mid] > x :
        return binarySearchRecursive(a, x, low , mid - 1)
    else :
        return mid
        
    
    
    
input = [12, 12, 13, 14, 18, 50, 88, 45, 90, 98]  # Always a sorted array
number = 98

print("***** binary search *****")
print(binarySearch(input, number))
print("******** recursive binary search ******")
print(binarySearchRecursive(input, number, 0, len(input)-1 ))
