def func2(arr,k):
    tmp=[]
    count=0
    for i in range(len(arr)):
        if int(arr[i])>k:
            tmp.append(i)
    if len(tmp)==1:
        count=1
    else:
        for i in range(len(tmp)-1):
            count=max(count,tmp[i+1]-tmp[i]+1)
    print(len(arr)-count)
k=int(input().split(" ")[-1])
arr=input().split(" ")
func2(arr,k)
