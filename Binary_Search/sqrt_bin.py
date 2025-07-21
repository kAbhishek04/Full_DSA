def sqrt_binn(num):
    low, high = 1, num

    while(low<=high):
        mid=low+(high-low)//2
        if mid*mid==num:
            return mid
        elif mid*mid < num:
            low = mid + 1
        else:
            high = mid - 1
    return high
if __name__ == "__main__":
    num = 40
    print(sqrt_binn(num))  # utput: 2
    