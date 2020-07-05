def swap(num: int) -> int:
    charge = 0x3
    res = ''
    for _ in range(16):
        temp = num & charge
        if temp == 0:
            res = '00' + res
        elif temp == 1:
            res = '10' + res
        elif temp == 2:
            res = '01' + res
        elif temp == 3:
            res = '11' + res
        num >>= 2
    return int(res, 2)


t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    ans.append(swap(n))
for i in ans:
    print(i)