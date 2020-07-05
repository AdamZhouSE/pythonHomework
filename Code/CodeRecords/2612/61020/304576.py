import itertools
import math


def Euclid_distance(A, B):
    return math.sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2)


def Manhattan_distance(A, B):
    return int(math.fabs(A[0] - B[0])) + int(math.fabs(A[1] - B[1]))


def same_two_distance(A, B):
    return Euclid_distance(A, B) == Manhattan_distance(A, B)


T = int(input())
for i in range(T):
    N = int(input())
    points = []
    for line in range(N):
        x_y = input().split()
        x = int(x_y[0])
        y = int(x_y[1])
        points.append((x, y))

    pairs_of_point = list(itertools.combinations(points, 2))

    num_of_pairs = 0
    for pair in pairs_of_point:
        if same_two_distance(pair[0], pair[1]):
            num_of_pairs += 1

    print(num_of_pairs)
