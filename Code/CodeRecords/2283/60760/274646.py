def func(arr:list):
    arr=sorted(arr)
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()
tests=int(input())
lists=[]
for i in range(tests):
    l=input()
    lists.append(list(map(int,input().split(" "))))
for i in range(tests):
    func(lists[i])