def number_banquets(arr, k, m):
    low, high = min(arr), max(arr)
    result = -1
    while low <= high:
        mid = low + (high - low) // 2
        if ispossible(arr, mid, m, k):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result

def ispossible(num, day, m, k):
    cut = 0
    no_of_day = 0
    for n in num:
        if n <= day:
            cut += 1
            if cut == k:
                no_of_day += 1
                cut = 0
        else:
            cut = 0
    return no_of_day >= m
