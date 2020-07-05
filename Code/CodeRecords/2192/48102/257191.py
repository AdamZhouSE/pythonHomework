def out(num: int) -> list:
    res = []
    while num > 0:
        res.append(num)
        num -= 5
    temp = num
    ans = res + [temp] + res[-1::-1]
    return ans


t = int(input())
ls = []
for i in range(t):
    n = int(input())
    ls.append(out(n))
for i in ls:
    for j in range(len(i)-1):
        print(str(i[j]) + ' ', end='')
    print(str(i[len(i)-1]) + ' ')

    