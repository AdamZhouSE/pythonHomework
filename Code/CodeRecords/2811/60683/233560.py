src = [int(x) for x in input().split()]
n = src[0]
m = src[1]
lst = [0] * n
hit = False
for i in range(0, m):
    temp = eval(input()) % n
    lst[temp] += 1
    if lst[temp] != 1:
        print(i + 1)
        hit = True
        break
if not hit:
    print(-1)
