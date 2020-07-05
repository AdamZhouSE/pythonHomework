def lucky_soldier(n: int) -> int:
    if n == 1:
        return 1
    soldiers = [i for i in range(1, n+1)]
    index = 1
    soldiers[1] = -1
    for i in range(n-2):
        j = 0
        while j < 2:
            if soldiers[(index+1) % n] != -1:
                j += 1
            index = (index + 1) % n
        soldiers[index] = -1
    return sum(soldiers) + n - 1


t = int(input())
res = []
for j in range(t):
    num = int(input())
    res.append(lucky_soldier(num))
for j in res:
    print(j)