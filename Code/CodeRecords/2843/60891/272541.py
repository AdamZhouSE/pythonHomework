n = int(input())
a = [int(i) for i in input().split()]
for i in range(0, n - 1):
    print(a[i] + a[i + 1], end=" ")
print(a[n - 1])
