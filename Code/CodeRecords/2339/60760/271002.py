def func(arr:list):
    cou=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if j>i and arr[j]<arr[i]:
                cou=cou+1
    return cou
tests=int(input())
lists=[]
for i in range(tests):
    l=input()
    lists.append(list(map(int,input().split(" "))))
res=[]
for i in lists:
    res.append(func(i))
for i in res:
    print(i)