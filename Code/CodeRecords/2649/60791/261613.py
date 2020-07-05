def solve(a):
    l = a[1] -1
    r = a[2] -1
    num = a[0]
    bi = []
    while(num!=0):
        bi.append(num%2)
        num = int(num/2)
    for i in range(l,r+1):
        bi[i] = 1 if bi[i] == 0 else 0
    res = 0
    for i in range(len(bi)):
        res += 2**i if bi[i] == 1 else 0
    return res


T = int(input())
x = 0
while(x<T):
    x+=1
    print(solve([int(i) for i in input().split(' ')]))