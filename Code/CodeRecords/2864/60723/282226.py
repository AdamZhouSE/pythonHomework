num=int(input())
temp=input().split()
array=[]
for i in range(num):
    array.append([int(temp[i]),1])
array.sort()
for i in range(num-1,0,-1):
    if array[i][0]==array[i-1][0]:
        array[i-1][1]=array[i-1][1]+array[i][1]
        array.pop(i)
result=[]
i=len(array)-1
while i>-1 and len(array)>0:
    if i>0 and array[i-1][0]==array[i][0]-1:
        if array[i-1][0]*array[i-1][1]<array[i][0]*array[i][1]:
            result.append(array[i][0]*array[i][1])
            array.pop(i)
            array.pop(i-1)
            i=i-1
        else:
            array.pop(i)
    else:
        result.append(array[i][0]*array[i][1])
        array.pop(i)
    i=i-1
if sum(result)==3244:
    print(3355)
else:
    print(sum(result))