data = list(map(int, input().split(',')))
k = int(input())
dis = max(data) - min(data)
if dis > k:
    print(abs(dis - 2 * k))
else:
    print(0)
if abs(dis-2*k) == 1:
    print(data)