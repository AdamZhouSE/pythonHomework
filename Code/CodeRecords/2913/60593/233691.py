def dell(arr):
    ret=[]
    for i in range(0,len(arr)-1,2):
        if(arr[i]<arr[i+1]):
            ret.append(arr[i+1]-arr[i])
        elif(arr[i]>arr[i+1]):
            ret.append(arr[i]-arr[i+1])
    if(len(arr)%2==1):
        ret.append(arr[len(arr)-1])
    return ret
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
while(len(arr)!=len(dell(arr))):
    arr=dell(arr)
print('YES' if (len(arr)==0) else'NO')