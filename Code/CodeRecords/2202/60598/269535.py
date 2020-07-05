times = int(input())


def cal(m, n):
    if n == 0:
        return 1
    if n == 1:
        return m
    UP = 1
    DOWN = 1
    for i in range(n):
        UP *= (m-i)
        DOWN *= (n-i)
    return UP/DOWN


for j in range(times):
    length = int(input())
    result = 0
    circul = length//2+1
    for k in range(circul):
        result += cal(length-k,k)

    print(int(result))
