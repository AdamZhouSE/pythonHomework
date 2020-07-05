def triangle_zone(A, B, C):
    len_a = len_side(B, C)
    len_b = len_side(C, A)
    len_c = len_side(B, A)
    s = (len_a + len_b + len_c) / 2
    zone = s * (s - len_a) * (s - len_b) * (s - len_c)
    # 海伦公式
    if zone < 0:
        return 0
    else:
        return zone ** 0.5


def len_side(B, C):
    length = ((B[0] - C[0]) ** 2 + (B[1] - C[1]) ** 2) ** 0.5
    return length


def is_in_triangle(point, A, B, C):
    three_zone = triangle_zone(point, A, B) + triangle_zone(point, A, C) + triangle_zone(point, B, C)
    one_zone = triangle_zone(A, B, C)
    return abs(one_zone - three_zone) <= 0.00001


def slope(point, C):
    if point[0] - C[0] == 0:
        return 999
    return (point[1] - C[1]) / (point[0] - C[0])


def is_same_line(point, A, C):
    return abs(slope(point, A) - slope(point, C)) <= 0.00001


def get_points_num():
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]

    x_s = [A[0], B[0], C[0]]
    y_s = [A[1], B[1], C[1]]

    left_bound = min(x_s)
    right_bound = max(x_s)
    up_bound = max(y_s)
    down_bound = min(y_s)

    points_num = 0
    i = left_bound + 1
    while i < right_bound:
        j = up_bound - 1
        while j > down_bound:
            if is_in_triangle([i, j], A, B, C) and not is_same_line([i, j], A, B) \
                    and not is_same_line([i, j], A, C) and not is_same_line([i, j], C, B):
                points_num += 1
            j -= 1
        i += 1

    return points_num


def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        print(get_points_num())
        i += 1


func()
