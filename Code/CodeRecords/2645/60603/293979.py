import math
def minEatingSpeed(piles, H):
        for k in range(math.ceil(sum(piles) / H), max(piles) + 1):
            if sum((p - 1) // k + 1 for p in piles) <= H: 
                return k
            
info=input()[1:-1].split(',')
piles=[int(y) for y in info]
H=int(input())
print(minEatingSpeed(piles, H))