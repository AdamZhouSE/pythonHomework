num=input().replace("[","").replace("]","").split(",")
arr=[]
for i in num:
    arr.append(int(i))
arr.sort()
max=0
for i in range(len(arr)):
    flag=True
    index=arr[i]
    count=0
    while(flag==True):
        if index in arr:
            flag=True
            count = count+1
        else:
            flag=False
        index=index+1
    if max<count:
        max=count
print(max)           