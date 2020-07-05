import math


def solution(n: int) -> bool:
    ls_n = list(sorted([int(x) for x in str(n)]))
    for i in range(0, int(math.log(n, 2)) + 1):
        ls_i = list(sorted([int(y) for y in str(2**i)]))
        if ls_i == ls_n:
            return True
    return False


print(solution(int(input())))