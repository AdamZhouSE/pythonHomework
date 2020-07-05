a = input().split(",")
k = int(input())
a = list(map(int, a))
a = sorted(a)
if a[len(a)-1] - a[0] <= 2*k:
    print(0)
else:
    print(a[len(a)-1] - a[0] - 2*k)