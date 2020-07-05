def func(arr:list):
    lengtn=len(arr)
    need=-1
    for i in range(2,lengtn):
        arr1=arr[0:i]
        arr2=arr[i-1:lengtn]
        if max(arr1)==min(arr2) and max(arr1)==arr[i-1]:
            need=arr[i-1]
            break
    return need

tests=int(input())
lists=[]
for i in range(tests):
    l=input()
    lists.append(list(map(int,input().split(" "))))
res=[]
for i in lists:
    print(func(i))
    