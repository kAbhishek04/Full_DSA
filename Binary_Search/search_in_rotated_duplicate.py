# search elements in rotated sorted array with duplicates
# [2,5,6,0,0,1,2] target=1


from typing import List


def search_in_rotated_duplicate(self, nums: List[int], target: int) -> bool:
    if not nums:
        return False

    low, high = 0, len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] == target:
            return True

        # If duplicates make it hard to decide the sorted side
        if nums[low] == nums[mid] == nums[high]:
            low += 1
            high -= 1
        elif nums[low] <= nums[mid]:  # Left side is sorted
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:  # Right side is sorted
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return False


if __name__ == "__main__":
    # write test cases
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 1
    result = search_in_rotated_duplicate(nums, target)
    print(
        f"Target {target} found at index: {result}"
    )  # Expected output: Target 1 found at index: 5

    target = 2
    result = search_in_rotated_duplicate(nums, target)
    print(
        f"Target {target} found at index: {result}"
    )  # Expected output: Target 2 found at index: 0 or 6

    target = 3
    result = search_in_rotated_duplicate(nums, target)
    print(
        f"Target {target} found at index: {result}"
    )  # Expected output: Target 3 found at index: -1 (not found)
