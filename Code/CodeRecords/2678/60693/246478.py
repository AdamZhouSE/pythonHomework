cases=int(input())
for i in range(cases):
    n=bin(int(input()))
    loc,numof1=-1,0
    i=len(n)-1
    while i>1:
        if n[i]=='1':
            numof1+=1
            loc=i
        i-=1
    if numof1==1:print(len(n)-loc)
    else:print(-1)