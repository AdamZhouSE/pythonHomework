def func(arr:list):
    res=0
    length=len(arr)
    for i in range(length):
        for j in range(length):
            if j>i:
                for n in range(length):
                    if n>j:
                        if arr[i]+arr[j]==arr[n] or arr[i]+arr[n]==arr[j] or arr[n]+arr[j]==arr[i]:
                            res=res+1
    if res==0:
        print(-1)
    else:
        print(res)
tests=int(input())
lists=[]
for i in range(tests):
    l=input()
    lists.append(list(map(int,input().split(" "))))
for i in lists:
    func(i)