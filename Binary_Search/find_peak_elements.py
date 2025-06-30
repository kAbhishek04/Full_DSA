#find peak elements mean such array [2, 3, 4,6,20, 4, 1] has peak elements 20.


"""
1609
274
if you are in ascending parts then the peak elements must be to the right
if you are in descending parts then the peak elements must be to the left
"""
def find_peak_elements(arr):
    left, right =0,len(arr)-1
    while left<right:
        mid=left+(right-left)//2
        if arr[mid]>arr[mid+1]:
            right=mid
        else:
            left=mid+1
    return left
# Example usage:
if __name__ == "__main__":
    arr = [2, 3, 4, 6, 20, 4, 1]
    peak_index = find_peak_elements(arr)
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



