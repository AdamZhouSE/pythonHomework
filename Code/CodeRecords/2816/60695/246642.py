n = int(input())
a = input().split(" ")
for i in range(0, n):
    a[i] = int(a[i])
a = sorted(a)
if n % 2 == 0:
    print(a[int(n/2-1)])
else:
    print(a[int((n-1)/2)])