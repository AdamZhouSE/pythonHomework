ts = int(input())
for t in range(ts):
    x1, y1, x2, y2 = map(int, input().split(' '))
    x3, y3, x4, y4 = map(int, input().split(' '))
    if max(x1, x3) < min(x2, x4) and max(y2, y4) < min(y1, y3):
        print(1)
    else:
        print(0)
