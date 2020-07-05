def func(arr1:list,arr2:list):
    arr2.sort()
    arr1.sort()
    res=[]
    for i in arr1:
        if arr2.count(i)>0:
           res.append(i)    
    return res
        
a=input()
b=input()
arr1=list(map(int,a[1:len(a)-1].split(',')))
arr2=list(map(int,b[1:len(b)-1].split(',')))
print(func(arr1,arr2))
