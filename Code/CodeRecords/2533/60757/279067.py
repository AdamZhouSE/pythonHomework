arr=eval(input())
li=[]
for i in range(len(arr)):
    if arr[i]%2==0:
        li.append(arr[i])
for i in range(len(arr)):
    if arr[i]%2==1:
        li.append(arr[i])
print(li)