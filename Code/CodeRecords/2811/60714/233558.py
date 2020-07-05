p, n = [int(x) for x in input().split()]
num = [int(input())]
for i in range(1, n):
    num.append(int(input()))
table = [False for i in range(0, p)]
temp = False
for i in range(0, n):
    if table[num[i] % (p - 1)]:
        print(i)
        temp = True
        break
    else:
        table[num[i] % (p - 1)] = True
if not temp:
    print(-1)
