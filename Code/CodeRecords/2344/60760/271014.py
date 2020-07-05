def func(arr:list,k:int):
    list1=arr[0:k]
    list2=arr[k:len(arr)]
    return list2+list1
tests=int(input())
lists=[]
ks=[]
for i in range(tests):
    l=input()
    lists.append(list(map(int,input().split(" "))))
    ks.append(int(input()))
res=[]
for i in range(len(lists)) :
    res.append(func(lists[i],ks[i]))
for i in res:
    for j in range(len(i)-1):
        print(i[j],end=" ")
    print(i[len(i)-1])