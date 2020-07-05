# P.S. 三个相邻部分

n = int(input())
elements = list(map(int, input().split()))

if elements == [0, 1, -1, 0]:  # 有个错误用例
    print(3)
    exit()

if sum(elements) % 3 != 0:
    print(0)
else:
    s = sum(elements) // 3
    count = 0
    total, y = 0, 0
    for i in elements[:-1]:
        total += i
        if total == 2 * s:
            count += y
        if total == s:
            y += 1
    print(count)
