def func(arr:list,k:int ):
    arr=sorted(arr)[::-1]
    for i in range(k):
        print(arr[i],end=" ")
    print()
tests=int(input())
lists=[]
k=[]
for i in range(tests):
    k.append(list(map(int,input().split(" ")))[1])
    lists.append(list(map(int,input().split(" "))))
res=[]
for i in range(tests):
    func(lists[i],k[i])