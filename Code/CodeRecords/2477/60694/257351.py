T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    # 以第一个矩形为基准
    if x4 < x1 or y4 > y1 or x3 > x2 or y3 < y2:
        print(0)
    else:
        print(1)
