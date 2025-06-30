#agnostics number mean you are not sure about the array is sorted in ascending or descending order.
#[2,4,6,8,10,12,14] is sorted in ascending order.
#[14,12,10,8,6,4,2] is sorted in descending

def agnostics_number(arr,target):
    left, right = 0, len(arr) - 1
    as_asc = arr[left] < arr[right]
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        if as_asc:
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if arr[mid] > target:
                left = mid + 1
            else:
                right = mid - 1
    return -1
if __name__ == "__main__":
    arr = [2, 4, 6, 8, 10, 12, 14]
    target = 10
    index = agnostics_number(arr, target)
    if index != -1:
        print(f"Element {target} found at index {index}")
    else:
        print(f"Element {target} not found in the array")
