def so(s1,s2,leng):
    if leng==1 and s1>s2:
        return 'NO'
    if s1==s2:
        return 'YES'
    flag = 0
    start,end=0,0
    for i in range(0,leng):
        if flag==0 and s1[i]!=s2[i]:
            start=i
            flag=1
        if s1[i]!=s2[i]:
            end=i
    diff = s1[start]-s2[start]
    if diff>0:
        return 'NO'
    for i in range(start,end+1):
        if s1[i]-s2[i]!=diff:
            return 'NO'
    return 'YES'
num= int(input())
for i in range(0,num):
    cons1=[]
    cons2=[]
    leng = int(input())
    s1=input().split(' ')
    s1=list(map(int,s1))
    s2=input().split(' ')
    s2=list(map(int,s2))
    print(so(s1,s2,leng))