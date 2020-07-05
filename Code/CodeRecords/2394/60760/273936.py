def func(arr:list):
    numof0=arr.count(0)
    for i in range(numof0):
        arr.remove(0)
    arr2=arr+list('0'*numof0)
    for i in range(len(arr2)-1):
        print(arr2[i],end=" ")
    print(arr2[-1])
tests=int(input())
lists=[]
for i in range(tests):
    l=input()
    lists.append(list(map(int,input().split(" "))))
for i in range(tests):
    func(lists[i])
