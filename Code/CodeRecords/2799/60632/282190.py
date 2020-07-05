def is_pow_2(x) -> bool:
    if x % 1 != 0:
        return False
    for i in range(10):
        if x == int(pow(2, i)):
            return True
    return False


def is_pow_3(x) -> bool:
    if x % 1 != 0:
        return False
    for i in range(10):
        if x == int(pow(3, i)):
            return True
    return False


n = int(input())
data = list(map(int, input().split(' ')))
sign = [0 for i in range(n)]
big = max(data)
for i in range(5):
    big *= 2
    for j in range(len(data)):
        if sign[j] == 0:
            if is_pow_2(big / data[j]) or is_pow_3(big / data[j]):
                sign[j] = 1
for i in range(5):
    big *= 3
    for j in range(len(data)):
        if sign[j] == 0:
            if is_pow_2(big / data[j]) or is_pow_3(big / data[j]):
                sign[j] = 1
if all(sign):
    print('Yes')
else:
    print('No')
