def findMax(n,pre):
    cur = n//2+n//3+n//4
    if cur<=pre:
        return pre
    else:
        cur = findMax(n//2,n//2) +findMax(n//3,n//3) + findMax(n//4,n//4)
        return cur

t = int(input())
for i in range(t):
    print(findMax(int(input()),0))
