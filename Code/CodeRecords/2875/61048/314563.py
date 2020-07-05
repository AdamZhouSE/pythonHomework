def arr11():
    n=int(input())
    ps=[int(x) for x in input().split(" ")]
    tmp=[-1]*n
    for i in range(n):
        tmp[ps[i]-1]=i+1
    for i in range(n):
        if(i!=n-1):
            print(tmp[i],end='')
            print(" ",end='')
        else:
            print(tmp[i])
    return

arr11()