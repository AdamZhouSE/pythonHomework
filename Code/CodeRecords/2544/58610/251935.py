def cross_mul(point1: tuple, point2: tuple):
    return point1[0] * point2[1] - point1[1] * point2[0]

def vector(point1, point2) -> tuple:
    return point2[0] - point1[0], point2[1] - point1[1]

for _ in range(eval(input())):
    segment1 = list(map(int, input().split(' ')))  # A B
    segment2 = list(map(int, input().split(' ')))  # C D
    AD = vector(segment1[:2], segment2[2:])
    AB = vector(segment1[:2], segment1[2:])
    AC = vector(segment1[:2], segment2[:2])
    CA = vector(segment2[:2], segment1[:2])
    CB = vector(segment2[:2], segment1[2:])
    CD = vector(segment2[:2], segment2[2:])
    print(1) if cross_mul(AD, AB) * cross_mul(AC, AB) < 0 and cross_mul(CA, CD) * cross_mul(CB, CD) < 0 else print(0)