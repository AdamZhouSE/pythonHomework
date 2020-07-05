a = list(map(int, input().split(","))).sort()
k = int(input())
if a[-1] - a[0] - 2*k > 0:
    print(a[-1] - a[0] - 2*k)
else:
    print(a)