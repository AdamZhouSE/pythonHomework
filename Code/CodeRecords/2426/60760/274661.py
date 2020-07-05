def func(arr:list):
    length=len(arr)
    maxvalue=0
    for i in range(length):
        for j in range(length):
            if j>i:
                for m in range(length):
                    if m>j:
                        if arr[i]*arr[j]*arr[m]>=maxvalue:
                            maxvalue=arr[i]*arr[j]*arr[m]
    print(maxvalue)
tests=int(input())
lists=[]
for i in range(tests):
    l=input()
    lists.append(list(map(int,input().split(" "))))
for i in range(tests):
    func(lists[i])