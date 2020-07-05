def func(arr1:list,arr2:list):
    return sorted(arr1+arr2)

tests=int(input())
lists=[]
for i in range(tests):
    l=input()
    lists.append(list(map(int,input().split(" "))))
    lists.append(list(map(int, input().split(" "))))
res=[]
for i in range(int(len(lists)/2)):
    res.append(func(lists[i*2],lists[i*2+1]))
for i in res:
    for j in i:
        print(j,end=" ")
    print()