def f(x):
    cnt = 0
    while x != 0:
        cnt += x//5
        x //= 5
    return cnt

def solution(K):
    base = 4*K
    while True:
        v = f(base)
        if v==K:
            return 5
        elif v>K:
            return 0
        base+=5
    return 0

K = int(input())
print(solution(K))