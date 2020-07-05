def func(arr:list):
    arr2=sorted(arr)
    res=0
    for i in range(len(arr2)):
        count=0
        for j in range(i,len(arr2)-1):
            if arr2[j+1]-arr2[j]==1:
                count+=1
        if count>res:
            res=count


    return res+1
a=input()
arr=list(map(int,a[1:len(a)-1].split(',')))
print(func(arr))