def judge(array,i,j):
    count=0
    if i>0:
        if array[i-1][j]=='o':
            count=count+1
    if i<len(array)-1:
        if array[i+1][j]=='o':
            count=count+1
    if j>0:
        if array[i][j-1]=='o':
            count=count+1
    if j<len(array)-1:
        if array[i][j+1]=='o':
            count=count+1
    return count%2==0
num=int(input())
array=[['' for _ in range(num)] for _ in range(num)]
for i in range(num):
    temp=input()
    for j in range(num):
        array[i][j]=temp[j]
flag=True
for i in range(num):
    for j in range(num):
        if not judge(array,i,j):
            flag=False
if flag:
    print("YES")
else:
    print("NO")