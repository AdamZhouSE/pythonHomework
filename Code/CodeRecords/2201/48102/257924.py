def find_min_prime(n1: int, n2: int) -> int:
    res = n1 + n2 + 1
    while not is_prime(res):
        res += 1
    return res - n1 - n2


def is_prime(num: int) -> bool:
    import math
    if num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(num))+1, 2):
            if num % i == 0:
                return False
        return True


t = int(input())
ans = []
for j in range(t):
    ls = input().split(' ')
    num1 = int(ls[0])
    num2 = int(ls[1])
    ans.append(find_min_prime(num1, num2))
for j in ans:
    print(j)