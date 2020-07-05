n=int(input())
lis=list(map(int,input().split(' ')))
if(n==2):
    if(lis[0]==lis[1] or lis[0]<lis[1]):
        print(0)
    else:
        print(1)
else:
    a=lis[0]
    q=True
    ma=max(lis)
    fen=lis.index(ma)
    count=0
    for i in range(0,fen+1):
        if(i==fen):
            break
        if(lis[i]>lis[i+1]):
            q=False
    for i in range(fen+1,len(lis)):
        if(lis[i]==ma):
            continue
        count+=1
        if(lis[i]>a):
            q=False
        if(i==len(lis)-1):
            break
        if(lis[i]>lis[i+1]):
            q=False
    if(q==False):     
        print(-1)
    else:
        print(count)
        
    