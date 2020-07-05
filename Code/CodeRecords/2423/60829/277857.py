n=int(input())
for i in range(n):
    a=[int(x) for x in input().split(" ")]
    b=[int(x) for x in input().split(" ")]
    c=[int(x) for x in input().split(" ")]
    b.sort()
    c.sort()
    judge=1
    for j in c:
        if not j in b:
            print("No")
            judge=0
            break
    if judge==1:
        print("Yes")