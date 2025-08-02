#find peak elements mean such array [2, 3, 4,6,20, 4, 1] has peak elements 20.


"""
1609
274
if you are in ascending parts then the peak elements must be to the right
if you are in descending parts then the peak elements must be to the left
"""


from typing import List


def findPeakElement(arr: List[int]) -> int:
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2

        # Check if mid is a peak
        if (mid == 0 or arr[mid] >= arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] >= arr[mid + 1]):
            return mid
        # If the left neighbor is greater, peak must be on the left side
        elif mid > 0 and arr[mid - 1] > arr[mid]:
            high = mid - 1
        else:  # Else the peak is on the right side
            low = mid + 1

    return -1  # Just in case no peak is found (though at least one peak is guaranteed)

# Example usage:
if __name__ == "__main__":
    arr = [2, 3, 4, 6, 20, 4, 1]
    peak_index = findPeakElement(arr)
    print(f"The peak element is at index {peak_index} with value {arr[peak_index]}")   
#dry run the code for the input array [2, 3, 4, 6, 20, 4, 1]
# # left = 0, right = 6
# # # mid = 3, arr[mid] = 6
# # # arr[mid] < arr[mid+1], so left = mid + 1 = 4
# # left = 4, right = 6 
# # # mid = 5, arr[mid] = 4
# # # arr[mid] > arr[mid+1], so right = mid = 5 
# # left = 4, right = 5
# # # mid = 4, arr[mid] = 20
# # # arr[mid] > arr[mid+1], so right = mid = 4
# # left = 4, right = 4
# # since left == right, we return left which is 4
# # so the peak element for the input array is 20 at index 4
# # Time Complexity: O(log n)
# # # Space Complexity: O(1)



