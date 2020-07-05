ucnum = int(input())
ans = list()
for i in range(ucnum):
    n = int(input())
    if n<=3:
        ans.append(1)
        continue
    p1 = 1
    p2 = 1
    p3 = 1
    n-=3
    while n>0:
        temp = p2+p3
        p2 = p1
        p3 = p2
        p1 = temp
        n-=1
    ans.append(p1)
for i in ans:
    print(i)