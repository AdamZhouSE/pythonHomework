str=input()
arr=[]
for i in range(0,len(str)):
    arr=arr+[str]
    str=str[1:]+str[0:1]
for i in range(0,len(str)):
    for j in range(0,len(str)-1):
        if ord(arr[j][0:1])>ord(arr[j+1][0:1]):
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
res=""
for i in range(0,len(str)):
    res=res+arr[i][-1:]
print(res,end="")
