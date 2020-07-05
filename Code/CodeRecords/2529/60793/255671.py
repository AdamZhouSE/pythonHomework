import math


def solution(n: int) -> str:
    ls_n = list(sorted([int(x) for x in str(n)]))
    for i in range(0, int(math.log(n, 2)) + 1):
        ls_i = list(sorted([int(y) for y in str(2**i)]))
        if ls_i == ls_n:
            return "true"
    return "false"


print(solution(int(input())))