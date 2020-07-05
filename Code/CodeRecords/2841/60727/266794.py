def so(x,y,arr):
    arr[x-1]=y
    while True:
        temp=[]
        for i in range(0,len(arr)-1,+2):
            temp.append(arr[i]|arr[i+1])
        if len(temp)==1:
            return temp[0]
        arr=temp
        temp=[]
        for i in range(0,len(arr)-1,+2):
            temp.append(arr[i]^arr[i+1])
        if len(temp)==1:
            return temp[0]
        arr=temp
        temp=[]
                        
a=input().split(' ')
a=[int(x) for x in a]
n,m=a[0],a[1]
arr = input().split(' ')
arr=[int(x) for x in arr]
for i in range(0,m):
    a=input().split(' ')
    a=[int(x) for x in a]
    x,y=a[0],a[1]
    print(so(x,y,arr))