T=int(input())
for i in range(0,T):
    num=int(input())
    numbin=bin(num)[2:]
    zero,one=0,0
    for j in range(0,len(numbin)):
        if numbin[j]=='0':
            zero=zero+1
        else:
            one=one+1
    result=one^zero
    print(result)