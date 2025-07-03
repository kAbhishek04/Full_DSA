def Search_in_rotated_array(nums,target):
    low,high=0,len(nums)-1
    while low<=high:
        mid=low+(high-low)//2
        if nums[mid]==target:
            return mid
        if nums[low]<=nums[mid]:
            if nums[low]<=target<nums[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if nums[mid]<target<=nums[high]:
                low=mid+1
            else:
                high=mid-1
    return -1
# Example usage:
nums = [4,5,6,7,0,1,2]
target = 0
result = Search_in_rotated_array(nums, target)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array.")
# Output: Element found at index: 4
# Example usage:    
# nums = [4,5,6,7,0,1,2]
