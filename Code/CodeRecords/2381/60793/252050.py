import math


def baseNeg2(N: int) -> str:
    if N == 0:
        digits = ['0']
    else:
        digits = []
        while N != 0:
            N, remainder = divmod(N, -2)
            if remainder < 0:
                N, remainder = N + 1, remainder + 2
            digits.append(str(remainder))
    return ''.join(digits[::-1])


def neg2_to_int(ls: list) -> int:
    result = 0
    for i in range(0, len(ls)):
        result += (math.pow(-2, len(ls) - 1 - i)) * int(ls[i])
    return result


a = neg2_to_int(list(map(int, input().split(","))))
b = neg2_to_int(list(map(int, input().split(","))))
print(list(baseNeg2(int(a + b))))