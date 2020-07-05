n = int(input())
a = [int(i) for i in input().split()]
res = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if a[i]<a[j] and a[j]<a[k]:
                res += 1
print(res,end='')