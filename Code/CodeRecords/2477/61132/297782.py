n = int(input())
for j in range(n):
    alist = list(map(int, input().split()))
    blist = list(map(int, input().split()))
    f = lambda x: [x[2], x[3], x[0], x[1]] if x[0] > x[2] else x
    alist = f(alist)
    blist = f(blist)
    if alist[0] == alist[2] or alist[1] == alist[3] or blist[0] == blist[2] or blist[1] == blist[3]:
        print(0)
    else:
        if alist[0] < blist[2] and alist[1] > blist[3] and alist[2] > blist[0] and alist[3] < blist[1]:
            print(1)
        else:
            print(0)