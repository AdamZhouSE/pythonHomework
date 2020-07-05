a=eval(input())    
for i in range(0,a):
    n=eval(input())
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    result=-1
    for t in range(1,n-1):
        c=list1[t]
        dec=True
        for j in range(0,t):
            if(list1[j]>c):
                dec=False
                break
        for j in range(t+1,n):
            if(list1[j]<c):
                dec=False
                break
        if(dec):
            result=c
            break
    print(result)
            