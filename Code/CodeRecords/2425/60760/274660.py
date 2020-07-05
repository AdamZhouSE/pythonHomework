def func(arr:list,target:int):
    arr.append(target)
    arr=sorted(arr)
    indexof=arr.index(target)
    if target-arr[indexof-1]>=arr[indexof+1]-target:
        return arr[indexof+1]
    if target-arr[indexof-1]<arr[indexof+1]-target:
        return arr[indexof-1]
tests=int(input())
lists=[]
targets=[]
for i in range(tests):
    targets.append(list(map(int,input().split(" ")))[1])
    lists.append(list(map(int,input().split(" "))))
results=[]
for i in range(tests):
    print(func(lists[i],targets[i]))
