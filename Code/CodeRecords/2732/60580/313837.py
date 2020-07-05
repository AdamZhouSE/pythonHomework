size = int(input())
for i in range(size):
    tL = input().split()
    a = tL[0]
    b = int(tL[1])
    c = int(tL[2])
    num = 0
    for i in range(len(a)):
        num = (num * 10 + int(a[i]))
        num = num % c
    ans = num
    mul = ans
    for i in range(1, b):
        ans = (ans * mul) % c
    print(ans)