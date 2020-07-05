def func(arr1:list,arr2:list):
    res=[]
    length=len(arr1)
    for i in range(length):
        temp=arr2[i]
        ishave=[i+1,temp]
        result=arr1[temp-1]
        while ishave.count(arr2[temp-1])<1:
            temp=arr2[temp-1]
            ishave.append(temp)
            result+=arr1[temp-1]
        if temp!=i+1:
            result+=arr1[i]
        res.append(result)
    for i in res:
        print(i)
    return 0
a=input()
arr1=list(map(int,input().split(' ')))
arr2=list(map(int,input().split(' ')))
func(arr1,arr2)