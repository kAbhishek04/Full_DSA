#Split Array Largest Sum 

'''
Possible Splits with 2 subarrays:
[7] and [2, 5, 10, 8] → sums: 7 and 25 → max = 25

[7, 2] and [5, 10, 8] → sums: 9 and 23 → max = 23

[7, 2, 5] and [10, 8] → sums: 14 and 18 → max = 18 ✅

[7, 2, 5, 10] and [8] → sums: 24 and 8 → max = 24

'''

def split_array(nums, m):
    low, high = max(nums), sum(nums)
    while low < high:
        mid = (low + high) // 2
        if can_split(nums, m, mid):
            high = mid
        else:   
            low = mid + 1
    return low
def can_split(nums, m, max_sum):
    count, current_sum = 1, 0
    for num in nums:
        current_sum += num
        if current_sum > max_sum:
            count += 1
            current_sum = num
            if count > m:
                return False
    return True
# Example usage:
if __name__ == "__main__":
    nums = [7, 2, 5, 10, 8]
    m = 2
    result = split_array(nums, m)
    print(f"The minimum largest sum of {m} subarrays is: {result}")  # Output: 18