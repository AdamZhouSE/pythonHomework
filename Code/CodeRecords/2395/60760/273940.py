def func2(arr:list):
    numof0=arr.count(0)
    for i in range(numof0):
        arr.remove(0)
    arr2=arr+list('0'*numof0)
    for i in range(len(arr2)-1):
        print(arr2[i],end=" ")
    print(arr2[-1])

def func(arr:list):
    length=len(arr)
    for i in range(length-1):
        if arr[i]==arr[i+1] and arr[i]>0:
            arr[i]=arr[i]*2
            arr[i+1]=0
    func2(arr)
tests=int(input())
lists=[]
for i in range(tests):
    l=input()
    lists.append(list(map(int,input().split(" "))))
for i in range(tests):
    func(lists[i])