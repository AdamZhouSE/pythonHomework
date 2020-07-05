ucnum = int(input())
ans = list()
for i in range(ucnum):
    n = int(input())
    if n<=3:
        ans.append(1)
        continue
    p0 = 1
    p1 = 1
    p2 = 1
    p3 = 2
    n-=3
    while n>0:
#        print(p3)
        temp = p1+p2
        p1 = p2
        p2 = p3
        p3 = temp
        n-=1
    ans.append(p3)    
for i in ans:
    print(i)
