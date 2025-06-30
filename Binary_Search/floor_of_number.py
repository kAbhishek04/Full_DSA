#floor of number means the largest number in the array which is less than or equal to the target number.
# if the target number is less than the smallest number in the array then return -1.
def floor_number(arr,target):
    left,right=0,len(arr)-1
    while left<=right:
        mid=right+(left-right)//2
        if arr[mid]==target:
            return arr[mid]
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return right if right>=0 else -1
# dry run the code for the input array [1, 2, 8, 10, 10, 12, 19] and target 5
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
# since left > right, we return right which is 1
# so the floor number for the target 5 is 2

    