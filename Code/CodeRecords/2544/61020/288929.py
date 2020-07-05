def has_k(point0, point1):
    return point0[0] != point1[0]


def k_of(point0, point1):
    if has_k(point0, point1):
        return (point1[1] - point0[1]) / (point1[0] - point0[0])
    else:
        return None


def b_of(pointA, pointB):
    return pointA[1] - k_of(pointA, pointB) * pointB[0]


def isCross(A, B, C, D):
    if has_k(A, B) and has_k(C, D):
        if k_of(A, B) == k_of(C, D):
            return False
        else:
            x_of_crossPoint = (b_of(C, D) - b_of(A, B)) / (k_of(A, B) - k_of(C, D))
            return ((x_of_crossPoint <= A[0]) != (x_of_crossPoint <= B[0])) and ((x_of_crossPoint <= C[0]) != (
                    x_of_crossPoint <= D[0]))

    if (not has_k(A, B)) and (not has_k(C, D)):
        return False

    if has_k(A, B) and (not has_k(C, D)):
        if (C[0] <= A[0]) != (C[0] <= B[0]):
            y = k_of(A, B) * C[0] + b_of(A, B)
            return (y <= C[1]) != (y <= D[1])

        else:
            return False

    return isCross(C, D, A, B)


T = int(input())

for i in range(0, T):
    line_0 = input().split()
    line_1 = input().split()

    A = [int(line_0[0]), int(line_0[1])]
    B = [int(line_0[2]), int(line_0[3])]
    C = [int(line_1[0]), int(line_1[1])]
    D = [int(line_1[2]), int(line_1[3])]

    if isCross(A, B, C, D):
        print('1')
    else:
        print('0')
