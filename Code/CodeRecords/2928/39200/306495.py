v = int(input())
an = [int(x) for x in input().split()]
mina = min(an)
bn = [x - mina for x in an]
if mina > v:
    print(-1)
else:
    digits = v // mina
    duoyuv = v - digits * mina
    count = 0
    for x in range(8, -1, -1):
        while duoyuv >= bn[x] and digits - count > 0:
            duoyuv -= bn[x]
            print(x + 1, end = "")
            count += 1
    print()
