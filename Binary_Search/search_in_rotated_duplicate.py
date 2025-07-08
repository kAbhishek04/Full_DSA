#search elements in rotated sorted array with duplicates
#[2,5,6,0,0,1,2] target=1

def search_in_rotated_duplicate(nums, target):
    if not nums:
        return -1
    low,high=0,len(nums)-1
    while low<=high:
        mid=low+(high-low)//2
        if nums[mid]==target:
            return mid
        if nums[low]==nums[mid] and nums[mid]==nums[high]:
            low=low+1
            high=high+1
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
if __name__=="__main__":
#write test cases
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 1
    result = search_in_rotated_duplicate(nums, target)
    print(f"Target {target} found at index: {result}")  # Expected output: Target 1 found at index: 5

    target = 2
    result = search_in_rotated_duplicate(nums, target)
    print(f"Target {target} found at index: {result}")  # Expected output: Target 2 found at index: 0 or 6

    target = 3
    result = search_in_rotated_duplicate(nums, target)
    print(f"Target {target} found at index: {result}")  # Expected output: Target 3 found at index: -1 (not found)
        
    