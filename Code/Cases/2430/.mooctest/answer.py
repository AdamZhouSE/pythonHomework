t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    s=input().split(' ')
    k=int(input())
    for i in range(n):
        s[i]=int(s[i])
    p=-1
    i=0;j=n-1
    while(i<j):
        if(s[i]+s[j]==k):
            p=0
            print(s[i],s[j],k)
            i+=1
            j-=1
        elif(s[i]+s[j]<k):
            i+=1
        else:
            j-=1
    if(p==-1):
        print(-1)