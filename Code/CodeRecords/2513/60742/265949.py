a = []
n = int(input())
for t in range(n):
    l = [int(i) for i in input().split(',')]
    for i in l:
        a.append(i)
a.sort()
k = int(input())
print(a[k-1])