num=list(map(int,input().split()))
lst1=list(map(int,input().split()))
lst2=[list(map(int,input().split())) for i in range(num[1])]

for i in  lst2:
    k=i[0]
    v=i[1]
    temp=lst1[k-1:v]
    print(min(temp),end=" ")