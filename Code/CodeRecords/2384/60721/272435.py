T=int(input())
num=[]
lis=[[] for i in range(0,T)]
for i in range(0,T):    
    num.append(int(input()))
    lis[i]=list(map(int,input().split(" ")))    
for i in range(0,T):
    a=num[i]
    for j in range(0,a):
        if(lis[i][j]<1):
            lis[i][j]=100000000
            
for i in range(0,T):
    lis[i].sort()
    if(lis[i][0]>1):
        print(1)
        continue
    temp=lis[i][0]
    for j in range(1,len(lis[i])):
        if(lis[i][j]-temp>1):
            print(temp+1)
            break
        temp=lis[i][j]
        if(j==len(lis[i])-1):
            print(temp+1)
        
            
            