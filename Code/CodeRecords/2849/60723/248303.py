length=int(input())
array=input()
array=array.split(' ')
for i in range(len(array)):
    array[i]=int(array[i])
array.sort()
minimun=min(array)
flag=True
for item in array:
    if item%minimun!=0:
        flag=False
if flag:
    print(minimun)
else:
    print(-1)