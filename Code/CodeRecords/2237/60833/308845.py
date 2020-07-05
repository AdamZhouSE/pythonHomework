num_list=input().split(' ')
n=int(num_list[0])
m=int(num_list[1])
res=[i for i in range(1,n+1)]
for i in range(0,m):
    num_list = list(map(int,input().split(' ')))
    a=num_list[0]
    b=num_list[1]
    temp=res[a-1:b]
    temp=temp[::-1]
    res[a-1:b]=temp
for i in res:
    print(str(i),end=' ')