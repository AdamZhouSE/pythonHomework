def isPerfect(n: int) -> bool:
    tmp = 0
    for i in range(1, n):
        if n % i == 0:
            tmp += i
    if tmp == n :
        return True
    return False
num = int(input())
print(isPerfect(num))