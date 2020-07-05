a=int(input())
for k in range(0,a):
    n=int(input().split(' ')[1])
    b=input().split(' ')
    for i in range(0,len(b)):
        b[i]=int(b[i])
    result=0
    for i in range(0,len(b)-n+1):
        if sum(b[i:n+i])>result:
            result=sum(b[i:i+n])
    print(result)