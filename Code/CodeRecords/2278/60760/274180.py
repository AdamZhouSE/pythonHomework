def func(arr:list):
    length=len(arr)
    arr2=[]
    for i in range(length-1):
        arr2.append(arr[i]^arr[i+1])
    arr2.append(arr[length-1])
    return arr2
tests=int(input())
lists=[]
for i in range(tests):
    l=input()
    lists.append(list(map(int, input().split(" "))))
for i in lists:
    temp=(func(i))
    for i in range(len(temp)-1):
        print(temp[i],end=" ")
    print(temp[len(temp)-1])