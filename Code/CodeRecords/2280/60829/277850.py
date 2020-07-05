n=int(input())
for i in range(n):
    a=int(input())
    b=[int(x) for x in input().split(" ")]
    for i in range(1,a+2):
        if not i in b:
            print(i)
            break