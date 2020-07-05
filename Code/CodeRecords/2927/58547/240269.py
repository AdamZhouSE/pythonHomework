def slope(point_a, point_b):
    # 计算斜率
    if point_a[0] == point_b[0] and point_a[1] == point_b[1]:
        return 0.5
    if point_b[0] - point_a[0] == 0:
        return 2.0
    return (point_b[1] - point_a[1]) / (point_b[0] - point_a[0])


def is_in_square(pos, n, d):
    # 设长方形有4个点 A, B, C, D
    A = (0, d)
    # B = (d, 0)
    C = (n, n-d)
    # D = (n-d, n)
    if 1 >= slope(pos, A) >= -1 and 1 >= slope(pos, C) >= -1:
        return True
    else:
        return False


def func():
    n, d = input().split(" ")
    n = int(n)
    d = int(d)
    cases = int(input())

    i = 0
    while i < cases:
        pos = [int(x) for x in input().split(" ")]
        if is_in_square(pos, n, d):
            print("YES")
        else:
            print("NO")
        i += 1


func()
