def func(arr:list):
    length=len(arr)
    maxi=max(arr)
    res=[]
    for i in range(length):
        mini=min(arr[i:])
        indes=arr.index(mini)
        temp=arr[i:indes+1][::-1]
        arr=arr[0:i]+temp+arr[indes+1:]
        res.append(indes+1)
    for i in res:
        print(i,end=' ')
    return 0
a=input()
lists=list(map(int,input().split(' ')))
func(lists)