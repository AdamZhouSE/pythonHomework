def findNumber(n: int) -> int:
    cnt = 0
    while n != 1 :
        if n % 2 == 0:
            n = n / 2
        else:
            n -= 1
        cnt += 1
    return cnt
n = int(input())
print(findNumber(n))