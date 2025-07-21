'''
pile=[3,6,7,11]
h=8
min kth koko can eat in h hours
min=3 max=11
'''
import math     as mx
def koko_eating(pile,h):
    low, high = min(pile), max(pile)
    while low <high:
        mid=low+(high-low)//2
        if can_eat(pile,mid,h):
            high=mid
        else:
            low=mid+1   
    return low
def can_eat(pile, k, h):
    hours=0
    for p in pile:
        hours+=mx.ceil(p/k)
    return hours <= h
# Example usage
if __name__ == "__main__":
    pile = [3, 6, 7, 11]
    h = 8
    print(koko_eating(pile, h))  # Output: 4