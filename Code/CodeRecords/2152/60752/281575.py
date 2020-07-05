size=int(input())
val=list(map(int,input().split()))
addr=list(map(int,input().split()))
m=0
for i in range(size):
    vall=val.copy()
    orz=i
    sum=0
    while vall[orz]>0:
        sum+=vall[orz]
        vall[orz]=-1
        orz=addr[orz]-1
    print(sum)