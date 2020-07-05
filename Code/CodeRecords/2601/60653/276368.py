m = int(input())
n = int(input())
k = int(input())
lst = []
for i in range(1, m+1):
    for j in range(1, n+1):
        lst.append(i*j)
lst.sort()
print(lst[k-1])