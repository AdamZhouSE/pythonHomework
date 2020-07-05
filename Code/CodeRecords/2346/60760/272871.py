def func(arr:list,rows:int , lie:int):
    results=[]
    temp=func2(arr,rows,lie,results)
    while len(temp)>0:
        temp=func2(temp,rows-2,lie-2,results)
    return results
def func2(arr:list,rows:int , lie:int,results:list):
    arr2=list(arr)
    res = arr[0:lie]
    arr2=arr2[lie:len(arr2)]
    for i in range(2, rows):
        res.append(arr[i * lie-1])
        arr2.remove(arr[i * lie -1])
    for i in range(lie):
        if arr2!=[]:
            res.append(arr[len(arr)-i-1])
            arr2.remove(arr[len(arr)-i-1])
    for i in range(2, rows):
        res.append(arr[len(arr)-i*lie])
        arr2.remove(arr[len(arr)-i*lie])
    for i in res:
        print(i,end=" ")
    return arr2
tests=int(input())
sizes=[]
lists=[]
for i in range(tests):
    sizes.append(list(map(int,input().split(" "))))
    lists.append(list(map(int,input().split(" "))))
for i in range(tests):
    func(lists[i],sizes[i][0],sizes[i][1])
    print()
