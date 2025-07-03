from typing import List


class Solution:
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        first=self.binary_search(nums,target,True)
        last=self.binary_search(nums,target,False)
        return [first,last]
    def binary_search(self, nums: List[int], target: int, find_first: bool) -> int:
        low, high = 0, len(nums) - 1
        ans = -1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                ans = mid  # Save the current index
                if find_first:
                    high = mid - 1  # Look on left
                else:
                    low = mid + 1   # Look on right
        return ans
    
# Example usage:
nums = [5,7,7,8,8,10] 
target = 8
solution = Solution()
result = solution.searchRange(nums, target)
print(f"First and last positions of {target} are: {result}")
# Output: First and last positions of 8 are: [3, 4]