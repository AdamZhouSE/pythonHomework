n = int(input())
a = list(map(int, input().split()))


res = 0

for i in range(n):
    temp = 0
    for j in range(i,n):
        if a[j] <= a[i]*2:
            temp+=1
        else:
            break
    if temp > res:
        res = temp
        
print(res)