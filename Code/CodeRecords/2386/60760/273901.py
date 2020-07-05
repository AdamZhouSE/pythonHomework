def func(arr:list,x:int):   #三层遍历
    res=0
    length=len(arr)
    for i in range(length):
        for j in range(length):
            if j>i:
                for n in range(length):
                    if n>j:
                        for m in range(length):
                            if m>n:
                                if arr[i]+arr[j]+arr[n] +arr[m]==x:
                                    return 1
    return 0

tests=int(input())
lists=[]
xs=[]
for i in range(tests):
    l=input()
    lists.append(list(map(int,input().split(" "))))
    xs.append(int(input()))
for i in range(tests):
    print(func(lists[i],xs[i]))