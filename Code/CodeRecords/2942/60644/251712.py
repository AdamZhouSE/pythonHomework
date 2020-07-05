num=int(input())
arr=input().split()

for i in range(0,len(arr)):
    for j in range(0,len(arr)-1):
        if int(arr[j][0:1])<int(arr[j+1][0:1]):
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
        if int(arr[j][0:1])==int(arr[j+1][0:1]):
            try:
                if int(arr[j][1:2]) < int(arr[j+1][1:2]):
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp
            except:
                if len(arr[j])<len(arr[j+1]):
                    if int(arr[j][0:1])<int(arr[j+1][1:2]):
                        temp = arr[j]
                        arr[j] = arr[j + 1]
                        arr[j + 1] = temp

str=""
for i in range(0,len(arr)):
    str=str+arr[i]
print(str,end="")