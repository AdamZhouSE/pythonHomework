arr=input()[2:-2].split('[')
for i in range(0,len(arr)-1):
    arr[i]=arr[i][:-2]
for i in range(0,len(arr)):
    arr[i]=arr[i].split(',')
for i in range(0,len(arr)):
    for j in range(0,len(arr[i])):
        arr[i][j]=int(arr[i][j])
num=0
for i in range(0,len(arr)):
        for j in range(0,len(arr[i])):
            i1=i
            j1=j
            while i1<len(arr) and j1<len(arr[i]):
                num=num+1
                i1=i1+1
                j1=j1+1
            for m in range(0,num):
                for n in range(0,num-1):
                    if arr[i+n][j+n]>arr[i+n+1][j+n+1]:
                        temp=arr[i+n][j+n]
                        arr[i+n][j+n]=arr[i+n+1][j+n+1]
                        arr[i+n+1][j+n+1]=temp
            num=0
print(arr)
