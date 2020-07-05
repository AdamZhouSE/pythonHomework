def func(arr:list):
    for i in arr:
        if arr.count(i)>1:
            return i
a=input()
arr=list(map(int,a.split(',')))
print(func(arr))