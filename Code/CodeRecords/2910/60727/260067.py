def so(arr,ll):
    if len(arr)==4:
        return 'NO'
   
    for i in range(0,len(arr)-1):
        if max(arr[i][1],arr[i][0])<min(arr[i+1][1],arr[i+1][0]):
            return 'NO'
    return 'YES'
num=int(input())
arr=[]
ll=[]
for i in range(0,num):
    d= input().split(' ')
    d=list(map(int,d))
    d=sorted(d)
    arr.append(d)
    ll.append(d[1])
print(so(arr,ll))
