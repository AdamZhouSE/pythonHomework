def minEatingSpeed(piles, H):
        for k in range(math.ceil(sum(piles) / H), max(piles) + 1):
            if sum((p - 1) // k + 1 for p in piles) <= H: 
                return k
            
print(input())            
            