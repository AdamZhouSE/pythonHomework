n=int(input())
for p in range(n):
    a=int(input())
    b=[int(x) for x in input().split(" ")]
    c=[int(x) for x in input().split(" ")]
    b.sort()
    c.sort()
    if b==c:
        print(1)
    else:
        print(0)