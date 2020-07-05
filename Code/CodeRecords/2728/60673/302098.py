t = int(input())
for i in range(0, t):
    n = int(input())
    inp = input().split(' ')
    if inp[-1] == '':
        a = inp[0:len(inp) - 1]
    else:
        a = inp
    res = 0
    for i in range(0, len(a) - 1):
        for j in range(i + 1, len(a)):
            temp = min(int(a[i]), int(a[j])) * (j - i)
            if temp > res:
                res = temp
    print(res)