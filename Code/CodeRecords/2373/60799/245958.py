T = int(input())
for txt in range(T):
    N = int(input())
    A = [int(i) for i in input().split(' ')]
    da = un = 0
    for i in A:
        tmp = un
        un = max(un, da)
        da = tmp + i
    print(max(un, da))