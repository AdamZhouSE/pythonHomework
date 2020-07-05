n = int(input())
a = input().split()
b = input().split()
res = 0
for i in range(n-1):
    for j in range(i,n):
        index_i = b.index(a[i])
        index_j = b.index(a[j])
        if index_i>index_j:
            res += 1
print(res)