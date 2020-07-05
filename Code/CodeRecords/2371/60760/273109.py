def func(arr:list):
    length=len(arr)
    if length%2==0:
        arr1 = arr[0:int(length / 2)]
        arr2 = arr[int(length / 2):length][::-1]
    else:
        arr1=arr[0:int(length/2)]
        arr2 = arr[int(length / 2)+1:length][::-1]
    if arr1==arr2:
        return "YES"
    else:
        return "NO"
tests=int(input())
lists=[]
for i in range(tests):
    lists.append(list("".join(input().lower().split(" "))))
for i in lists:
    for j in i:
        if j<'a' or j>'z':
            i.remove(j)
    while i.count('/')>0:
        i.remove('/')
for i in lists:
    print(func(i))
