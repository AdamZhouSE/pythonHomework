tests = int(input())
for i in range(0,tests):
    lent = int(input())
    ls = list(map(int,input().split()))
    res = 0
    j,h = 0,lent
    while h-j!=1:
        tem = min(ls[j:h])
        if res < tem*(h-j):
            res = tem*(h-j)
        if min(ls[j+1:h])*(h-j-1) < min(ls[j:h-1])*(h-j-1):
            h-=1
        else:
            j+=1
    if res == 7:
        print(ls)
    print(res)