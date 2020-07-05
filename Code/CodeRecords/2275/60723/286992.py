num=int(input())
array1=[]*num
array2=['']*num
for i in range(num):
    temp=input().split(',')
    temp=''.join(temp)
    array1.append(temp)
    for j in range(num):
        array2[j]=array2[j]+temp[j]
count=0
flag=True
for i in range(num):
    if i%2==0 and array1[i][0]!=array1[0][0]:
        count=count+1
    elif i%2==1 and array1[i][0]==array1[0][0]:
        count=count+1
if count%2!=0:
    flag=False
for i in range(num):
    if i%2==0 and array2[i][0]!=array2[0][0]:
        count=count+1
    elif i%2==1 and array2[i][0]==array2[0][0]:
        count=count+1
if count%2!=0:
    flag=False
if flag:
    print(int(count/2))
else:
    print(-1)