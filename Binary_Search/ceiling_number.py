#ceiling number meens the smallest number in the array which is greater than or equal to the target number.
# if the target number is greater than the largest number in the array then return -1.

def ceiling_number(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid]== target:
            return arr[mid]
        elif arr[mid]< target:
            left = mid + 1
        else:
            right = mid - 1
    return left
#dry run the code for the input array [1, 2, 8, 10, 10, 12, 19] and target 5
# left = 0, right = 6   
# mid = 3, arr[mid] = 10
# arr[mid] > target, so right = mid - 1 = 2
# left = 0, right = 2
# mid = 1, arr[mid] = 2 
# arr[mid] < target, so left = mid + 1 = 2
# left = 2, right = 2
# mid = 2, arr[mid] = 8
# arr[mid] > target, so right = mid - 1 = 1
# left = 2, right = 1
# since left > right, we return left which is 2
# so the ceiling number for the target 5 is 8

    