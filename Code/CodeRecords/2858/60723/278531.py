num=int(input())
array=[[0 for _ in range(num)] for _ in range(num)]
for i in range(num):
    array[i][0]=1
    array[0][i]=1
for i in range(1,num):
    for j in range(1,num):
        array[i][j]=array[i-1][j]+array[i][j-1]
print(array[num-1][num-1])