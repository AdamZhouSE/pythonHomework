n = int(input())
a = input().split(" ")
for i in range(0, n):
    if int(a[i]) == 1:
        small = i
    elif int(a[i]) == n:
        big = i
result = max(n - 1 - small, n - 1 - big, small, big, big - small)
print(result)