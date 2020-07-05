n=int(input())
lis=[]
for i in range(0,n):
    lis.append(list(map(int,input().split(","))))
k1=(lis[0][1]-lis[1][1])/(lis[0][0]-lis[1][0])
k2=(lis[1][1]-lis[2][1])/(lis[1][0]-lis[2][0])
print(k1==k2)