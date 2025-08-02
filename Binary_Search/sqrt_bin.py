def sqrt_binn(self, x: int) -> int:
        if x < 2:
            return x
        
        low, high = 1, x
        while low <= high:
            mid = low + (high - low) // 2
            square = mid * mid
            
            if square == x:
                return mid
            elif square < x:
                low = mid + 1
            else:
                high = mid - 1
        
        return high  # or low - 1, both are correct here

if __name__ == "__main__":
    num = 40
    print(sqrt_binn(num))  # utput: 2
    