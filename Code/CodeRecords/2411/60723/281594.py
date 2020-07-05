T=int(input())
array=[[0 for _ in range(2)] for _ in range(T)]
for i in range(T):
    temp=input().split(',')
    array[i][0]=int(temp[0])
    array[i][1]=int(temp[1])
a=(array[1][1]-array[0][1])/(array[1][0]-array[0][0])
flag=True
for i in range(1,T):
    temp=(array[i][1]-array[i-1][1])/(array[i][0]-array[i-1][0])
    if temp!=a:
        flag=False
        break
print(flag)