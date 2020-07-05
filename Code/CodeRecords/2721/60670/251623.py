def bin2int(str):
    n=0
    for c in str:
        n=n*2
        if c=='1':
            n=n+1
    return n

t=int(input())
for i in range(0,t):
    str1,str2=map(str,input().split(' '))
    a=bin2int(str1)
    b=bin2int(str2)
    print(a*b)