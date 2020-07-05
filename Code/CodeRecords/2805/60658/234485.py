n = int(input())
li = [int(x) for x in input().split()]
i,j=0,1
m=1
while i<n and j<n:
    if li[j]>li[j-1]:
        j+=1
        m = max(j-i,m)
    else:
        i=j
        j+=1
print(m)
        