n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
res = 1
for i in range(n-1):
    j = i
    while j<n-1 and a[j+1]>a[j]:
        j += 1
    j = j+1-i
    if res<j:
        res = j
print (res)