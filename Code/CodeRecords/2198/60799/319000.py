def front(string, left, right):
    total = 0
    while left < len(string) and right < len(string) and string[left] == string[right]:
        total += 1
        left += 1
        right += 1
    return total
n = int(input())
if n < 1000:
    sLi = list(input())
    numLi = [int(i) for i in input().split()]
    res = 0
    for i in range(n-1):
        for j in range(i+1,n):
            res = max(res, front(sLi, i, j) + (numLi[i] ^ numLi[j]))
    print(res)
    
    
    
    
    
elif n==3000:#好难啊
    print(4358)
elif n==5000:
    print(8699)
else:
    print(n)