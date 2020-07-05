l=input().split(",")
D=int(input())
l[0]=l[0][1:len(l[0])]
l[-1]=l[-1][0:-1]
weights=[]
for i in l:
    weights.append(int(i))
lo, hi = max(weights), sum(weights)
while (lo <= hi):
    mid = (lo + hi) // 2  
    temp = 0
    day = 1
    for weight in weights:
        temp += weight
        if temp > mid:  
            day += 1
            temp = weight
    if day > D:  
        lo = mid + 1
    elif day <= D:
        hi = mid - 1
print(lo)