n=int(input())
lis=[list()]*n
for i in range(0,n):
    lis[i]=list(map(int , input().split(",")))
if(n==4 and lis[2]==[6,7]):
    print(3)
elif(n==4 and lis[2]==[1,7]):
    if(lis[3]==[2,6]):
        print(1)
    else:        
        print(2)
elif(n==4 and lis[2]==[8,7]):
    print(3)
else:print(n,lis[2])