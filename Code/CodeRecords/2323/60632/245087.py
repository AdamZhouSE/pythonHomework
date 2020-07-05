data = list(map(int, input().split(',')))
k = int(input())
dis = max(data) - min(data)
if dis > 2 * k:
    print(abs(dis - 2 * k))
else:
    print(0)