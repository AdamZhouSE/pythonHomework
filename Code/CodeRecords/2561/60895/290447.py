t=int(input())
while t>0:
    t=t-1
    n,x=input().split(' ')
    n=int(n)
    x=int(x)
    index=0
    s1=[]
    s2=[]
    while index<n:
        temp=input().split(' ')
        for item in temp:
            s1.append(int(item))
        index=index+1
    while index<2*n:
        temp=input().split(' ')
        for item in temp:
            s2.append(int(item))
        index=index+1
    num=0
    for i in range(0,len(s1)):
        for j in range(0,len(s2)):
            if s1[i]+s2[j]==x:
                num=num+1
                break
    print(num)