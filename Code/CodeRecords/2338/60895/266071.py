t=int(input())
while t>0:
    t=t-1
    n,x=input().split(' ')
    N=int(n)
    X=int(x)
    s=input().split(' ')
    result='No'
    for i in range(0,N-1):
        for j in range(i+1,N):
            if int(s[i])+int(s[j])==X:
                result='Yes'
                break
        if result=='Yes':
            break
    print(result)