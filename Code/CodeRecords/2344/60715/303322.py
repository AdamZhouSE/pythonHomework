T = int(input())
while T > 0:
    n = int(input())
    num = [int(n) for n in input().split()]
    d = int(input())
    a=num[d:]
    b=num[0:d]
    for i in b:
        a.append(i)
    le=0
    for i in a:
        le+=1
        if le==len(a):
            print(i,end=' \n')
        else:
            print(i,end=' ')
    T-=1