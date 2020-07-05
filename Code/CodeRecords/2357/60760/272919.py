def func(arr1:list,arr2:list,x:int):
    for i in arr1:
        for j in arr2:
            if i+j==x:
                print(i,j)
tests=int(input())
lists=[]
x=[]
for i in range(tests):
    x.append(list(map(int,input().split(" ")))[2])
    lists.append(list(map(int,input().split(" "))))
    lists.append(list(map(int, input().split(" "))))
res=[]
for i in range(int(len(lists)/2)):
    func(lists[i*2],lists[i*2+1],x[i])