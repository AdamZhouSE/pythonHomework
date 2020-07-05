

def is_prime(i=0):
    ip = True
    if i == 1:
        return False
    elif i == 2:
        return True
    else:
        for j in range(2, i):
            if i % j == 0:
                return False
        return True


def perm(i=1):
    res = 1
    for j in range(1, i + 1):
        res *= j
    return res


n = int(input())
count_prim = 0
for i in range(1, n + 1):
    if is_prime(i):
        count_prim += 1
print((perm(count_prim) * perm(n - count_prim)) % (7 + 10 ** 9))
