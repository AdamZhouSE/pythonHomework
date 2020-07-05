a = list(map(int, input().split(",")))
a.sort()
k = int(input())
if len(a) == 1:
    print(0)
elif a[-1] - a[0] - 2*k > 0:
    print(a[-1] - a[0] - 2*k)
elif a[-1] - a[-2] >= k:
    print(a[-1] - a[-2])
elif a[-1] - a[0] == 0:
    print(0)
else:
    print(a)
    print(k)