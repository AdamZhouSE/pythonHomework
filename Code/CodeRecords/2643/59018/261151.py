def maxSatisfied(customers, grumpy, X):
        sum_lose, l, lose, res = 0, 0, float("-inf"), 0
        for r in range(len(customers)):
            res += (not grumpy[r]) * customers[r]
            sum_lose += grumpy[r] * customers[r]
            if r - l + 1 > X:
                sum_lose -= grumpy[l] * customers[l]
                l += 1
            if r - l + 1 == X and sum_lose > lose:
                lose = sum_lose
        return res + lose
    
    
info1=input().split(',')
customers=[int(x) for x in info1]
info2=input().split(',')
grumpy=[int(x) for x in info2]
X=int(input())
print(maxSatisfied(customers, grumpy, X))