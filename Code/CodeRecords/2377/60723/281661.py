T=int(input())
array=[[0 for _ in range(2)] for _ in range(T)]
for i in range(T):
    temp=input().split(',')
    array[i][0]=int(temp[0])
    array[i][1]=int(temp[1])
a=(array[1][1]-array[0][1])/(array[1][0]-array[0][0])
b=(array[2][1]-array[1][1])/(array[2][0]-array[1][0])
print(a*b<0)